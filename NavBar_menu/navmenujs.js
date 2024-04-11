function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
  
    if (username === "usuario" && password === "contraseña") {
      alert("¡Inicio de sesión exitoso!");
      return true;
    } else {
      alert("Nombre de usuario o contraseña incorrectos.");
      return false;
    }
  }
  