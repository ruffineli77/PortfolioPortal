
var bodyElement = document.querySelector('body')

function toggleDarkMode() {
    var dark_setting = localStorage.getItem('isDarkMode')
    var body_element = document.body;
    var dark_light_image = document.getElementById("dark-light-image")

    body_element.classList.toggle("dark-mode");

    if (body_element.classList.contains("dark-mode")){
      localStorage.setItem('isDarkMode', true)
      dark_light_image.src="static/svg_images/moon-solid.svg"
    } else{
      localStorage.setItem('isDarkMode', false)
      dark_light_image.src="static/svg_images/sun-regular.svg"
    }
}


// Open Top Dropdown. This smells and is dripping wet but it works.

document.addEventListener('DOMContentLoaded', () => {
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
    // Get all "navbar-link" elements
    const $navbarLinks = Array.prototype.slice.call(document.querySelectorAll('.navbar-link'), 0);
    // Combine both collections into a single array
    const combinedArray = [...$navbarBurgers, ...$navbarLinks];

    // Add a click event on each of the burgers and a click event on each of the navbar-link dropdowns.
    // Loop over the combined array and add the click event
    $navbarBurgers.forEach(el => {
      el.addEventListener('click', () => {
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');
        // Toggle aria-expanded attribute
        const currentState = el.getAttribute('aria-expanded') === 'true';
        el.setAttribute('aria-expanded', String(!currentState));
      });
    });

    $navbarLinks.forEach(el => {
      el.addEventListener('click', () => {
        if (window.innerWidth < 1023) {
            const target = el.dataset.target;
            const $target = document.getElementById(target);

            el.classList.toggle('is-active');
            $target.classList.toggle('is-active');
            // // Toggle aria-expanded attribute
            const currentState = el.getAttribute('aria-expanded') === 'true';
            el.setAttribute('aria-expanded', String(!currentState));
        }
      });
    });
    $navbarLinks.forEach(el => {
      // Existing code for click event
      el.addEventListener('click', () => {
        if (window.innerWidth < 1023) {
          // ... existing code for click event
        }
      });

      // Get the corresponding dropdown for this navbar link
      const target = el.dataset.target;
      const $target = document.getElementById(target);

      // Add mouseover and mouseout events for larger screens
      if (window.innerWidth >= 1023) {
        el.addEventListener('mouseover', () => {
          el.classList.add('is-active');
          $target.classList.add('is-active');
        });

        el.addEventListener('mouseout', () => {
          el.classList.remove('is-active');
          $target.classList.remove('is-active');
        });

        // Also add mouseover and mouseout for the dropdown itself
        if ($target) {
          $target.addEventListener('mouseover', () => {
            el.classList.add('is-active');
            $target.classList.add('is-active');
          });

          $target.addEventListener('mouseout', () => {
            el.classList.remove('is-active');
            $target.classList.remove('is-active');
          });
        }
      }
    });
});
