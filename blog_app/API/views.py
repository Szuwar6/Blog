
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import generics
from .serializers import ArticleSerializer
from blog.models import Article

class GetAllArticles(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class GetArticle(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article


class CreateArticle(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


class DestroyArticle(generics.DestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    queryset = Article

class UpdateArticle(generics.UpdateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    queryset = Article

class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    queryset = Article