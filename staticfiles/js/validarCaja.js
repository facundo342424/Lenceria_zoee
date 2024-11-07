$(document).ready(function() {
    $.ajax({
        url: 'administrarCajas/',  // URL de la vista que devuelve el fragmento HTML
        method: 'GET',
        dataType: 'html',
        success: function(data) {
            // Inserta el fragmento HTML en el elemento con id="caja-status"
            document.getElementById("caja-status").innerHTML = data;
        }
    });
});