from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics 
from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response


#generic 이용
# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

#순수 APIView 이용
# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
# public_post_list = PublicPostListAPIView.as_view()

#함수 기반 이용
@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)

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
