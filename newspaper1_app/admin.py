from django.contrib import admin

# Register your models here.

from newspaper1_app.models import Post, Category, Tag, Contact, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Comment)


