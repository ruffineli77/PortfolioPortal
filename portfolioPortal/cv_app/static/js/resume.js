
document.addEventListener('DOMContentLoaded', () => {
  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add('is-active');
  }

  function closeModal($el) {
    $el.classList.remove('is-active');
  }

  function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
      closeModal($modal);
    });
  }
  // Function to enable/disable scrolling
  function toggleScrolling(enableScrolling) {
    const body = document.body;
    const html = document.documentElement;

    if (enableScrolling) {
      body.style.overflow = 'auto';
      html.style.overflow = 'auto';
    } else {
      body.style.overflow = 'hidden';
      html.style.overflow = 'hidden';
    }
  }

  // Add a click event on buttons to open a specific modal
  (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
    const modal = $trigger.dataset.target;
    const $target = document.getElementById(modal);

    $trigger.addEventListener('click', () => {
      openModal($target);
      toggleScrolling(false); // Disable scrolling when a modal is opened
    });
  });

  // Add a click event on various child elements to close the parent modal
  (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
    const $target = $close.closest('.modal');

    $close.addEventListener('click', () => {
      closeModal($target);
      toggleScrolling(true); // Enable scrolling when a modal is closed
    });
  });

  // Add a keyboard event to close all modals
  document.addEventListener('keydown', (event) => {
    if (event.code === 'Escape') {
      closeAllModals();
      toggleScrolling(true); // Enable scrolling when all modals are closed
    }
  });
});