import requests
from bs4 import BeautifulSoup
from Creature import Createure


class CreaturesScraper:
    def __init__(self, creaturesURL):
        self.url = creaturesURL
        self.page = requests.get(creaturesURL)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.creatures = []


    def fetchCreatures(self):
        table = self.soup.find("tbody")
        creaturesTRS = table.findAll("tr")

        for cr in creaturesTRS:
            tds = cr.find_all("td")
            if len(tds) > 0:  # ignore headers

                name = tds[0].text.strip()
                gifurl = tds[1].find("a")['href']
                self.creatures.append(Createure(name, gifurl))
        return self.creatures
