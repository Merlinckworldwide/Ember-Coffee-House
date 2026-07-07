import os
import re
import urllib.request

target_dir = r"C:\Users\Chikondi Kandodo\.gemini\antigravity\scratch\ember-coffee-house"
html_file = os.path.join(target_dir, "brewing-equipment.html")

content = open(html_file, encoding='utf-8').read()

def download_img(url, local_path):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req).read()
    with open(local_path, 'wb') as f:
        f.write(data)

# 1. Grinder
g_url = 'https://loremflickr.com/600/400/coffee,grinder/all'
g_path = os.path.join(target_dir, 'images', 'real_grinder.jpg')
download_img(g_url, g_path)
content = re.sub(r'img src="[^"]+" alt="Precision Coffee Grinder"', r'img src="images/real_grinder.jpg" alt="Precision Coffee Grinder"', content)

# 2. Kettle
k_url = 'https://loremflickr.com/600/400/coffee,kettle/all'
k_path = os.path.join(target_dir, 'images', 'real_kettle.jpg')
download_img(k_url, k_path)
content = re.sub(r'img src="[^"]+" alt="Gooseneck Kettle"', r'img src="images/real_kettle.jpg" alt="Gooseneck Kettle"', content)

# 3. Aeropress
a_url = 'https://loremflickr.com/600/400/aeropress,coffee/all'
a_path = os.path.join(target_dir, 'images', 'real_aeropress.jpg')
download_img(a_url, a_path)
content = re.sub(r'img src="[^"]+" alt="Aeropress"', r'img src="images/real_aeropress.jpg" alt="Aeropress"', content)

open(html_file, 'w', encoding='utf-8').write(content)
print("Equipment images fixed via LoremFlickr")
