

function sendData() {
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

   // $(function() {
   // $('#buttonStart').click(function() {

        $.ajax({
            url: '/receiveData',
            data:  names,
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log("SUCCESS")
            },
            error: function(error) {
                console.log(error);
                console.log("FAILURE")
            }
        });
    //});
//});

}