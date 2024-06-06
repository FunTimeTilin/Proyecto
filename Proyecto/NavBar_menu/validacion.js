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

document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('rol').value;
    const usernameError = document.getElementById('usernameError');
    const passwordError = document.getElementById('passwordError');
    const roleError = document.getElementById('rolError');
    usernameError.textContent = '';
    passwordError.textContent = '';
    roleError.textContent = '';

    let isValid = true;
    if (username.length < 4 || username.length > 20) {
        usernameError.textContent = 'El nombre de usuario debe tener entre 4 y 20 caracteres.';
        isValid = false;
    }
    if (password.length < 8) {
        passwordError.textContent = 'La contraseña debe tener al menos 8 caracteres.';
        isValid = false;
    }
    if (role === '') {
        roleError.textContent = 'Por favor, seleccione un rol.';
        isValid = false;
    }
    if (isValid) {
        alert('Formulario enviado correctamente.');
    }
});
