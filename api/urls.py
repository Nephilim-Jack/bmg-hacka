from django.urls import path
from . import views

urlpatterns = [
    path('get_user/<int:user_id>', views.get_user),
    path('get_groups', views.get_groups)
]