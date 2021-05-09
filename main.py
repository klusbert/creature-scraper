import os

import requests
from PIL import Image

from CreaturesScraper import CreaturesScraper


def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def load_creatures():
    creatures = creaturesScraper.fetchCreatures()

    create_dir("creatures")
    count = len(creatures) * 1.0
    i = 0.0
    for c in creatures:
        create_dir(f"creatures\\{c.name}")
        c.save_gif(f"creatures\\{c.name}\\")

        i = i + 1
        print(f"loading:{i / count * 100} %")


if __name__ == '__main__':
    creaturesScraper = CreaturesScraper("https://tibia.fandom.com/wiki/List_of_Creatures")
    load_creatures()


