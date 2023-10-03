# context-processor:

from django.db.models import F, Sum, Case, When

from newspaper1_app.models import Category, Tag, Post


def navigation(request):
    categories = Category.objects.all()[:4]
    tags = Tag.objects.all()[:5]
    # Get the post with the highest views_count of posts in each category
    top_categories = (
        Post.objects.values("category__pk", "category__name")
        .annotate(
            pk=F("category__pk"), name=F("category__name"), max_views=Sum("views_count")
        )
        .order_by("-views_count")
        .values("pk", "name", "max_views")
    )
    
    category_ids = [top_category["pk"] for top_category in top_categories]  # [2,6,5,6]
    order_by_max_views = Case(
        *[
            When(
                id=category["pk"], then=category["max_views"]
            )  # When(id=2, then=11), When(id=6,then=2)
            for category in top_categories
        ]
    )
    whats_new_categories = Category.objects.filter(pk__in=category_ids).order_by(
        -order_by_max_views
    )[:4]
    top_categories = Category.objects.filter(pk__in=category_ids).order_by(
        -order_by_max_views
    )[:4]

    

    return {
        "categories": categories,
        "tags": tags,
        "top_categories": top_categories,
        "whats_new_categories": whats_new_categories,
    }


# def navigation(request):
#     categories = Category.objects.all()[:5]
#     tags = Tag.objects.all()[:7]
    
#     # get the post with the maximum views_count of posts in each category
#     top_categories = (
#         Post.objects.values("category__pk", "category__name")
#         .annotate(
#             pk = F("category__pk"), name = F("category__name"), max_views = Sum("views_count")
#         )
#         .order_by("-views_count")
#         .values("pk", "name", "max_views")
#         .distinct()[:4]
#     )
    
#     category_ids = [top_category["pk"] for top_category in top_categories] # [2,6,5,6]
#     order_by_max_views = Case(
#         *[
#             When(
#                 id = category["pk"], then=category["max_views"] # when(id=2, then=11), when(id=6, then=2)
#             )
#             for category in top_categories
#         ]
#     )
    
#     # yo paxi modify gareko ho
#     whats_new_categories = Category.objects.filter(
#         pk__in=category_ids).order_by(-order_by_max_views)[:4]
    
    
#     # yo pailako logic modify garnu vanda agadi
#     # whats_new_categories = Category.objects.filter(
#     #     pk__in=[top_category["pk"] for top_category in top_categories]
#     #     # pk__in = [4,1,6]
#     # )
    
#     return {
#         "categories": categories,
#         "tags": tags,
#         "top_categories": top_categories,
#         "whats_new_categories": whats_new_categories,
            
#     }