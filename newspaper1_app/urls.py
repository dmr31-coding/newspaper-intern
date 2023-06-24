

from django.urls import path

from newspaper1_app import views


urlpatterns = [
    path("", views.HomeView.as_view(), name='home',),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name='post-detail',),
    path("post-list", views.PostListView.as_view(), name='post-list',),
    path("post-by-category/<int:cat_id>/", views.PostByCategoryView.as_view(), name = "post-by-category",),
    path("post-by-tag/<int:tag_id>/", views.PostByTagView.as_view(), name = "post-by-tag",),
    path("about/", views.AboutView.as_view(), name = "about"),
    path("post-search/", views.PostSearchView.as_view(),name = "post-search",),
    path("contact/", views.ContactView.as_view(), name = "contact",),
    path("newsletter/", views.NewsletterView.as_view(), name = "newsletter",),
    path("comment/", views.CommentView.as_view(), name = "comment",),
    path(
        "post1-delete/<int:pk>/",
        views.PostDeleteView.as_view(), 
        name="post1-delete"),
    path(
        "post1-create/",
        views.PostCreateView.as_view(), 
        name="post1-create"),
    path(
        "draft1-list/",
        views.DraftListView.as_view(), 
        name="draft1-list"),
    path(
        "post1-publish/<int:pk>/",
        views.PostPublishView.as_view(), 
        name="post1-publish"),
    path(
        "post1-update/<int:pk>/",
        views.PostUpdateView.as_view(), 
        name="post1-update"),
    path(
        "draft1-detail/<int:pk>/",
        views.DraftDetailView.as_view(), 
        name="draft1-detail"),
    path(
        "tag-list/",
        views.TagListView.as_view(), 
        name="tag-list"),
    path(
        "tag-update/<int:pk>/",
        views.TagUpdateView.as_view(), 
        name="tag-update"),
    path(
        "tag-delete/<int:pk>/",
        views.TagDeleteView.as_view(), 
        name="tag-delete"),
    path(
        "tag-create/",
        views.TagCreateView.as_view(), 
        name="tag-create"),
    # category
    
    path(
        "category-list/",
        views.CategoryListView.as_view(), 
        name="category-list"),
    path(
        "category-update/<int:pk>/",
        views.CategoryUpdateView.as_view(), 
        name="category-update"),
    path(
        "category-delete/<int:pk>/",
        views.CategoryDeleteView.as_view(), 
        name="category-delete"),
    path(
        "category-create/",
        views.CategoryCreateView.as_view(), 
        name="category-create"),
]
