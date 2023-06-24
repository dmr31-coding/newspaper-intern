from django.contrib import admin

# Register your models here.

from newspaper1_app.models import Post, Category, Tag, Contact, Comment

# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Comment)


from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ("content",)
    list_display = ("title", "category", "author", "created_at",)
    date_hierarchy = "published_at"

admin.site.register(Post, PostAdmin)