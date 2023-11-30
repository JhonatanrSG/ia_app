// static/js/home_script.js
$(document).ready(function () {
  $("#button-addon1").click(function () {
    // Obtén el valor del input de consulta
    var sqlQuery = $("#sqlQueryInput").val();

    // Realiza una solicitud AJAX para ejecutar la consulta
    $.ajax({
      type: 'POST',
      url: '{% url "execute_sql" %}',  // Utiliza la función {% url %}
      data: {
        'sql_query': sqlQuery,
        'csrfmiddlewaretoken': '{{ csrf_token }}'
      },
      success: function (data) {
        console.log(data);
      },
      error: function (error) {
        console.log(error);
      }
    });
  });
});



