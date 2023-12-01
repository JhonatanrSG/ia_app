var contenedorGrafico = document.createElement('div');
contenedorGrafico.id = 'miGrafico';
document.body.appendChild(contenedorGrafico);

// Guarda la referencia del gráfico en un ámbito más amplio
var grafico;

$(document).ready(function () {
  $("#button-addon1").click(function () {
    var sqlQuery = $("#sqlQueryInput").val();
    console.log(sqlQuery);

    // Realiza una solicitud AJAX directamente a tu endpoint de ejecución SQL en lugar de la API de OpenAI
    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:8000/app/execute_sql/',
      data: {
        'sql_query': sqlQuery,  // Utiliza la consulta SQL directamente
        'csrfmiddlewaretoken': '{{ csrf_token }}'
      },
      success: function (data) {
        $("#datos").html(crearTablaDinamica(data.data));

        // Modifica esta parte para determinar el tipo de gráfico y pasarlo como parámetro
        var tipoGrafico = determinarTipoGrafico(data.data);

        // Si el gráfico ya existe, actualiza los datos; de lo contrario, créalo
        if (grafico) {
          actualizarGrafico(grafico, data.data);
        } else {
          grafico = crearGrafico(data.data, tipoGrafico);
        }
      },
      error: function (error) {
        console.log(error);
      }
    });
  });
});

// Función para actualizar el gráfico con nuevos datos
function actualizarGrafico(grafico, nuevosDatos) {
  grafico.data.labels = Object.keys(nuevosDatos);
  grafico.data.datasets[0].data = Object.values(nuevosDatos);
  grafico.update(); // Actualiza el gráfico con los nuevos datos
}

// Función para determinar el tipo de gráfico en función de los datos
function determinarTipoGrafico(jsonObj) {
  var cantidadDatos = Object.keys(jsonObj).length;
  // Puedes personalizar esta lógica según tus necesidades
  if (cantidadDatos > 10) {
    return 'bar'; // Si hay más de 10 datos, usa un gráfico de barras
  } else {
    return 'line'; // De lo contrario, usa un gráfico de líneas
  }
}

// Función para preparar los datos para el gráfico (puedes personalizar esto según la estructura de tus datos)
function prepararDatosGrafico(jsonObj) {
  var labels = Object.keys(jsonObj);
  var data = Object.values(jsonObj);
  return {
    labels: labels,
    datasets: [{
      label: 'Datos',
      data: data,
      backgroundColor: 'rgba(75, 192, 192, 0.2)', // Puedes personalizar el color
      borderColor: 'rgba(75, 192, 192, 1)', // Puedes personalizar el color
      borderWidth: 1
    }]
  };
}


// Función para crear la tabla dinámica
function crearTablaDinamica(jsonObj) {
  var tabla = document.createElement('table');
  var thead = document.createElement('thead');
  var tbody = document.createElement('tbody');

  // Comprobamos si jsonObj tiene un valor
  if (jsonObj && typeof jsonObj === 'object') {
    // Crear el encabezado de la tabla
    var theadRow = document.createElement('tr');
    Object.keys(jsonObj).forEach(key => {
      var th = document.createElement('th');
      th.appendChild(document.createTextNode(key));
      theadRow.appendChild(th);
    });
    thead.appendChild(theadRow);

    // Crear el cuerpo de la tabla
    var tbodyRow = document.createElement('tr');
    Object.values(jsonObj).forEach(value => {
      var td = document.createElement('td');
      td.appendChild(document.createTextNode(value));
      tbodyRow.appendChild(td);
    });
    tbody.appendChild(tbodyRow);
  } else {
    // Si jsonObj no tiene un valor válido, mostramos un mensaje de error en la tabla
    var errorRow = document.createElement('tr');
    var errorCell = document.createElement('td');
    errorCell.colSpan = 2;
    errorCell.appendChild(document.createTextNode('Error: Datos no válidos'));
    errorRow.appendChild(errorCell);
    tbody.appendChild(errorRow);
  }

  // Completar y agregar la tabla
  tabla.appendChild(thead);
  tabla.appendChild(tbody);
  return tabla;
}

// Función para crear el gráfico
function crearGrafico(jsonObj, tipoGrafico) {
  // Prepara los datos para el gráfico
  var datosGrafico = prepararDatosGrafico(jsonObj);

  // Define las opciones del gráfico (puedes personalizar esto según tus necesidades)
  var opcionesGrafico = {
    responsive: true,
    maintainAspectRatio: false
  };

  // Crea el gráfico
  var ctx = document.getElementById('miGrafico').getContext('2d');
  var nuevoGrafico = new Chart(ctx, {
    type: tipoGrafico,
    data: datosGrafico,
    options: opcionesGrafico
  });

  return nuevoGrafico;
}




