from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogPageView.as_view(), name='blog-page'),
    path('', views.search, name='search'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('add-post-comment/<int:id>', views.add_post_comment, name='add-post-comment'),
    path('tag/<tag>', views.tag, name='tag'),
    path('cat/<str:category>', views.BlogPageView.as_view(), name='posts-by-cat'),
    path('date/<str:date>', views.BlogPageView.as_view(), name='posts-by-date'),
]
