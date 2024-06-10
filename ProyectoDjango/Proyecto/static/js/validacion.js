/* Inicio de sesion */
function validacion(){
  let user = document.getElementById("username").value;
  let pass = document.getElementById("pass").value;


  if(String(user).length >= 4 && String(user).length <= 25){
    if (String(pass).length >= 8){
        document.getElementById("username").style.border = "1px solid lightgrey";
        document.getElementById("pass").style.border = "1px solid lightgrey";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-succes w-50 mx-auto text-center'>"+"Inicio correcto!</div>"

    }else{
        document.getElementById("pass").style.border = "1px solid red";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>"+"La contraseña debe contener mínimo 8 caracteres</div>"
        }
  }else{
    document.getElementById("username").style.border = "1px solid red";
    document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>El usuario debe contar con al menos 4 caracteres y un maximo de 25</div>"
  }
}
/* Formulario de registro */
document.getElementById('registro').addEventListener('submit', function(event) {
  var nombre = document.getElementById('nombre').value;
  var apellidoPaterno = document.getElementById('apellido_paterno').value;
  var apellidoMaterno = document.getElementById('apellido_materno').value;
  var rut = document.getElementById('rut').value;
  var contrasena = document.getElementById('contraseña').value;
  var direccion = document.getElementById('direccion').value;
  var email = document.getElementById('email').value;
  var genero = document.getElementById('genero').value;

  if (nombre.length > 20 || nombre.length == 0) {
      alert('El nombre no puede estar vacío y debe tener un máximo de 20 caracteres.');
      event.preventDefault();
  }

  if (apellidoPaterno.length > 20 || apellidoPaterno.length == 0) {
      alert('El apellido paterno no puede estar vacío y debe tener un máximo de 20 caracteres.');
      event.preventDefault();
  }

  if (apellidoMaterno.length > 20 || apellidoMaterno.length == 0) {
      alert('El apellido materno no puede estar vacío y debe tener un máximo de 20 caracteres.');
      event.preventDefault();
  }

  if (rut.length > 10 || rut.length == 0) {
      alert('El RUT no puede estar vacío y debe tener un máximo de 10 caracteres.');
      event.preventDefault();
  }

  if (contrasena.length < 8 || contrasena.length > 20 || !/[a-z]/.test(contrasena) || !/[0-9]/.test(contrasena)) {
      alert('La contraseña debe tener entre 8 y 20 caracteres y debe contener números y letras.');
      event.preventDefault();
  }

  if (direccion.length > 50 || direccion.length == 0) {
      alert('La dirección no puede estar vacía y debe tener un máximo de 50 caracteres.');
      event.preventDefault();
  }

  if (!/^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/.test(email)) {
      alert('Por favor, introduce un correo electrónico válido.');
      event.preventDefault();
  }

  if (genero == '') {
      alert('Por favor, selecciona un género.');
      event.preventDefault();
  }
});

  
