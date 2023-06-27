from django.contrib.auth.models import User, Group
from rest_framework import serializers

from newspaper1_app.models import Tag, Category, Post, Comment, Newsletter

# convert from json string to dictionary object and vice-versa
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'groups', 'last_login', 'date_joined',]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
        
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
        
class PostSerializer(serializers.ModelSerializer):
    
    # yo chai yo vitra chaine but navako kura i.e. custom kura
    comments = serializers.SerializerMethodField()
    
    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj).values()
        return comments
    
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'featured_image',
            'views_count',
            'status',
            'published_at',
            'category',
            'tag',
            'author',
            'comments',
            ]
        
        # yo chai api bata halna namilne kura haru
        extra_kwargs = {
            "published_at": {"read_only": True},
            "author": {"read_only": True},
            "views_count": {"read_only": True},
            
        }
       
    # yo login user lai nai author user banako 
    def validate(self, data):
        data["author"] = self.context["request"].user
        return data
    
    
class PostPublishSerializer(serializers.Serializer):
    post = serializers.IntegerField()
    
    
class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = "__all__"
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"