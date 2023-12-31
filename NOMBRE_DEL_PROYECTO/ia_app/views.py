from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import pyodbc
from django.http import JsonResponse
from .models import DatabaseConfiguration
import requests

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin:index')  # Usuario de administración
            else:
                return redirect('home')  # Otra página principal para usuarios normales

    return render(request, 'loginHT.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def get_database_config():
    # Supongamos que solo hay una configuración de base de datos activa
    return DatabaseConfiguration.objects.first()



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin:index')  # Usuario de administración
            else:
                return redirect('home')  # Otra página principal para usuarios normales

    return render(request, 'loginHT.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def get_database_config():
    # Supongamos que solo hay una configuración de base de datos activa
    return DatabaseConfiguration.objects.first()



def execute_sql(request):
    if request.method == 'POST':
        sql_query1 = request.POST.get('sql_query1[data]', '')
        print(request.POST)
        type(print(sql_query1))
        db_config = get_database_config()

        try:
            with pyodbc.connect(f"Driver={db_config.odbc_driver};"
                                f"Server={db_config.server};"
                                f"Database={db_config.database};"
                                f"Trusted_Connection={'yes' if db_config.trusted_connection else 'no'};"
                                f"LoginTimeout={db_config.login_timeout};"
                                f"encrypt={'yes' if db_config.encrypt else 'no'};"
                                ) as conexion:
                print("Conexión a la base de datos exitosa.")
                cursor = conexion.cursor()

                # Agrega este print para registrar la consulta SQL antes de ejecutarla
                print("Consulta SQL a ejecutar:", sql_query1)

                # Validar que la consulta SQL no esté vacía antes de ejecutarla
                if sql_query1:
                    print(sql_query1)
                    # Ejecutar la consulta SQL
                    cursor.execute(sql_query1)
                    columnas = [col[0] for col in cursor.description]
                    data = [dict(zip(columnas, row)) for row in cursor.fetchall()]
                    print(data)
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'error': 'La consulta SQL está vacía.'})

        except Exception as e:
            print(f"Error de conexión: {str(e)}")
            return JsonResponse({'error': f'Error de conexión: {str(e)}'})
