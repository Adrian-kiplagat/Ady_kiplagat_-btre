from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
]
