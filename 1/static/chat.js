$(document).ready(function () {
  // Automatically scroll to the bottom of the chatbox
  $("#chatbox").scrollTop($("#chatbox")[0].scrollHeight);

  $("#userInput").keypress(function (event) {
    if (event.which == 13) {
      var userInput = $("#userInput").val();
      $.ajax({
        url: "/send_message",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({ message: userInput }),
        success: function (response) {
          if (response.clear_chat) {
            $("#chatbox").html("");  // Clear the chatbox
            response.initial_conversation.forEach(function (line) {
              $("#chatbox").append("<p>" + line + "</p>");
            });
          } else {
            $("#chatbox").append("<p>" + response.response.replace(/\n/g, "<br>") + "</p>");
          }
          $("#userInput").val("");
          $("#chatbox").scrollTop($("#chatbox")[0].scrollHeight);
        }
      });
    }
  });
});
