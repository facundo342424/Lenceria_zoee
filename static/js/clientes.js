function openFormModal(url) {
    bootbox.dialog({
        title: 'Formulario',
        message: "<iframe id='formIframe' src='" + url + "' scrolling='yes' marginwidth='0' marginheight='0' frameborder='no' width='100%' height='600'></iframe>",
        size: 'large',
        buttons: {
            cancel: {
                label: 'Cerrar',
                className: 'btn-secondary',
                callback: function() {}
            },
            ok: {
                label: 'Guardar',
                className: 'btn-primary',
                callback: function() {
                    var iframe = document.getElementById('formIframe');
                    // Acceder al contenido del iframe para realizar la acción de guardar
                    var form = iframe.contentWindow.document.querySelector('form');
                    var formData = new FormData(form);

                    $.ajax({
                        url: form.action,
                        method: form.method,
                        data: new URLSearchParams(formData).toString(),
                        success: function(data) {
                            if (data.form_is_valid) {
                                bootbox.hideAll();
                                $('#clientesTable').DataTable().ajax.reload(null, false);
                            } else {
                                // Recargar el iframe si la validación falla
                                iframe.contentWindow.document.open();
                                iframe.contentWindow.document.write(data.html_form);
                                iframe.contentWindow.document.close();
                            }
                        }
                    });
                    return false;
                }
            }
        }
    });
}
