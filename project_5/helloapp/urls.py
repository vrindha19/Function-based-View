from django.urls import path
from .views import login_view

urlpatterns = [
    path('login_view/', login_view, name='login_view'),
]
