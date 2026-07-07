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

header_old = """    <div class="container header-inner">
      <a href="index.html" class="logo">Ember Coffee House</a>
      <button class="hamburger" id="hamburger">☰</button>"""

header_new = """    <div class="container header-inner">
      <a href="index.html" class="logo">Ember Coffee House</a>
      <div class="header-socials" style="display: flex; gap: 15px; align-items: center; margin-left: auto; margin-right: 20px;">
        <a href="#" style="color: var(--color-light);" title="Instagram"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
        <a href="#" style="color: var(--color-light);" title="Twitter"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
        <a href="#" style="color: var(--color-light);" title="Facebook"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
      </div>
      <button class="hamburger" id="hamburger">☰</button>"""

footer_old = """      <div class="footer-grid">
        <div>
          <h4>Ember Coffee House</h4>
          <p>123 Roaster Way<br>Coffeeville, CF 90210</p>
          <p>Email: hello@embercoffee.com</p>
        </div>
        <div>
          <h4>Quick Links</h4>
          <ul class="footer-links">
            <li><a href="coffee-selection.html">Shop Coffee</a></li>
            <li><a href="brewing-equipment.html">Equipment</a></li>
            <li><a href="events-workshops.html">Events</a></li>
          </ul>
        </div>
        <div>
          <h4>Social</h4>
          <ul class="footer-links">
            <li><a href="#">Instagram</a></li>
            <li><a href="#">Twitter</a></li>
            <li><a href="#">Facebook</a></li>
          </ul>
        </div>
      </div>"""

footer_new = """      <div class="footer-grid">
        <div>
          <h4>Ember Coffee House</h4>
          <p>Chilobwe road<br>Kandodocoffieevielle, CKF 2002</p>
          <p>Email: kandodo@embercoffee.com</p>
        </div>
        <div>
          <h4>Quick Links</h4>
          <ul class="footer-links">
            <li><a href="coffee-selection.html">Shop Coffee</a></li>
            <li><a href="brewing-equipment.html">Equipment</a></li>
            <li><a href="events-workshops.html">Events</a></li>
          </ul>
        </div>
        <div>
          <h4>Social</h4>
          <ul class="footer-links">
            <li><a href="#"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: text-bottom; margin-right: 5px;"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>Instagram</a></li>
            <li><a href="#"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: text-bottom; margin-right: 5px;"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>Twitter</a></li>
            <li><a href="#"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: text-bottom; margin-right: 5px;"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>Facebook</a></li>
          </ul>
        </div>
      </div>"""

for f in html_files:
    fpath = os.path.join(target_dir, f)
    with open(fpath, "r", encoding="utf-8") as file:
        content = file.read()
    
    content = content.replace(header_old, header_new)
    content = content.replace(footer_old, footer_new)
    
    with open(fpath, "w", encoding="utf-8") as file:
        file.write(content)

# Now, add 3 more items to brewing-equipment.html
equipment_file = os.path.join(target_dir, "brewing-equipment.html")
with open(equipment_file, "r", encoding="utf-8") as file:
    equip_content = file.read()

new_equipment = """
      <div class="card">
        <img src="https://images.unsplash.com/photo-1579624535359-8d76e4c3da1c?auto=format&fit=crop&w=600&q=80" alt="Precision Coffee Grinder" class="card-img">
        <div class="card-body">
          <h3>Precision Coffee Grinder</h3>
          <p>Flat burr grinder designed for uniform grind size and maximum flavor extraction.</p>
          <p style="font-size: 0.9rem; color: var(--color-accent); margin-bottom: 1rem;"><strong>Tip:</strong> Clean the burrs monthly for best performance.</p>
          <button class="btn add-to-cart" style="margin-top: auto;" data-id="e4" data-name="Precision Coffee Grinder" data-price="250.00" data-img="https://images.unsplash.com/photo-1579624535359-8d76e4c3da1c?auto=format&fit=crop&w=100&q=80">Add to Cart - $250.00</button>
        </div>
      </div>

      <div class="card">
        <img src="https://images.unsplash.com/photo-1620189507195-68309c04c4d0?auto=format&fit=crop&w=600&q=80" alt="Gooseneck Kettle" class="card-img">
        <div class="card-body">
          <h3>Electric Gooseneck Kettle</h3>
          <p>Precise temperature control and flow rate for the perfect pour-over experience.</p>
          <p style="font-size: 0.9rem; color: var(--color-accent); margin-bottom: 1rem;"><strong>Tip:</strong> Aim for 200°F (93°C) for light and medium roasts.</p>
          <button class="btn add-to-cart" style="margin-top: auto;" data-id="e5" data-name="Electric Gooseneck Kettle" data-price="120.00" data-img="https://images.unsplash.com/photo-1620189507195-68309c04c4d0?auto=format&fit=crop&w=100&q=80">Add to Cart - $120.00</button>
        </div>
      </div>

      <div class="card">
        <img src="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=600&q=80" alt="Aeropress" class="card-img">
        <div class="card-body">
          <h3>AeroPress Coffee Maker</h3>
          <p>Compact and durable, perfect for travel or making a quick, clean cup at home.</p>
          <p style="font-size: 0.9rem; color: var(--color-accent); margin-bottom: 1rem;"><strong>Tip:</strong> Try the inverted method for a longer steeping time.</p>
          <button class="btn add-to-cart" style="margin-top: auto;" data-id="e6" data-name="AeroPress Coffee Maker" data-price="30.00" data-img="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=100&q=80">Add to Cart - $30.00</button>
        </div>
      </div>
"""

equip_content = equip_content.replace('    </div>\n\n  </main>', new_equipment + '    </div>\n\n  </main>')

with open(equipment_file, "w", encoding="utf-8") as file:
    file.write(equip_content)

print("Done")
