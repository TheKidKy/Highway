from django.shortcuts import render, redirect
from django.db.models import Count, Q
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from .forms import CommentForm
from .models import Post, PostCategory, PostComment, PostVisit
from utils.http_service import get_client_ip
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


class BlogPageView(ListView):
    model = Post
    template_name = 'blog_module/blog.html'
    context_object_name = 'posts'
    queryset = Post.objects.annotate(views=Count('postvisit')).filter(is_active=True)
    paginate_by = 3
    ordering = ['-release_date']

    def get_context_data(self, **kwargs):
        context = super(BlogPageView, self).get_context_data()
        return context

    def get_queryset(self):
        query = super(BlogPageView, self).get_queryset()
        category_name = self.kwargs.get('category')
        archives = self.kwargs.get('release_date')
        request: HttpRequest = self.request
        post_name = request.GET.get('search')

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)

        if archives is not None:
            query = query.filter(release_date__iexact=archives)

        if post_name is not None:
            query = query.filter(title__icontains=post_name)



        return query


class PostDetailView(DetailView):
    template_name = 'blog_module/single-post.html'
    model = Post

    def get_queryset(self):
        query = super(PostDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        request = self.request
        loaded_post = self.object
        user_id = None
        user_ip = get_client_ip(self.request)
        if self.request.user.is_authenticated:
            user_id = self.request.user.id

        has_been_visited = PostVisit.objects.filter(ip__iexact=user_ip, post_id=loaded_post.id).exists()

        if not has_been_visited:
            new_visit = PostVisit(ip=user_ip, user_id=user_id, post_id=loaded_post.id)
            new_visit.save()
        context['visit_count'] = PostVisit.objects.filter(post_id=loaded_post.id).count()

        post: Post = kwargs.get('object')

        context['comment_form'] = CommentForm()
        context['comments'] = PostComment.objects.filter(post_id=post.id).order_by('-create_date')
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
    return render(request, 'blog_module/components/post_categories.html', {'categories': post_categories, })


@login_required
def add_post_comment(request: HttpRequest, id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = comment_form.cleaned_data.get('text')
            new_comment = PostComment(text=text, user_id=request.user.id, post_id=id)
            new_comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def tag(request, tag):
    # This page shows all posts with the related tag
    posts = Post.objects.filter(tag=tag)
    return render(request, 'blog_module/tag.html', {'tag': tag, 'posts': posts})


# todo: building a search box to search and explore posts
def search(request):
    if request.method == 'GET':  # this will be GET now
        post_name = request.GET('search')  # do some research what it does
        status = Post.objects.filter(title__icontains=post_name)
        return render(request, "blog_module/blog.html", {"related_posts": status})
    else:
        return render(request, "blog_module/blog.html")
