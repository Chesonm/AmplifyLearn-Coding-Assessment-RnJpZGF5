import pandas as pd
from bs4 import BeautifulSoup
import requests
import os

url = 'https://acms.washington.edu/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
img_tags = soup.find_all('img')

home_page_path = 'acms.html'
with open(home_page_path, 'w', encoding='utf-8') as home_page_file:
    home_page_file.write(str(soup))

img_directory = 'img'
os.makedirs(img_directory, exist_ok=True)

for img_tag in img_tags:
    img_url = img_tag['src']
    if not img_url.startswith('http'):
        img_url = url + img_url

    img_name = img_tag.get('alt', 'image.jpg').replace(" ", "_")
    clean_img_name = os.path.basename(img_name.split('?')[0])

    file_path = os.path.join(img_directory, clean_img_name)

    with open(file_path, "wb") as f:
        response = requests.get(img_url)
        f.write(response.content)
