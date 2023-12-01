from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('ia_app.urls')),  # Reemplaza 'ia_app' con el nombre de tu aplicación
]


