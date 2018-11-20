var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $("#btnReset").click(function(event) {
    var email = $("#email").val();

    $.ajax({
      url: URL + "/abtms/auth/reset/",
      type: "POST",
      data: {"email": email},
      success: function(data) {
        console.log("Entrar realizado com sucesso.");
        window.location.replace("/abtms/login/");
      },
      error: function(data) {
        console.log("Houve um problema ao entrar na aplicação.");
        window.location.replace("/abtms/auth/reset/");
      }
    });
  });
});
