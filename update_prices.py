import os
import re

target_dir = r"C:\Users\Chikondi Kandodo\.gemini\antigravity\scratch\ember-coffee-house"
html_files = [
    "index.html",
    "coffee-selection.html",
    "brewing-equipment.html",
    "events-workshops.html",
    "shopping-cart.html",
    "special-offers.html"
]

# Price map: old USD display -> new MWK display, and data-price old -> new
price_map = {
    # Coffee
    '"18.00"': '"2500.00"',
    '"22.00"': '"3200.00"',
    '"19.50"': '"2800.00"',
    '"20.00"': '"3000.00"',
    '"24.00"': '"3500.00"',
    '"21.50"': '"3100.00"',
    '"17.00"': '"2200.00"',
    # Equipment
    '"750.00"': '"150000.00"',
    '"45.00"':  '"8500.00"',
    '"35.00"':  '"6500.00"',
    '"250.00"': '"50000.00"',
    '"120.00"': '"22000.00"',
    '"30.00"':  '"5500.00"',
}

# Button/display text map: old button text -> new
btn_map = {
    "Add to Cart - $18.00":   "Add to Cart - MWK 2,500",
    "Add to Cart - $22.00":   "Add to Cart - MWK 3,200",
    "Add to Cart - $19.50":   "Add to Cart - MWK 2,800",
    "Add to Cart - $20.00":   "Add to Cart - MWK 3,000",
    "Add to Cart - $24.00":   "Add to Cart - MWK 3,500",
    "Add to Cart - $21.50":   "Add to Cart - MWK 3,100",
    "Add to Cart - $17.00":   "Add to Cart - MWK 2,200",
    "Add to Cart - $750.00":  "Add to Cart - MWK 150,000",
    "Add to Cart - $45.00":   "Add to Cart - MWK 8,500",
    "Add to Cart - $35.00":   "Add to Cart - MWK 6,500",
    "Add to Cart - $250.00":  "Add to Cart - MWK 50,000",
    "Add to Cart - $120.00":  "Add to Cart - MWK 22,000",
    "Add to Cart - $30.00":   "Add to Cart - MWK 5,500",
}

for f in html_files:
    fpath = os.path.join(target_dir, f)
    with open(fpath, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace data-price values
    for old, new in price_map.items():
        content = content.replace(f"data-price={old}", f"data-price={new}")

    # Replace button text
    for old, new in btn_map.items():
        content = content.replace(old, new)

    # Replace any remaining $ amounts with MWK using regex
    content = re.sub(r'\$(\d+(?:\.\d{2})?)', r'MWK \1', content)

    with open(fpath, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Updated {f}")

print("All prices updated to MWK!")
