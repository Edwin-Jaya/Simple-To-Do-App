from .views import index_view, dashboard_view, create_form, update_form, delete_form
from django.urls import path


APP_NAME = 'todolist'

urlpatterns = [
    path('', index_view, name='index'),
    path('dashboard', dashboard_view, name='dashboard'),
    path('create', create_form, name='create'),
    path('update/<int:pk>', update_form, name='update'),
    path('delete/<int:pk>', delete_form, name='delete')
]