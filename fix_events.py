import os
import re
import urllib.request

target_dir = r"C:\Users\Chikondi Kandodo\.gemini\antigravity\scratch\ember-coffee-house"
html_file = os.path.join(target_dir, "events-workshops.html")

content = open(html_file, encoding='utf-8').read()

def download_img(url, local_path):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req).read()
    with open(local_path, 'wb') as f:
        f.write(data)

# 1. Tasting
t_url = 'https://loremflickr.com/600/400/coffee,tasting/all'
t_path = os.path.join(target_dir, 'images', 'real_tasting.jpg')
download_img(t_url, t_path)
content = re.sub(r'img src="[^"]+" alt="Coffee Tasting Evening"', r'img src="images/real_tasting.jpg" alt="Coffee Tasting Evening"', content)

# 2. Latte Art
l_url = 'https://loremflickr.com/600/400/latte,art/all'
l_path = os.path.join(target_dir, 'images', 'real_latte_art.jpg')
download_img(l_url, l_path)
content = re.sub(r'img src="[^"]+" alt="Latte Art Workshop"', r'img src="images/real_latte_art.jpg" alt="Latte Art Workshop"', content)

# 3. Roaster
r_url = 'https://loremflickr.com/600/400/coffee,roaster/all'
r_path = os.path.join(target_dir, 'images', 'real_roaster.jpg')
download_img(r_url, r_path)
content = re.sub(r'img src="[^"]+" alt="Meet the Roaster"', r'img src="images/real_roaster.jpg" alt="Meet the Roaster"', content)

open(html_file, 'w', encoding='utf-8').write(content)
print("Events images fixed via LoremFlickr")
