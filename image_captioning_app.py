from flask import Flask, abort, request
from im2txt import run_caption
import json

app = Flask(__name__)

@app.route('/', methods=["POST"])
def hello_world():
  if not request.data:
    return json.dumps({"image_caption": "nothing to see here."})

  model_output = run_caption(request.data)
  return json.dumps({"image_caption": model_output})

if __name__ == '__main__':
  app.run()
