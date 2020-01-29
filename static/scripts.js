$(document).ready(function () {
    $('select').selectize({
        sortField: 'text'
    });
 
});

// call logs pagination
$(document).ready(function () {
    $('#dtBasicExample').DataTable();
    $('.dataTables_length').addClass('bs-select');
  });