from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.lead_list, name='lead_list'),
    path('<int:pk>/', views.lead_detail, name='lead_detail'),
    path('create/', views.lead_create, name='lead_create'),
    path('<int:pk>/edit/', views.lead_edit, name='lead_edit'),
    path('<int:pk>/delete/', views.lead_delete, name='lead_delete'),
    path('<int:pk>/to_customer/', views.lead_to_customer, name='lead_to_customer'),
]
