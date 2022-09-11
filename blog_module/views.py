from django.shortcuts import render
from django.db.models import Count
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Post, PostCategory, PostComment, PostVisit
from utils.http_service import get_client_ip
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

# Create your views here.


class BlogPageView(ListView):
    model = Post
    template_name = 'blog_module/blog.html'
    context_object_name = 'posts'
    paginate_by = 3
    ordering = ['-release_date']

    def get_context_data(self, **kwargs):
        context = super(BlogPageView, self).get_context_data(**kwargs)
        post = self.kwargs.get('object')
        context['visit_count'] = PostVisit.objects.filter(post=post).count()
        return context

    def get_queryset(self):
        query = super(BlogPageView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query

        
class PostDetailView(DetailView):
    template_name = 'blog_module/single-post.html'
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_post = self.object
        user_ip = get_client_ip(self.request)
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        has_been_visited = PostVisit.objects.filter(ip__iexact=user_ip, post_id=loaded_post.id).exists()
        if not has_been_visited:
            new_visit = PostVisit(ip=user_ip, user_id=user_id, post_id=loaded_post.id)
            new_visit.save()
        context['visit_count'] = PostVisit.objects.filter(post_id=loaded_post.id).count()

        post: Post = kwargs.get('object')
        context['comments'] = PostComment.objects.filter(id=post.id)
        context['comments_count'] = PostComment.objects.filter(id=post.id).count()

        return context


# ---- COMPONENTS ----
def posts_archive_component(request):
    posts = Post.objects.filter(release_date='2022-07-13')
    return render(request, 'blog_module/components/posts_archive_component.html', {'posts': posts})


# Filtering the three latest posts.
def recent_posts_component(request):
    posts = Post.objects.filter(is_active=True).order_by('-release_date')[0:3]
    return render(request, 'blog_module/components/recent_posts_component.html', {'posts': posts})


def post_categories_component(request):
    post_categories = PostCategory.objects.annotate(posts_count=Count('post')).filter(is_active=True)
    return render(request, 'blog_module/components/post_categories.html', {'categories': post_categories,})


@login_required
def post_comments(request: HttpRequest):
    post = Post.objects.all()
    context = {
        'comments': PostComment.objects.filter(id=post.id)
    }
    return render(request, 'blog_module/includes/post_comments_partial.html', context)


def tag(request, tag):
    # This page shows all posts with the related tag
     posts = Post.objects.filter(tag=tag)
     return render(request, 'blog/tag.html', {'tag': tag, 'posts': posts})


# todo: building a search box to search and explore posts
def search(request):        
    if request.method == 'GET': # this will be GET now      
        post_name = request.GET('search') # do some research what it does
        status = Post.objects.filter(title__icontains=post_name)
        return render(request, "blog_module/blog.html", {"related_posts":status})
    else:
        return render(request, "blog_module/blog.html")
