from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name="auth_app/login.html"), name='login'),
    path('logout/', views.user_logout, name='logout'),
]