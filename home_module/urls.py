from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('wallpapers', views.WallpapersView.as_view(), name='wallpapers-page'),
    path('about-us', views.AboutUS.as_view(), name='about-page'),
]
