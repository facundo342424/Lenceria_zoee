$('#editProductModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Botón que abrió el modal
    var id = button.data('id');
    var nombre = button.data('nombre');
    var marca = button.data('marca');
    var precio = button.data('precio');
    var color = button.data('color');

    // Actualiza los campos del modal
    var modal = $(this);
    modal.find('#editProductId').val(id);
    modal.find('#editProductNombre').val(nombre);
    modal.find('#editProductMarca').val(marca);
    modal.find('#editProductPrecio').val(precio);
    modal.find('#editProductColor').val(color);

    // Actualiza la acción del formulario de edición
    modal.find('#editProductForm').attr('action', '{% url "edicion" "" %}' + id);
});



