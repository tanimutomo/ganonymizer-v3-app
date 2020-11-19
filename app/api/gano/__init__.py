import os
import PIL
import time
import typing

from PIL import Image
from typing import Tuple
import yaml

from .modules.ganonymizer import GANonymizer
from .parser import ConfigParser


MAX_SIDE = 1920

cfg = None
model = None


def load_config():
    global cfg
    cfg_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "config.yml",
    )
    with open(cfg_path) as f:
        cfg = yaml.safe_load(f)
    cfg = ConfigParser(cfg)
    print("[INFO] Device: ", cfg.device)


def load_model():
    global model
    model = GANonymizer(cfg)


def ganonymize(inp_pil):
    _, out_pil = model(_resize(inp_pil))
    return out_pil


def _resize(img):
    long_side = max(img.size)
    if long_side <= MAX_SIDE:
        return img

    f = MAX_SIDE / long_side
    w, h = img.size
    return img.resize((int(w*f), int(h*f)))


