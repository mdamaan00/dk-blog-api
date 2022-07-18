from distutils.command.upload import upload
from email.policy import default
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from froala_editor.fields import FroalaField
from core.settings import TIME_ZONE
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=250,default=None,unique=True)
    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self) :
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published','Published'),
    )

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'blog',default=None)
    excerpt = models.TextField(null=True)
    content  = FroalaField(theme='dark')
    slug = models.SlugField(max_length=250,unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,related_name='blog_category',null=True)
    status = models.CharField(max_length=10, choices=options,default='published')
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published',)
    
    def __str__(self) -> str:
        return self.title