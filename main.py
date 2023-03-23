from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

url = "https://howtamil.com/fruits-names-images/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Getting the table body
table_body = soup.table.tbody

fruits_imgs_src_links = []
fruits_imgs_alts_text = []

# Extracing Images src url and alt text
for table_row in table_body.contents:
    table_row_contents = table_row.contents
    table_data_contents = table_row_contents[1].contents

    img = table_data_contents[0]
    fruits_imgs_src_links.append(img["data-src"])
    fruits_imgs_alts_text.append(img["alt"])
    
# Format the text by as per my needs
for i in range(len(fruits_imgs_alts_text)):
    fruit_name = fruits_imgs_alts_text[i]
    fruits_imgs_alts_text[i] = fruit_name.capitalize().replace(" ", "_")

# Downloading all the images
for i in range(len(fruits_imgs_src_links)):
    urllib.request.urlretrieve(fruits_imgs_src_links[i], f"{fruits_imgs_alts_text[i]}.jpg")



