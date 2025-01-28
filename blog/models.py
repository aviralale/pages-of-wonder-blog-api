from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import pre_save
from .utils import generate_unique_slug

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='categories', blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='blog/thumbnails', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    def __str__(self):
        return f"{self.title} by {self.author.username}"

@receiver(pre_save, sender=BlogPost)
def pre_save_blog_post(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(BlogPost, instance.title)

@receiver(pre_save, sender=Category)
def pre_save_category(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(Category, instance.name)