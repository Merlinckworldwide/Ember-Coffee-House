import os

target_dir = r"C:\Users\Chikondi Kandodo\.gemini\antigravity\scratch\ember-coffee-house"
html_files = [
    "index.html",
    "coffee-selection.html",
    "brewing-equipment.html",
    "events-workshops.html",
    "shopping-cart.html",
    "special-offers.html"
]

# Restore logo to show BOTH image + text side by side
old_logo = '<a href="index.html" class="logo"><img src="logo/logo.png" alt="Ember Coffee House" class="logo-img"></a>'
new_logo = '<a href="index.html" class="logo"><img src="logo/logo.png" alt="Ember Coffee House Logo" class="logo-img"><span class="logo-text">Ember Coffee House</span></a>'

for f in html_files:
    fpath = os.path.join(target_dir, f)
    with open(fpath, "r", encoding="utf-8") as file:
        content = file.read()
    content = content.replace(old_logo, new_logo)
    with open(fpath, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Updated {f}")

# Update CSS
css_path = os.path.join(target_dir, "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace old logo-img rule with improved combined logo styles
old_css = """
/* Logo image */
.logo-img {
  height: 50px;
  width: auto;
  display: block;
  object-fit: contain;
  filter: brightness(0) invert(1); /* Makes logo white to stand out on dark header */
}
"""

new_css = """
/* Logo — image + text side by side */
.logo {
  display: flex !important;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}
.logo-img {
  height: 60px;
  width: auto;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);
  flex-shrink: 0;
}
.logo-text {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--color-light);
  letter-spacing: 0.5px;
  white-space: nowrap;
}
"""

css = css.replace(old_css, new_css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
    print("Updated style.css")

print("Done!")
