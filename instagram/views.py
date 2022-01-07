from rest_framework.viewsets import ModelViewSet
from rest_framework import generics 
from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post


class PublicPostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body:", request.body)#실제 프로덕션이라면 Print는 비추, 장고 기본의 로거를 상요해라
    #     print("request.POST:", request.POST)
    #     return super().dispatch(request, *args, **kwargs)
"""
아래 2개를 한번에 만들어 주는 것이 from rest_framework.viewsets import ModelViewSet, from .serializers import PostSerializer
def post_list(request):
    #2개 분기
    pass

def post_detail(request):
    # request.method => 최소 3개 분기
    pass
"""
