import os
import torch


from .deeplabv3.model.deeplabv3 import DeepLabV3

class SemanticSegmenter():
    def __init__(self, opt):
        if opt.semseg_method == 'DeepLabV3':
            self.model = self._set_deeplabv3(opt)
        else:
            raise NotImplementedError('Please prepare {} model in modules/ .'.format(opt.semseg))

    def __call__(self, img):
        # semantic segmentation
        label_map = self.model(img)
        return label_map

    def _set_deeplabv3(self, opt):
        deeplabv3_weight_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'deeplabv3/pretrained/model_13_2_2_2_epoch_580.pth',
        )
        resnet_weights_root = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'deeplabv3/pretrained/resnet',
        )

        model = DeepLabV3(opt.resnet, resnet_weights_root, opt.device)
        param = torch.load(deeplabv3_weight_path, map_location=opt.device)
        model.load_state_dict(param)
        model.eval() # (set in evaluation mode, this affects BatchNorm and dropout)

        return model