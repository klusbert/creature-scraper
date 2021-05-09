import os

import requests
from PIL import Image


class Createure:
    def __init__(self, name, linkToGif):
        self.name = name
        self.linkToGif = linkToGif

    def save_gif(self, dir):
        if len(self.name) > 1:
            im = Image.open(requests.get(self.linkToGif, stream=True).raw)
            num_key_frames = im.n_frames
            print(dir)
            for i in range(num_key_frames):
                im.seek(im.n_frames // num_key_frames * i)
                im.save(f'{dir}{self.name}{i}.png')
        else:
            print()