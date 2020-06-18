$(document).ready(function () {

    function controlWaterPump(operation) {
        console.log("Sending ajax request to control water pump, operation= %s", operation)
        $.post("/api/water-pump", { "operation": operation })
            .done(function (response) {
                document.getElementById("water-pump-status").textContent = JSON.stringify(response, undefined, 2);
            });
    }

    $("#water-pump-on").click(function (e) {
        controlWaterPump("on");
        e.preventDefault();
    });

    $("#water-pump-off").click(function (e) {
        controlWaterPump("off");
        e.preventDefault();
    });

});