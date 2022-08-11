from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.urls import reverse
from account_module.models import User

# Create your models here.

def validate_rating(value):
    # a function for validating the rating : between 0 and 5.
    if value > 5 or value < 0:
        raise ValidationError(
            ('rating must be between 0 to 5'),
            params={'value': value},
        )

class PostCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='title')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='url title')
    is_active = models.BooleanField(verbose_name='active')
    is_delete = models.BooleanField()

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class PostTag(models.Model):
    title = models.CharField(max_length=20, db_index=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    category = models.ManyToManyField(PostCategory, related_name='post_categories', verbose_name='categories')
    tag = models.ManyToManyField(PostTag, verbose_name='Post tags')
    release_date = models.DateField(null=True)
    author = models.CharField(max_length=30)
    rating = models.IntegerField(validators=[validate_rating])
    is_active = models.BooleanField(default=False, verbose_name='Active')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, editable=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # This function reverses the urls.
        return reverse('post-detail', args=[self.slug])

    def save(self, *args, **kwargs): # Save function is used to save the arguments in the database.
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta: # Meta class is used to change the module verbose name.
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class PostVisit(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Post')
    ip = models.CharField(max_length=30, verbose_name='User IP')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} / {self.ip}'

    class Meta:
        verbose_name = 'Post visit'
        verbose_name_plural = 'Post visits'
