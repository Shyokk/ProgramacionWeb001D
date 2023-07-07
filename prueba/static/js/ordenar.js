$(document).ready(function(){
    $("#busqueda").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#productos tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });