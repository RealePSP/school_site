from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('detail/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('create/<int:klass_id>/', views.profile_create, name='profile_create'),
    path('edit/<int:pk>/', views.profile_edit, name='profile_edit'),
    path('delete/<int:pk>/', views.profile_delete, name='profile_delete'),
]
