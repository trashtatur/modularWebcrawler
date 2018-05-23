function consoleIn() {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('//PRINTED_STUFF',function (data) {
        document.getElementById('scrapyConsoleOut').innerText+=data+"\n"
    })
}