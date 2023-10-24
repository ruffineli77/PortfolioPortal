//
// var bodyElement = document.querySelector('body')
//
// function toggleDropdown(element) {
//     const answerContainer = element.nextElementSibling;
//     answerContainer.style.display = answerContainer.style.display === 'none' ? 'block' : 'none';
// }


var activeDropdown = null; // Keep track of the currently opened dropdown

function toggleDropdown(element) {
    const answerContainer = element.nextElementSibling;

    // Hide the previously active dropdown if there is one
    if (activeDropdown && activeDropdown !== answerContainer) {
        activeDropdown.style.display = 'none';
    }

    // Toggle the clicked dropdown
    if (answerContainer.style.display === 'none' || !answerContainer.style.display) {
        answerContainer.style.display = 'block';
        activeDropdown = answerContainer;
    } else {
        answerContainer.style.display = 'none';
        activeDropdown = null;
    }
}


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

  // Add a click event on buttons to open a specific modal
  (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
    const modal = $trigger.dataset.target;
    const $target = document.getElementById(modal);

    $trigger.addEventListener('click', () => {
      openModal($target);
    });
  });

  // Add a click event on various child elements to close the parent modal
  (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
    const $target = $close.closest('.modal');

    $close.addEventListener('click', () => {
      closeModal($target);
    });
  });

  // Add a keyboard event to close all modals
  document.addEventListener('keydown', (event) => {
    if (event.code === 'Escape') {
      closeAllModals();
    }
  });
});