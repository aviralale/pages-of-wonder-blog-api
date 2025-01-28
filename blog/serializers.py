from rest_framework import serializers
from .models import Category, BlogPost

class CategorySerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'image', 'posts_count']
        read_only_fields = ['slug']

    def get_posts_count(self, obj):
        return obj.blogpost_set.count()

class BlogPostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    category_name = serializers.ReadOnlyField(source='category.name')
    category_slug = serializers.ReadOnlyField(source='category.slug')
    
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'content', 'created_at', 'updated_at',
            'author', 'author_username', 'category', 'category_name',
            'category_slug',
            'thumbnail', 'slug'
        ]
        read_only_fields = ['author', 'created_at', 'updated_at', 'slug', 'category_slug']