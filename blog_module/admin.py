from django.contrib import admin

from contact_module.models import Contact
from home_module.models import Wallpaper
from account_module.models import User
from blog_module.models import PostTag, PostVisit, PostCategory
from . import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ['title', 'author', 'release_date', 'rating']
    list_filter = ['title', 'author', 'release_date', 'rating']
    list_editable = ['author', 'release_date', 'rating']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject', 'name', 'created_date']
    list_filter = ['subject', 'name', 'created_date']

admin.site.register(models.Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Wallpaper)
admin.site.register(User)
admin.site.register(PostTag)
admin.site.register(PostVisit)
admin.site.register(PostCategory)