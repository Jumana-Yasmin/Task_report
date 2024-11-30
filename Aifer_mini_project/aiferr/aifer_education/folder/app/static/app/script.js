document.addEventListener("DOMContentLoaded", function() {
    alert("JavaScript file is loaded successfully!");
});

document.addEventListener('DOMContentLoaded', function() {
    // Form Validation on Student Registration
    const registrationForm = document.getElementById('form');
    if (registrationForm) {
        registrationForm.addEventListener('submit', function(event) {
            const username = document.getElementById('id_username');
            const password = document.getElementById('id_password');
            const passwordConfirm = document.getElementById('id_password_confirm');
            
            if (!username.value || !password.value || password.value !== passwordConfirm.value) {
                event.preventDefault();
                alert('Please fill out all fields correctly.');
            }
        });
    }

    // Form Validation on Student Login
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            const username = document.getElementById('id_name');
            const password = document.getElementById('id_password');
            
            if (!username.value || !password.value) {
                event.preventDefault();
                alert('Please enter both username and password.');
            }
        });
    }
    
    // Button hover effects (optional)
    const submitButton = document.getElementById('submit');
    if (submitButton) {
        submitButton.addEventListener('mouseover', function() {
            submitButton.style.backgroundColor = '#0056b3';
        });

        submitButton.addEventListener('mouseout', function() {
            submitButton.style.backgroundColor = '#007bff';
        });
    }

    const loginButton = document.getElementById('login-btn');
    if (loginButton) {
        loginButton.addEventListener('mouseover', function() {
            loginButton.style.backgroundColor = '#0056b3';
        });

        loginButton.addEventListener('mouseout', function() {
            loginButton.style.backgroundColor = '#007bff';
        });
    }
});
