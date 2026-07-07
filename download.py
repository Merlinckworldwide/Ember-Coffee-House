import urllib.request
import os
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

target_dir = r'C:\Users\Chikondi Kandodo\.gemini\antigravity\scratch\ember-coffee-house'
images_dir = os.path.join(target_dir, 'images')
os.makedirs(images_dir, exist_ok=True)

html_files = [f for f in os.listdir(target_dir) if f.endswith('.html')]

img_urls = set()

for f in html_files:
    fpath = os.path.join(target_dir, f)
    with open(fpath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Match src="..."
    urls = re.findall(r'src="(https://images\.unsplash\.com/[^"]+)"', content)
    urls += re.findall(r'src="(https://picsum\.photos/[^"]+)"', content)
    
    # Match url('...')
    urls += re.findall(r"url\('(https://images\.unsplash\.com/[^']+)'\)", content)
    urls += re.findall(r"url\('(https://picsum\.photos/[^']+)'\)", content)
    
    # Match data-img="..."
    urls += re.findall(r'data-img="(https://images\.unsplash\.com/[^"]+)"', content)
    urls += re.findall(r'data-img="(https://picsum\.photos/[^"]+)"', content)
    
    for u in urls:
        img_urls.add(u.replace("&amp;", "&"))

print(f"Found {len(img_urls)} unique images.")

url_to_local = {}

for i, url in enumerate(img_urls):
    local_filename = f'img_{i}.jpg'
    local_path = os.path.join(images_dir, local_filename)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response, open(local_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        url_to_local[url] = f'images/{local_filename}'
        print(f"Downloaded {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Replace in all files
for f in html_files:
    fpath = os.path.join(target_dir, f)
    with open(fpath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    for url, local_rel_path in url_to_local.items():
        content = content.replace(url, local_rel_path)
        # Also handle potential HTML entity replacements
        content = content.replace(url.replace("&", "&amp;"), local_rel_path)
        
    with open(fpath, 'w', encoding='utf-8') as file:
        file.write(content)

print("HTML files updated with local images.")
