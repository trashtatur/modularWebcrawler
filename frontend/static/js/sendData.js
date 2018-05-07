

function sendData() {

var socket = io.connect('http://' + document.domain + ':' + location.port);
    /**
     * Table of modules
     * @type {HTMLCollectionOf<table>}
     */
    var moduleTable = document.getElementsByClassName("ModuleTable");
    var moduleArray = Array.prototype.slice.call(moduleTable);
    var table = moduleArray[0];
    var tableWidth = (table.children[0].children[0].children).length;
    var names = {};
    for (var i=0; i< tableWidth; i++) {
        var name = table.children[0].children[0].children[i].innerText;
        var searchString = document.getElementById(name).value;
        names[name]=searchString;
    }

    socket.emit('##SEND_DATA',{data : names})
}