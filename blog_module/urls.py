from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogPageView.as_view(), name='blog-page'),
    path('', views.search, name='search'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('tag/<tag>', views.tag, name='tag'),
]