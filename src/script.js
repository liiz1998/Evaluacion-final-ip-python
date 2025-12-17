document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita el envío real del formulario

    // Validar campos
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();

    if(name === "" || email === "" || message === "") {
        alert("Por favor, complete todos los campos.");
        return;
    }

    // Validar email con regex simple
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(!emailPattern.test(email)) {
        alert("Por favor, ingrese un email válido.");
        return;
    }

    // Mostrar mensaje de éxito
    document.getElementById("successMessage").textContent = "¡Formulario enviado correctamente!";
    this.reset();
});
