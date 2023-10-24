
document.addEventListener("DOMContentLoaded", function() {
    const anchor = window.location.hash;
    if (anchor) {
      const element = document.querySelector(anchor);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }
  });