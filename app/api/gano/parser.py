import datetime
import os

import torch


class ConfigParser(dict):
    def __init__(self, cfg):
        self._parse(cfg)
        self._set_log_path()
        self._set_device()
 
    def _parse(self, cfg):
        for k, v in cfg.items():
            self.__setattr__(k, v)

    def _set_log_path(self):
        self.log = os.path.join(
            self.log_root,
            datetime.datetime.now().strftime('%Y%m%d-%H%M%S'),
        )
        self.inter_log = os.path.join(self.log, 'intermediates')
        os.makedirs(self.inter_log)

    def _set_device(self):
        self.device = torch.device(
            'cuda:{}'.format(self.gpu_id) if torch.cuda.is_available() else 'cpu'
        )
