from django.urls import path
from . import views

app_name = 'contracts'

urlpatterns = [
    path('', views.contract_list, name='contract_list'),
    path('<int:pk>/', views.contract_detail, name='contract_detail'),
    path('create/', views.contract_create, name='contract_create'),
    path('<int:pk>/edit/', views.contract_edit, name='contract_edit'),
    path('<int:pk>/delete/', views.contract_delete, name='contract_delete'),
]
