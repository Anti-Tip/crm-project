from django.urls import path
from . import views

app_name = 'advertisements'

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    path('create/', views.advertisement_create, name='advertisement_create'),
    path('<int:pk>/edit/', views.advertisement_edit, name='advertisement_edit'),
    path('<int:pk>/delete/', views.advertisement_delete, name='advertisement_delete'),
]
