import base64
import io

from flask import jsonify
from PIL import Image

import api.gano as gano


def health():
    return jsonify({"message": "hello"}), 200


def image(inp_b64):
    print("\n---------------------------------------------")
    inp_io = io.BytesIO(base64.b64decode(inp_b64))
    inp_io.seek(0)
    inp_pil = Image.open(inp_io)
    inp_pil = inp_pil.convert("RGB")

    out_pil = gano.ganonymize(inp_pil)

    buff = io.BytesIO()
    out_pil.save(buff, format="JPEG")
    out_b64 = base64.b64encode(buff.getvalue())
    print("---------------------------------------------\n")

    return jsonify({"image": out_b64.decode()}), 200