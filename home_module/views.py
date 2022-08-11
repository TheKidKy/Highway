from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . import models

# Create your views here.

class HomePageView(ListView):
    template_name = 'home_module/index.html'
    model = models.Wallpaper
    context_object_name = 'wallpapers'
    paginate_by = 3


class WallpapersView(ListView):
    template_name = 'home_module/wallpapers.html'
    model = models.Wallpaper
    context_object_name = 'wallpapers'
    paginate_by = 12

# rendering header and footer using django render partial which is more dynamic than "include" tag.
def header_component(request):
    return render(request, 'shared/components/header_component.html')

def footer_component(request):
    return render(request, 'shared/components/footer_component.html')

def menu_component(request):
    return render(request, 'shared/components/menu_component.html')

class AboutUS(TemplateView):
    template_name = 'home_module/about.html'
