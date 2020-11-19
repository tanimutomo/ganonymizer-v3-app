import io
import base64
import json
import os
import requests

from PIL import Image


HOST = "http://127.0.0.1:5000"
INPUT_IMAGE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "images/input.png"
)
INPUT_TXT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "images/input.txt"
)
OUTPUT_IMAGE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "images/output.png"
)

def post_img():
    inp_img = _load_img()
    res = requests.post(
        HOST + "/image",
        json.dumps({"image": inp_img}),
        headers={"Content-Type": "application/json"},
    )
    _save_img(res.json()["image"])


def _load_img() -> str:
    img_pil = Image.open(INPUT_IMAGE_PATH)
    img_pil = img_pil.convert("RGB")

    buff = io.BytesIO()
    img_pil.save(buff, format="JPEG")
    img_b64 = base64.b64encode(buff.getvalue())
    img_b64 = img_b64.decode()

    with open(INPUT_TXT_PATH, "w") as f:
        f.write(img_b64)

    return img_b64


def _save_img(img_b64):
    img_io = io.BytesIO(base64.b64decode(img_b64))
    img_io.seek(0)
    img_pil = Image.open(img_io)
    img_pil = img_pil.convert("RGB")
    img_pil.save(OUTPUT_IMAGE_PATH)


if __name__ == "__main__":
    post_img()