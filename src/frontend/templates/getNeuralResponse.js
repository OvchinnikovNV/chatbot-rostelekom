function getNeuralResponse() {
    let rawText = $("#textInput").val();
    let userHtml = '<p class="userField"><span class="userText">' + rawText + '</span></p>';
    $("#textInput").val("");
    $("#chat_field").append(userHtml);
    document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
    $.get("/get", { msg: rawText }).done(function(data) {
        let botHtml = '<p class="botField"><span class="botText">' + data + '</span></p>';
        $("#chat_field").append(botHtml);
        document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
    });
}
$("#textInput").keypress(function(e) {
    if ((e.which == 13) && document.getElementById("textInput").value != "" ){
        getNeuralResponse();
    }
});
$("#buttonInput").click(function() {
    if (document.getElementById("textInput").value != "") {
        getNeuralResponse();
    }
})