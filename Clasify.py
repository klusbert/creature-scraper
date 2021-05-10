import tensorflow as tf
import numpy as np

import os
import json

model = tf.keras.models.load_model("D:\\tibia_jpg_3backgrounds.h5")
image_size = (64, 64)

file_path = 'C:\\Users\\klusb\\Documents\\tibia-creature-scraper\\creatures\\Dog\\Dog0.png'
# file_path = 'C:\\Users\\klusb\\RiderProjects\\ConsoleApp1\\SpriteDumper\\Images\\0024\\Sprites 173.jpg'

subfolders = [f.path for f in os.scandir('creatures') if f.is_dir()]


def get_images(folder):
    images = []
    for file in os.listdir(s):
        if file.endswith(".png"):
            images.append(os.path.join(s, file))
    return images


creatures = {}

for s in subfolders:
    images = get_images(s)
    image = tf.keras.preprocessing.image.load_img(images[0], color_mode='rgb', target_size=image_size)
    image_array = tf.keras.preprocessing.image.img_to_array(image, data_format='channels_last')

    image_array = tf.expand_dims(image_array, 0)  # Create batch axis
    pred = np.argmax(model.predict(image_array))
    creature_name = s.replace('creatures\\', "")



    pred = np.int(pred)

    if pred not in creatures:
        creatures[pred] = []
        # append some value
    creatures[pred].append(creature_name)

print(creatures)

with open('data.json', 'w') as fp:
    json.dump(creatures, fp)
