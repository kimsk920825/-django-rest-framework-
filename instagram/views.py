from instagram.permissions import IsAuthorOrReadonly
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics 
from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

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
    permission_classes = [IsAuthenticated, IsAuthorOrReadonly] #인증이 됨을 보장받을 수 있음.
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['message']
    
    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body:", request.body)#실제 프로덕션이라면 Print는 비추, 장고 기본의 로거를 상요해라
    #     print("request.POST:", request.POST)
    #     return super().dispatch(request, *args, **kwargs)

    def perform_create(self,serializer):
        # FIXME: 인증이 되어있다는 가정하에, author를 지정
        author = self.request.user #User or AnonymouseUser
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(author=author, ip=ip)

    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['PATCH'])
    def set_public(self,request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

"""
아래 2개를 한번에 만들어 주는 것이 from rest_framework.viewsets import ModelViewSet, from .serializers import PostSerializer
def post_list(request):
    #2개 분기
    pass

def post_detail(request):
    # request.method => 최소 3개 분기
    pass
"""

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'instagram/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({
            'post' : PostSerializer(post).data

        })