import urllib.request
from bs4 import BeautifulSoup
import pandas as pd


page = urllib.request.urlopen("https://www.molsoncoors.com/brands/our-brands")

soup = BeautifulSoup(page, 'html.parser')

beer_soups = soup.findAll("div", {"class": "beer-target"})

new_entry = []

full_list = []

for beer in beer_soups :
    new_entry.append(beer['data-target'])

    new_entry.append(beer['aria-label'])

    full_list.append(new_entry)

    new_entry = []


df = pd.DataFrame(full_list, columns=["Label","Data Targets"])

df.to_csv('brands.csv')
