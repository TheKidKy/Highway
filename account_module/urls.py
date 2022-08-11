from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginPageView.as_view(), name='login-page'),
    path('register/', views.RegisterPageView.as_view(), name='register-page'),
    path('logout/', views.logOut, name='logout-page')
]
