document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('passwordForm').addEventListener('submit', function (event) {
        event.preventDefault();
        checkStrength();
    });
});

function checkStrength() {
    var password = document.getElementById('password').value;

    // Client-side validation
    if (password.length < 8) {
        alert('Password must be at least 8 characters long.');
        return;
    }

    // Send password to server for strength checking
    fetch('/check_strength', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ password: password }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('strengthResult').innerText = "Password Strength: " + data.strength;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
