from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('funcionario/create', views.create_employee, name='create-employee'),
    path('funcionario/update/<int:employee_id>', views.update_employee),
    path('funcionario/delete/<int:employee_id>', views.delete_employee),
    
    path('endereco/create', views.create_address, name='create-address'),
    path('endereco/update/<int:employee_id>', views.update_address),
    path('endereco/delete/<int:employee_id>', views.delete_address),
    
    path('cliente/create', views.create_client, name='create-client'),
    path('cliente/update/<int:employee_id>', views.update_client),
    path('cliente/delete/<int:employee_id>', views.delete_client),

    path('servico/create', views.create_service, name='create-service'),
    path('servico/update/<int:employee_id>', views.update_service),
    path('servico/delete/<int:employee_id>', views.delete_service),
]
