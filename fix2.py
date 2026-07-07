import os
import re

target_dir = r"C:\Users\Chikondi Kandodo\.gemini\antigravity\scratch\ember-coffee-house"

# 1. Fix CSS Colors
css_path = os.path.join(target_dir, "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

css_content = css_content.replace("--color-dark: #2A2522;", "--color-dark: #3E2723;") # Deep rich brown
css_content = css_content.replace("--color-light: #F8F5F2;", "--color-light: #FFF8E7;") # Warm cream
css_content = css_content.replace("--color-accent: #D97736;", "--color-accent: #D84315;") # Burnt orange
css_content = css_content.replace("--color-accent-hover: #BF6226;", "--color-accent-hover: #BF360C;")
css_content = css_content.replace("--color-text: #3D3530;", "--color-text: #4E342E;")

# Also fix nav alignment
css_content = css_content.replace(".main-nav ul {\n  display: flex;\n  list-style: none;\n  gap: 1.5rem;\n}", 
""".main-nav ul {
  display: flex;
  list-style: none;
  gap: 1.5rem;
  align-items: center;
}""")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)


# 2. Fix Images
html_files = [
    "index.html",
    "coffee-selection.html",
    "brewing-equipment.html",
    "events-workshops.html",
    "shopping-cart.html",
    "special-offers.html"
]

# I'll manually replace picsum images with appropriate Unsplash images based on the alt tags.
# I will parse the file, find img tags, and set the src depending on alt.

image_map = {
    "Coffee Selection": "https://images.unsplash.com/photo-1559525839-b184a4d698c7?auto=format&fit=crop&w=600&q=80",
    "Brewing Equipment": "https://images.unsplash.com/photo-1585494156145-1c60a45eba3f?auto=format&fit=crop&w=600&q=80",
    "Events": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=600&q=80",
    "Ember House Blend": "https://images.unsplash.com/photo-1559525839-b184a4d698c7?auto=format&fit=crop&w=600&q=80",
    "Ethiopia Yirgacheffe": "https://images.unsplash.com/photo-1610889556528-9a770e32642f?auto=format&fit=crop&w=600&q=80",
    "Midnight Ember": "https://images.unsplash.com/photo-1587734195503-904fca47e0e9?auto=format&fit=crop&w=600&q=80",
    "Espresso Machine": "https://images.unsplash.com/photo-1585494156145-1c60a45eba3f?auto=format&fit=crop&w=600&q=80",
    "Pour Over Kit": "https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&w=600&q=80",
    "French Press": "https://images.unsplash.com/photo-1544681280-d25a782adc9b?auto=format&fit=crop&w=600&q=80",
    "Precision Coffee Grinder": "https://images.unsplash.com/photo-1579624535359-8d76e4c3da1c?auto=format&fit=crop&w=600&q=80",
    "Gooseneck Kettle": "https://images.unsplash.com/photo-1620189507195-68309c04c4d0?auto=format&fit=crop&w=600&q=80",
    "Aeropress": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=600&q=80",
    "Coffee Tasting Evening": "https://images.unsplash.com/photo-1495474472202-8a9d1c97a552?auto=format&fit=crop&w=600&q=80",
    "Latte Art Workshop": "https://images.unsplash.com/photo-1511920170033-f8396924c348?auto=format&fit=crop&w=600&q=80",
    "Meet the Roaster": "https://images.unsplash.com/photo-1521302080334-4bebac2763a6?auto=format&fit=crop&w=600&q=80"
}

def img_replacer(match):
    src = match.group(1)
    alt = match.group(2)
    new_src = image_map.get(alt, src) # Keep old if not found
    if "picsum" in new_src and "slide" in alt.lower():
         new_src = src
    return f'img src="{new_src}" alt="{alt}"'

for f in html_files:
    fpath = os.path.join(target_dir, f)
    with open(fpath, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Replace img src based on alt
    content = re.sub(r'img src="([^"]+)" alt="([^"]+)"', img_replacer, content)
    
    # Also replace hero slideshow inline images manually
    if f == "index.html":
        content = re.sub(r'<div class="slide" style="background-image: url\(\'https://picsum\.photos/seed/2/800/600\'\);"></div>', r'<div class="slide" style="background-image: url(\'https://images.unsplash.com/photo-1495474472202-8a9d1c97a552?auto=format&fit=crop&w=1200&q=80\');"></div>', content)
        content = re.sub(r'<div class="slide" style="background-image: url\(\'https://picsum\.photos/seed/3/800/600\'\);"></div>', r'<div class="slide" style="background-image: url(\'https://images.unsplash.com/photo-1511920170033-f8396924c348?auto=format&fit=crop&w=1200&q=80\');"></div>', content)
        content = re.sub(r'<div class="slide" style="background-image: url\(\'https://picsum\.photos/seed/4/800/600\'\);"></div>', r'<div class="slide" style="background-image: url(\'https://images.unsplash.com/photo-1521302080334-4bebac2763a6?auto=format&fit=crop&w=1200&q=80\');"></div>', content)
    
    # Nav bar socials margin to auto so it pushes right
    content = content.replace('margin-left: 1rem;', 'margin-left: auto;')
    
    with open(fpath, "w", encoding="utf-8") as file:
        file.write(content)

print("Updates applied")
