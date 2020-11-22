from django.urls import path
from . import views

app_name = 'work'

urlpatterns = [
  path('funcionario/', views.employee_list, name='employee_list'),
  path('funcionario/new/', views.employee_create, name='employee_new'),
  path('funcionario/edit/<int:matr>/', views.employee_update, name='employee_edit'),
  path('funcionario/delete/<int:pk>/', views.employee_delete, name='employee_delete'),
  
  path('cliente', views.client_list, name='client_list'),
  path('cliente/new/', views.client_create, name='client_new'),
  path('cliente/edit/<int:matr>/', views.client_update, name='client_edit'),
  path('cliente/delete/<int:pk>/', views.client_delete, name='client_delete'),

  path('servico', views.service_list, name='service_list'),
  path('servico/new/', views.service_create, name='service_new'),
  path('servico/edit/<int:matr>/', views.service_update, name='service_edit'),
  path('servico/delete/<int:pk>/', views.service_delete, name='service_delete'),

  path('item', views.item_list, name='item_list'),
  path('item/new/', views.item_create, name='item_new'),
  path('item/edit/<int:matr>/', views.item_update, name='item_edit'),
  path('item/delete/<int:pk>/', views.item_delete, name='item_delete'),

  path('servico_item', views.service_item_list, name='service_item_list'),
  path('servico_item/new/', views.service_item_create, name='service_item_new'),
  path('servico_item/edit/<int:matr>/', views.service_item_update, name='service_item_edit'),
  path('servico_item/delete/<int:pk>/', views.service_item_delete, name='service_item_delete'),

  path('ordem_servico', views.service_order_list, name='service_order_list'),
  path('ordem_servico/new/', views.service_order_create, name='service_order_new'),
  path('ordem_servico/edit/<int:matr>/', views.service_order_update, name='service_order_edit'),
  path('ordem_servico/delete/<int:pk>/', views.service_order_delete, name='service_order_delete'),

  path('cliente_servico', views.client_service_list, name='client_service_list'),
  path('cliente_servico/new/', views.client_service_create, name='client_service_new'),
  path('cliente_servico/edit/<int:matr>/', views.client_service_update, name='client_service_edit'),
  path('cliente_servico/delete/<int:pk>/', views.client_service_delete, name='client_service_delete'),
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('funcionario/create', views.create_employee, name='create-employee'),
#     path('funcionario/update/<int:employee_id>', views.update_employee),
#     path('funcionario/delete/<int:employee_id>', views.delete_employee),
    
#     path('endereco/create', views.create_address, name='create-address'),
#     path('endereco/update/<int:employee_id>', views.update_address),
#     path('endereco/delete/<int:employee_id>', views.delete_address),
    
#     path('cliente/create', views.client_create, name='create-client'),
#     path('cliente/update/<int:employee_id>', views.update_client),
#     path('cliente/delete/<int:employee_id>', views.delete_client),

#     path('servico/create', views.create_service, name='create-service'),
#     path('servico/update/<int:employee_id>', views.update_service),
#     path('servico/delete/<int:employee_id>', views.delete_service),
# ]
