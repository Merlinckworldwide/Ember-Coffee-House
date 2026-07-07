import os
import re

target_dir = r"C:\Users\Chikondi Kandodo\.gemini\antigravity\scratch\ember-coffee-house"

# 1. Update style.css
css_path = os.path.join(target_dir, "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

old_css = """.hero-slideshow {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  z-index: 1;
}

.slide {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  opacity: 0;
  transition: opacity 1s ease-in-out;
  background-size: cover;
  background-position: center;
}

.slide.active {
  opacity: 0.5; /* dark overlay effect */
}"""

new_css = """.hero-slideshow {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  z-index: 1;
  display: flex;
  transition: transform 1s ease-in-out;
}

.slide {
  flex: 0 0 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  position: relative;
}

.slide::after {
  content: "";
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0, 0, 0, 0.5);
}"""

css_content = css_content.replace(old_css, new_css)
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)


# 2. Update script.js
js_path = os.path.join(target_dir, "script.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

old_js = """  // --- 1. Slideshow (Home Page) ---
  const slides = document.querySelectorAll('.slide');
  if (slides.length > 0) {
    let currentSlide = 0;
    slides[currentSlide].classList.add('active');
    
    setInterval(() => {
      slides[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add('active');
    }, 5000);
  }"""

new_js = """  // --- 1. Slideshow (Home Page) ---
  const slideshow = document.querySelector('.hero-slideshow');
  const slides = document.querySelectorAll('.slide');
  if (slideshow && slides.length > 0) {
    let currentSlide = 0;
    
    setInterval(() => {
      currentSlide = (currentSlide + 1) % slides.length;
      slideshow.style.transform = `translateX(-${currentSlide * 100}%)`;
    }, 5000);
  }"""

js_content = js_content.replace(old_js, new_js)
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)


# 3. Update index.html
html_path = os.path.join(target_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace the hero-slideshow content
slides_html = """    <div class="hero-slideshow">
      <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1495474472202-8a9d1c97a552?auto=format&fit=crop&w=1200&q=80');"></div>
      <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1511920170033-f8396924c348?auto=format&fit=crop&w=1200&q=80');"></div>
      <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1521302080334-4bebac2763a6?auto=format&fit=crop&w=1200&q=80');"></div>
      <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1442512595331-e89e73853f31?auto=format&fit=crop&w=1200&q=80');"></div>
    </div>"""

html_content = re.sub(r'<div class="hero-slideshow">.*?</div>\s*<div class="hero-content">', slides_html + '\n    <div class="hero-content">', html_content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Slide fix applied")
