import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text, 'html.parser')

# Mendapatkan waktu sistem saat ini
scraping_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

headlines_data = []

for headline in obj.find_all('div', class_='caption'):
    h3_tag = headline.find('h3')
    category_elem = headline.find('span', class_='kanal-info')
    time_published_elem = headline.find('div', class_='date')
    
    if h3_tag and category_elem and time_published_elem:
        title = h3_tag.text
        category = category_elem.text
        time_published = time_published_elem.text.strip()
        
        headline_info = {
            "judul": title,
            "kategori": category,
            "waktu_publikasi": time_published,
            "waktu_pengambilan_data": scraping_time
        }
        
        headlines_data.append(headline_info)

# Menyimpan data dalam file JSON
with open('data.json', 'w') as json_file:
    json.dump(headlines_data, json_file, indent=4)

print("Data telah disimpan dalam file JSON.")
