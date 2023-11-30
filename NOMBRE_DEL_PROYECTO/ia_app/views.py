import pyodbc
import pandas as pd
from django.db import connection
from .models import DatabaseConfiguration
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='login')  # Redirige a la página de inicio de sesión si el usuario no está autenticado
def home(request):
    return render(request, 'home.html')

def get_database_config():
    # Supongamos que solo hay una configuración de base de datos activa
    return DatabaseConfiguration.objects.first()

def execute_sql(request):
    if request.method == 'POST':
        sql_query = request.POST.get('sql_query', '')
        context = {}
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
                cursor.execute(sql_query)  # Ejecutar la consulta proporcionada por el usuario
                resultado = cursor.fetchall()
                print(resultado)

                return JsonResponse({'success': 'Consulta exitosa', 'table_data': resultado})
        except Exception as e:
            print(f"Error de conexión: {str(e)}")
            return JsonResponse({'error': f'Error de conexión: {str(e)}'})
