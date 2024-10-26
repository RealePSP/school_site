from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list, name='class_list'),
    path('<int:pk>/', views.class_detail, name='class_detail'),
    path('<int:pk>/students/', views.class_students, name='class_students'),
]
