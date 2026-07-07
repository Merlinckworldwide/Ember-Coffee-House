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

socials_block = """      <div class="header-socials" style="display: flex; gap: 15px; align-items: center; margin-left: auto; margin-right: 20px;">
        <a href="#" style="color: var(--color-light);" title="Instagram"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
        <a href="#" style="color: var(--color-light);" title="Twitter"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
        <a href="#" style="color: var(--color-light);" title="Facebook"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
      </div>
"""

new_socials_li = """          <li style="display: flex; gap: 15px; align-items: center; margin-left: 1rem;">
            <a href="#" style="color: var(--color-light);" title="Instagram"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
            <a href="#" style="color: var(--color-light);" title="Twitter"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
            <a href="#" style="color: var(--color-light);" title="Facebook"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
          </li>
"""

img_counter = 1

for f in html_files:
    fpath = os.path.join(target_dir, f)
    with open(fpath, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Move socials block
    content = content.replace(socials_block, "")
    content = content.replace("          <li><a href=\"shopping-cart.html\">Cart</a></li>", "          <li><a href=\"shopping-cart.html\">Cart</a></li>\n" + new_socials_li)
    
    # Fix broken images
    # Find all unsplash images
    def replacer(match):
        global img_counter
        img_counter += 1
        return f"https://picsum.photos/seed/{img_counter}/800/600"
        
    content = re.sub(r'https://images\.unsplash\.com/[^"\']+', replacer, content)
    
    with open(fpath, "w", encoding="utf-8") as file:
        file.write(content)

# Update style.css to ensure responsive images and nav
css_path = os.path.join(target_dir, "style.css")
with open(css_path, "r", encoding="utf-8") as file:
    css_content = file.read()

# Add img max-width if not present (already has it but let's be sure)
if "img {\n  max-width: 100%;" not in css_content:
    css_content = css_content.replace("a:hover {\n  color: var(--color-accent);\n}", "a:hover {\n  color: var(--color-accent);\n}\n\nimg {\n  max-width: 100%;\n  height: auto;\n}")
    
with open(css_path, "w", encoding="utf-8") as file:
    file.write(css_content)

print("Fixes applied successfully")
