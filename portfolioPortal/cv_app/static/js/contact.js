
document.addEventListener('DOMContentLoaded', function() {
    var emailInput = document.querySelector('input[type="email"]');
    var emailError = document.querySelector(".help");

    emailInput.addEventListener('input', function() {
        var emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        if (!emailPattern.test(emailInput.value)) {
            emailInput.classList.add('is-danger');
            emailError.classList.add('is-danger');
            // Show validation message
        } else {
            emailInput.classList.remove('is-danger');
            emailError.classList.remove('is-danger');
            // Hide validation message
        }
    });
});
