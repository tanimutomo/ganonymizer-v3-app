from flask import request

from api import app
from api import controllers as con
from api.gano import load_config, load_model


@app.before_first_request
def init():
    load_config()
    load_model()


@app.route("/health")
def health():
    return con.health()


@app.route("/image", methods=["POST"])
def image():
    img_b64 = request.json["image"]
    return con.image(img_b64)