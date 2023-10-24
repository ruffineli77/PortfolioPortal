
// document.addEventListener("DOMContentLoaded", function() {
//   setTimeout(function() {
//     const element = document.getElementById("flashMessage");
//     element.style.opacity = "0";
//     element.addEventListener("transitionend", function() {
//       element.style.display = "none";
//     }, false);
//   }, 5000);  // 5 seconds after the page load
// });


// Assuming a function `showFlashMessage()` will be triggered when the form is submitted successfully
function showFlashMessage() {
  const element = document.getElementById("flashMessage");
  element.className += " fade-in";  // Add fade-in class to make it visible and interactable

  // Remove it after 5 seconds
  setTimeout(function() {
    element.className = element.className.replace(" fade-in", ""); // Remove fade-in class
    element.className += " fade-out";  // Add fade-out class to start the fade-out

    element.addEventListener("transitionend", function() {
      element.className = element.className.replace(" fade-out", "");  // Remove fade-out class
    }, false);
  }, 5000);  // 5 seconds after it appears
}
