// static/js/home_script.js
$(document).ready(function () {
  $("#button-addon1").click(function () {
    var sqlQuery = $("#sqlQueryInput").val();

    $.ajax({
      type: 'POST',
      url: '{% url "execute_sql" %}',
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




