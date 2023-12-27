from torch import nn
from core.config import config
import models.frame_modules as frame_modules
import models.prop_modules as prop_modules
import models.map_modules as map_modules
import models.fusion_modules as fusion_modules

class TAN(nn.Module):
    def __init__(self):
        super(TAN, self).__init__()

        self.frame_layer = getattr(frame_modules, config.TAN.FRAME_MODULE.NAME)(config.TAN.FRAME_MODULE.PARAMS)#用于获取模块对象中的某个属性或方法：对象FrameAvgPool.__init__（config.TAN.FRAME_MODULE.PARAMS）
        self.prop_layer = getattr(prop_modules, config.TAN.PROP_MODULE.NAME)(config.TAN.PROP_MODULE.PARAMS)#SparsePropMaxPool
        self.fusion_layer = getattr(fusion_modules, config.TAN.FUSION_MODULE.NAME)(config.TAN.FUSION_MODULE.PARAMS)#BaseFusion
        self.map_layer = getattr(map_modules, config.TAN.MAP_MODULE.NAME)(config.TAN.MAP_MODULE.PARAMS)#MapConv
        self.pred_layer = nn.Conv2d(config.TAN.PRED_INPUT_SIZE, 1, 1, 1)#512

    def forward(self, textual_input, textual_mask, visual_input):

        vis_h = self.frame_layer(visual_input.transpose(1, 2))#提取视觉特征
        map_h, map_mask = self.prop_layer(vis_h)#地图特征和地图掩码，
        #地图特征map_h是一个二维热图，用于表示视觉输入中哪些区域与文本输入相关。
        #地图掩码map_mask是一个二进制掩码，用于指示哪些位置应该被用于计算损失函数，哪些位置应该被忽略。
        fused_h = self.fusion_layer(textual_input, textual_mask, map_h, map_mask)#文本-视觉特征融合
        fused_h = self.map_layer(fused_h, map_mask)#地图特征修正
        prediction = self.pred_layer(fused_h) * map_mask#卷积预测，同时过滤掉地图掩码不匹配的部分

        return prediction, map_mask

    def extract_features(self, textual_input, textual_mask, visual_input):
        vis_h = self.frame_layer(visual_input.transpose(1, 2))
        map_h, map_mask = self.prop_layer(vis_h)

        fused_h = self.fusion_layer(textual_input, textual_mask, map_h, map_mask)
        fused_h = self.map_layer(fused_h, map_mask)
        prediction = self.pred_layer(fused_h) * map_mask

        return fused_h, prediction, map_mask
