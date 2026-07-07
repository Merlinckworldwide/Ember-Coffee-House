import os
import re
import urllib.request

target_dir = r"C:\Users\Chikondi Kandodo\.gemini\antigravity\scratch\ember-coffee-house"
html_file = os.path.join(target_dir, "coffee-selection.html")
images_dir = os.path.join(target_dir, "images")

def download_img(url, local_path):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req).read()
    with open(local_path, 'wb') as f:
        f.write(data)

# Download 4 new coffee images
new_coffees = [
    {
        "id": "c4",
        "name": "Guatemala Antigua",
        "origin": "Guatemala (Single Origin)",
        "notes": "Toffee, Almond, Mild Spice",
        "best": "Drip, Chemex",
        "price": "20.00",
        "img_url": "https://loremflickr.com/600/400/coffee,beans,guatemala/all",
        "img_file": "coffee_guatemala.jpg",
        "alt": "Guatemala Antigua"
    },
    {
        "id": "c5",
        "name": "Kenya AA Peaberry",
        "origin": "Kenya (Single Origin)",
        "notes": "Blackcurrant, Grapefruit, Wine",
        "best": "Pour-over, Aeropress",
        "price": "24.00",
        "img_url": "https://loremflickr.com/600/400/coffee,espresso,dark/all",
        "img_file": "coffee_kenya.jpg",
        "alt": "Kenya AA Peaberry"
    },
    {
        "id": "c6",
        "name": "Costa Rica Honey",
        "origin": "Costa Rica (Single Origin)",
        "notes": "Peach, Honey, Milk Chocolate",
        "best": "V60, French Press",
        "price": "21.50",
        "img_url": "https://loremflickr.com/600/400/coffee,cup,hot/all",
        "img_file": "coffee_costarica.jpg",
        "alt": "Costa Rica Honey"
    },
    {
        "id": "c7",
        "name": "Ember Decaf Blend",
        "origin": "Mexico & Peru",
        "notes": "Caramel, Walnut, Smooth Finish",
        "best": "Espresso, Drip",
        "price": "17.00",
        "img_url": "https://loremflickr.com/600/400/coffee,latte,mug/all",
        "img_file": "coffee_decaf.jpg",
        "alt": "Ember Decaf Blend"
    }
]

for c in new_coffees:
    local_path = os.path.join(images_dir, c["img_file"])
    print(f"Downloading {c['name']}...")
    download_img(c["img_url"], local_path)
    print(f"  -> saved to images/{c['img_file']}")

# Build new cards HTML
new_cards_html = ""
for c in new_coffees:
    new_cards_html += f"""
      <div class="card coffee-card">
        <img src="images/{c['img_file']}" alt="{c['alt']}" class="card-img">
        <div class="card-body">
          <h3>{c['name']}</h3>
          <p><strong>Origin:</strong> {c['origin']}</p>
          <p><strong>Notes:</strong> {c['notes']}</p>
          <p><strong>Best for:</strong> {c['best']}</p>
          <button class="btn add-to-cart" style="margin-top: auto;" data-id="{c['id']}" data-name="{c['name']}" data-price="{c['price']}" data-img="images/{c['img_file']}">Add to Cart - ${c['price']}</button>
        </div>
      </div>
"""

content = open(html_file, encoding='utf-8').read()

# Insert new cards before closing </div> of the coffeeGrid
content = content.replace(
    '    </div>\n\n    <!-- Plugins -->',
    new_cards_html + '    </div>\n\n    <!-- Plugins -->'
)

open(html_file, 'w', encoding='utf-8').write(content)
print("Done — 4 new coffees added to coffee-selection.html")
