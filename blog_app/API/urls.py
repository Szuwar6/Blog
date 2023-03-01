from django.urls import path
from .views import (
    GetAllArticles,
    GetArticle,
    CreateArticle,
    DestroyArticle,
    UpdateArticle,
    RetrieveUpdateDestroy,
)

urlpatterns = [
    path("articles/", GetAllArticles.as_view(), name="get_articles"),
    path("article/<int:pk>/", GetArticle.as_view(), name="get_article"),
    path("article/create/", CreateArticle.as_view(), name="create_article"),
    path("article/destroy/<int:pk>/", DestroyArticle.as_view(), name="destroy_article"),
    path("article/update/<int:pk>/", UpdateArticle.as_view(), name="update_article"),
    path("article/rud/<int:pk>/", RetrieveUpdateDestroy.as_view(), name="rud"),
]
