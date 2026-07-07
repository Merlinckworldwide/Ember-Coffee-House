document.addEventListener('DOMContentLoaded', () => {

  // --- 1. Slideshow (Home Page) ---
  const slideshow = document.querySelector('.hero-slideshow');
  const slides = document.querySelectorAll('.slide');
  if (slideshow && slides.length > 0) {
    let currentSlide = 0;
    
    setInterval(() => {
      currentSlide = (currentSlide + 1) % slides.length;
      slideshow.style.transform = `translateX(-${currentSlide * 100}%)`;
    }, 5000);
  }

  // --- 2. Modal (Home Page) ---
  const modal = document.getElementById('firstVisitModal');
  if (modal) {
    const hasVisited = localStorage.getItem('ember_visited');
    if (!hasVisited) {
      setTimeout(() => {
        modal.classList.add('show');
      }, 2000);
    }

    const closeBtn = document.getElementById('closeModalBtn');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        modal.classList.remove('show');
        localStorage.setItem('ember_visited', 'true');
      });
    }

    const modalForm = document.getElementById('modalForm');
    if (modalForm) {
      modalForm.addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Thank you for signing up! Check your email for your 10% discount code.');
        modal.classList.remove('show');
        localStorage.setItem('ember_visited', 'true');
      });
    }
  }

  // --- 3. Mobile Navigation ---
  const hamburger = document.getElementById('hamburger');
  const mainNav = document.getElementById('mainNav');
  if (hamburger && mainNav) {
    hamburger.addEventListener('click', () => {
      mainNav.classList.toggle('open');
    });
  }

  // --- 4. Live Search (Coffee Selection) ---
  const searchInput = document.getElementById('coffeeSearch');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const term = e.target.value.toLowerCase();
      const items = document.querySelectorAll('.coffee-card');
      
      items.forEach(item => {
        const text = item.textContent.toLowerCase();
        if (text.includes(term)) {
          item.style.display = 'flex';
        } else {
          item.style.display = 'none';
        }
      });
    });
  }

  // --- 5 & 6 & 7. Shopping Cart Logic ---
  const addToCartBtns = document.querySelectorAll('.add-to-cart');
  addToCartBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const id = e.target.getAttribute('data-id');
      const name = e.target.getAttribute('data-name');
      const price = parseFloat(e.target.getAttribute('data-price'));
      const img = e.target.getAttribute('data-img');

      let cart = JSON.parse(localStorage.getItem('ember_cart')) || [];
      const existing = cart.find(item => item.id === id);

      if (existing) {
        existing.qty += 1;
      } else {
        cart.push({ id, name, price, img, qty: 1 });
      }

      localStorage.setItem('ember_cart', JSON.stringify(cart));
      alert(`${name} added to cart!`);
    });
  });

  const cartTbody = document.getElementById('cartTbody');
  if (cartTbody) {
    renderCart();
  }

  function renderCart() {
    let cart = JSON.parse(localStorage.getItem('ember_cart')) || [];
    cartTbody.innerHTML = '';
    
    if (cart.length === 0) {
      cartTbody.innerHTML = '<tr><td colspan="5" style="text-align:center;">Your cart is empty</td></tr>';
      document.getElementById('cartTotal').textContent = '0.00';
      return;
    }

    let total = 0;
    cart.forEach(item => {
      const subtotal = item.price * item.qty;
      total += subtotal;

      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td><img src="${item.img}" alt="${item.name}"></td>
        <td>${item.name}</td>
        <td>$${item.price.toFixed(2)}</td>
        <td>${item.qty}</td>
        <td><button class="btn remove-btn" data-id="${item.id}">Remove</button></td>
      `;
      cartTbody.appendChild(tr);
    });

    document.getElementById('cartTotal').textContent = total.toFixed(2);

    // Attach remove listeners
    document.querySelectorAll('.remove-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.target.getAttribute('data-id');
        removeFromCart(id);
      });
    });
  }

  function removeFromCart(id) {
    let cart = JSON.parse(localStorage.getItem('ember_cart')) || [];
    cart = cart.filter(item => item.id !== id);
    localStorage.setItem('ember_cart', JSON.stringify(cart));
    renderCart();
  }

  // --- 8. Event Registration Form Validation ---
  const eventForm = document.getElementById('eventForm');
  if (eventForm) {
    eventForm.addEventListener('submit', (e) => {
      // Basic validation is handled by HTML5 attributes (required, type="email"),
      // but we can intercept to show a custom message.
      e.preventDefault();
      alert('Registration successful! We will email you the details shortly.');
      eventForm.reset();
    });
  }

});
