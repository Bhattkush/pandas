AOS.init();

// Greeting message
document.addEventListener("DOMContentLoaded", function() {
  const greeting = document.createElement("p");
  const hour = new Date().getHours();
  let message = "";

  if (hour < 12) message = "Good Morning, welcome to The Space Hub!";
  else if (hour < 18) message = "Good Afternoon, enjoy your cosmic meal!";
  else message = "Good Evening, relax and dine among the stars!";

  greeting.textContent = message;
  greeting.classList.add("lead", "text-info", "mt-3");
  document.querySelector("#home .content").appendChild(greeting);
});

// Menu filter
const buttons = document.querySelectorAll('.filter-btn');
const items = document.querySelectorAll('.menu-item');

buttons.forEach(btn => {
  btn.addEventListener('click', () => {
    const category = btn.getAttribute('data-category');
    items.forEach(item => {
      if (category === 'all' || item.dataset.category === category) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  });
});
