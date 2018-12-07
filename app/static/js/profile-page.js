var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $("#btnCreateHelp").click(function(event){
    $.ajax({
      url: URL + "/coaprendiz/skills/",
      type: "GET",
      success: function(data) {
        var skills = $("#skills");
        skills.empty();

        for(index in data) {
          skills.append($("<option />").text(data[index]["name"]).attr("value", data[index]["_id"]));
        }
      },
      error: function() {
        console.log("ERROR");
      }
    })
  });
});
