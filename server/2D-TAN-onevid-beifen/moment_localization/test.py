import os
import math
import argparse
import pickle as pkl

from tqdm import tqdm
import numpy as np
import torch
from torch.utils.data import DataLoader

import _init_paths
from core.engine import Engine
import datasets
import models
from core.utils import AverageMeter
from core.config import config, update_config
from core.eval import eval_predictions, display_results
import models.loss as loss

import time

os.environ["CUDA_VISIBLE_DEVICES"] = '0,1,2,3'  

torch.manual_seed(0)
torch.cuda.manual_seed(0)

#分类结果，真值，数据集名，测试/训练  save_scores(state['sorted_segments_list'], annotations, config.DATASET.NAME, args.split)
def save_scores(scores, data, dataset_name, split):
    results = {}
    for i, d in enumerate(data):#index，value
        #data的d：annotations.append({'video':vid, 'times':[s_time, e_time], 'description': sent, 'duration': self.durations[vid]})
        results[d['video']+'_'+d['description']] = scores[i]
    print(results)

if __name__ == '__main__':
    update_config('experiments/charades/2D-TAN-16x16-K5L8-pool.yaml')
    

    device = ("cuda" if torch.cuda.is_available() else "cpu" )
    model = getattr(models, config.MODEL.NAME)()
    model_checkpoint = torch.load(config.MODEL.CHECKPOINT)
    model.load_state_dict(model_checkpoint)
    if torch.cuda.device_count() > 1:
        print("Using", torch.cuda.device_count(), "GPUs")
        model = torch.nn.DataParallel(model)
    model  = model.to(device)
    model.eval()


    def network(sample):
        anno_idxs = sample['batch_anno_idxs']
        textual_input = sample['batch_word_vectors'].cuda()
        textual_mask = sample['batch_txt_mask'].cuda()
        visual_input = sample['batch_vis_input'].cuda()
        map_gt = sample['batch_map_gt'].cuda()
        duration = sample['batch_duration']

        # map_mask二进制掩码，用于指示模型预测的地图中哪些位置应该被考虑在内，哪些位置应该被忽略
        # 调用tan（继承nn.Model）中的forward：def forward(self, textual_input, textual_mask, visual_input)
        prediction, map_mask = model(textual_input, textual_mask, visual_input)#生成预测结果和地图掩码（用于计算loss）
        loss_value, joint_prob = getattr(loss, config.LOSS.NAME)(prediction, map_mask, map_gt, config.LOSS.PARAMS)#name：bce_rescale_loss，
                                                                                                                  #joint_prob = torch.sigmoid(scores) * map_mask

        sorted_times = None if model.training else get_proposal_results(joint_prob, duration)

        return loss_value, sorted_times

    def get_proposal_results(scores, durations):#得到视频片段的提议（proposal）结果
        # assume all valid scores are larger than one
        out_sorted_times = []
        for score, duration in zip(scores, durations):#对每个预测结果scores和对应持续时长
            T = score.shape[-1]#计算帧数
            sorted_indexs = np.dstack(np.unravel_index(np.argsort(score.cpu().detach().numpy().ravel())[::-1], (T, T))).tolist()#对 score 进行排序，并得到排序后的索引列表 sorted_indexs
            sorted_indexs = np.array([item for item in sorted_indexs[0] if item[0] <= item[1]]).astype(float)

            sorted_indexs[:,1] = sorted_indexs[:,1] + 1
            sorted_indexs = torch.from_numpy(sorted_indexs).cuda()
            target_size = config.DATASET.NUM_SAMPLE_CLIPS // config.DATASET.TARGET_STRIDE#//整除,size=16
            out_sorted_times.append((sorted_indexs.float() / target_size * duration).tolist())

        return out_sorted_times


    def on_test_start(state):
        state['sorted_segments_list'] = []#初始化结果
        state['output'] = []

    def on_test_forward(state):
        min_idx = min(state['sample']['batch_anno_idxs'])
        batch_indexs = [idx - min_idx for idx in state['sample']['batch_anno_idxs']]
        sorted_segments = [state['output'][i] for i in batch_indexs]
        state['sorted_segments_list'].extend(sorted_segments)

    def on_test_end(state):
#annotations（真值）存储视频编号、相应描述的开始结束时间、描述、整个视频持续时间--来自txt文件  annotations.append({'video':vid, 'times':[s_time, e_time], 'description': sent, 'duration': self.durations[vid]})
        annotations = test_dataset.annotations
#将state['sorted_segments_list']存储        
        results = {}
        for i, d in enumerate(annotations):#迭代每一组视频文本
            #data的d：annotations.append({'video':vid, 'times':[s_time, e_time], 'description': sent, 'duration': self.durations[vid]})
            results[d['video']+'_'+d['description']] = state['sorted_segments_list'][i]
            print('Most likely in '+d['video']+': '+d['description']+' is:'+str(state['sorted_segments_list'][i][0]))



    engine = Engine()
    engine.hooks['on_test_start'] = on_test_start
    engine.hooks['on_test_forward'] = on_test_forward
    engine.hooks['on_test_end'] = on_test_end
    
    #编写视频名称、文字
    video_name = 'YVKIV'
    description = 'the person puts down the bag'
    info = video_name+' 0 1##'+description+'.\n'
    # info = ['3MSZA 24.3 30.4##person turn a light on.','AMT7R 4.3 12.5##a person is putting a picture onto the wall.','YVKIV 4.4 9.2##the person puts down the bag.','GBD1Y 26.2 31.3##person closes the door.','E6DLK 9.3 14.4##person runs to the window to look out.']
    #写文件
    with open('/home/sduu2/userspace/yyr/Jason/2D-TAN-onevid/data/Charades-STA/charades_sta_test.txt', 'w') as f:
        f.write(info)
    f.close
    #下载数据集
    test_dataset = getattr(datasets, config.DATASET.NAME)('test')
    dataloader = DataLoader(test_dataset,
                            batch_size=config.TRAIN.BATCH_SIZE,
                            shuffle=False,
                            num_workers=config.WORKERS,
                            pin_memory=False,
                            collate_fn=datasets.collate_fn)
    #测试，平均耗时1s
    engine.test(network,dataloader,'test')
