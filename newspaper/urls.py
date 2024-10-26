from django.urls import path
from . import views

urlpatterns = [
    path('new/<int:klass_id>/', views.newspaper_create, name='add_newspaper'),
    path('<int:pk>/edit/', views.newspaper_edit, name='edit_newspaper'),
    path('<int:pk>/delete/', views.newspaper_delete, name='delete_newspaper'),
]
