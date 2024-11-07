$(document).ready(function() {  
    if (estadoCaja === 'None' || estadoCaja === undefined || !contieneDatos(estadoCaja)) {
        fnAbrirCaja()
    }
});

function contieneDatos(arr) {    
        if (arr != "[]") {
            return true; // El arreglo contiene datos
        }
    // }
    return false; // El arreglo está vacío o contiene solo objetos vacíos
}

function fnAbrirCaja(){    
        try {
            //var sUrl = "{% url 'abrirCaja' %}";
            //var sUrl = djangojs.reverse('abrirCaja'); 
            // Agregar el dominio del sitio web a la URL del iframe
            sUrl = "http://" + location.host + "/cajas/abrirCaja/";

            oVentana = bootbox.dialog(
            {
               title: "Abrir caja",
               message: "<iframe id=\"abrirCaja\" src=\"" + sUrl + "\" scrolling=\"yes\" marginwidth=\"100%\" marginheight=\"0\" frameborder=\"no\" width=\"100%\" height=\"600\"></iframe>",
               size: 'large',
               closeButton: false,
               buttons: {
                   Cancel: {
                       label: 'Cerrar',
                       className: 'btn-danger btn-sm bootbox-close-button',
                       callback: function () {
                           console.log("cerrando");
                           location.href = "http://" + location.host + "/cajas/";
                       }
                   }
               },
            //    callback: function (result) {debugger;
            //       console.log("cerrar");
            //       bootbox.hideAll();
            //   }
           });
          
            $("#dvBootbox").attr("style", "width: 100%; height: 100%;");
         }
         catch (oError) {
            bootbox.alert("<div style='text-align:left'>Ocurrió un error:<br>" + oError + "</div>");
         }
}



