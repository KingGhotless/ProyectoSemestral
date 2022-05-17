function confirmDelete(codigo) {
  Swal.fire({
      title: '¿Estas seguro?',
      text: "No podrás deshacer la acción!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, eliminar',
      cancelButtonText: "Cancelar"
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          'Eliminado!',
          'Producto eliminado correctamente.',
          'success'
        ).then(function() {
            window.location.href = "/eliminar_producto/"+ codigo +"/";
        })
      }
    })
}