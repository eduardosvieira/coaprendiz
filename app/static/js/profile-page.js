var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $("btnCreateHelp").click(function(event){
    var title = $("#title").val();
    var description = $("#description").val();
  });
});
