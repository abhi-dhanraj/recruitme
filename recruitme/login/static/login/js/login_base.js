// Get the modal
var modal = document.getElementById("id01");

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
/**************** Login signup ************** */

var loginForm = document.getElementById("login");
var signupForm = document.getElementById("signup");
var toggleButton = document.getElementById("btn");

function signup() {
  // loginForm.style.left = "-400px";
  // signupForm.style.left = "50px";
  loginForm.style.left = "-900px";
  signupForm.style.left = "100px";
  toggleButton.style.left = "125px";
}

function login() {
  // loginForm.style.left = "50px";
  // signupForm.style.left = "450px";
  loginForm.style.left = "100px";
  signupForm.style.left = "900px";
  toggleButton.style.left = "0";
}
