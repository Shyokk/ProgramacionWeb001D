// Función para validar el formulario
function validarFormulario() {
    // Obtener los valores de los campos del formulario
    const email = document.getElementById('inputPassword5').value.trim();
    const contrasena = document.getElementById('inputPassword5').value.trim();
    const rut = document.getElementById('inputRut').value.trim();
    const direccion = document.getElementById('inputDireccion').value.trim();

    // Validar que los campos no estén vacíos
    if (email === '' || contrasena === '' || rut === '' || direccion === '') {
        alert('Todos los campos son obligatorios');
        return;
    }

    // Validar el formato del email
    const formatoEmail = /\S+@\S+\.\S+/;
    if (!formatoEmail.test(email)) {
        alert('El email no tiene un formato válido');
        return;
    }

    // Validar que la contraseña tenga al menos 6 caracteres
    if (contrasena.length < 6) {
        alert('La contraseña debe tener al menos 6 caracteres');
        return;
    }

    // Validar que el rut tenga al menos 10 caracteres y que el penúltimo sea un guión
    if (rut.length < 10 || rut.charAt(rut.length - 2) !== '-') {
        alert('El RUT no tiene un formato válido');
        return;
    }

    // Validar que la dirección tenga al menos 10 caracteres
    if (direccion.length < 10) {
        alert('La dirección debe tener al menos 10 caracteres');
        return;
    }

    // Si se llega aquí es porque el formulario es válido, por lo que se inicia la sesión
    iniciarSesion();
}

function iniciarSesion() {
    var email = document.getElementById("inputPassword5").value;
    var contrasena = document.getElementById("inputPassword5").value;
    var rut = document.getElementById("inputRut").value;
    var direccion = document.getElementById("inputDireccion").value;

    // Validar campos
    if (validarCampos(email, contrasena, rut, direccion)) {
        // Guardar información de inicio de sesión en localStorage
        localStorage.setItem("usuario", email);
        localStorage.setItem("contrasena", contrasena);
        localStorage.setItem("rut", rut);
        localStorage.setItem("direccion", direccion);

        // Redireccionar a la página de inicio de sesión
        window.location.href = "iniciosesion.html";
    }
}

// Función para cerrar sesión
function cerrarSesion() {
    localStorage.removeItem("usuario");
    localStorage.removeItem("contrasena");
    localStorage.removeItem("rut");
    localStorage.removeItem("direccion");
    window.location.href = "index.html";
}

window.addEventListener("load", function () {
    var usuario = localStorage.getItem("usuario");
    if (usuario != null) {
        // Mostrar mensaje de sesión iniciada y botón de cerrar sesión
        var mensaje = "Sesión iniciada como " + usuario;
        document.getElementById("mensajeSesion").innerHTML = mensaje;
        document.getElementById("cerrarSesion").style.display = "block";
    }
});

