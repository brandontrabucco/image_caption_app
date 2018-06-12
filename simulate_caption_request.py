import requests as rq
import tensorflow as tf
import json

class HandleRequest(object):
    
    def __init__(self, image_uri):
        with tf.gfile.GFile(
                image_uri, "rb") as f:
            self.r = rq.post(
                "http://ec2-18-218-42-22.us-east-2.compute.amazonaws.com", 
                data=f.read())
        
    def caption(self):
        if self.r.status_code == 200:
            return self.r.json()["image_caption"]
        else:
            return [[""]]
