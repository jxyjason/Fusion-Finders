class Engine(object):
    def __init__(self):
        self.hooks = {}

    def hook(self, name, state):

        if name in self.hooks:#如果已经加入进去了，再次hook的时候就会运行加入名称对应的方法
            self.hooks[name](state)

    def test(self, network, iterator, split):#engine.test(network,dataloader, args.split)
        state = {
            'network': network,
            'iterator': iterator,
            #dataloader： dataloader = DataLoader(test_dataset,#包含数据集，格式：annotations.append({'video':vid, 'times':[s_time, e_time], 'description': sent, 'duration': self.durations[vid]})格式给出
                            # batch_size=config.TRAIN.BATCH_SIZE,
                            # shuffle=False,
                            # num_workers=config.WORKERS,
                            # pin_memory=False,
                            # collate_fn=datasets.collate_fn)
            'split': split,
            't': 0,
            'train': False,
        }

        self.hook('on_test_start', state)#开始，初始化训练
        for sample in state['iterator']:#迭代加载一个批次的dataset中的数据，称为sample
            state['sample'] = sample
            self.hook('on_test_sample', state)#未知语句

            def closure():
                loss, output = state['network'](state['sample'])#送入网络方法network()中训练，生成output和loss
                state['output'] = output
                state['loss'] = loss
                self.hook('on_test_forward', state)
                # to free memory in save_for_backward
                state['output'] = None
                state['loss'] = None

            closure()
            state['t'] += 1
        self.hook('on_test_end', state)
        return state