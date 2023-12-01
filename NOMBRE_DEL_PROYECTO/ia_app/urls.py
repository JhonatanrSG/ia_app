# ia_app/urls.py

from django.urls import path
from .views import login_view, home, execute_sql

# ia_app/urls.py

urlpatterns = [
    path('', login_view, name='login_view'),
    path('home/', home, name='home'),
    path('execute_sql/', execute_sql, name='execute_sql'),
]


