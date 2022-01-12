from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include,path
router = DefaultRouter()
router.register('post',views.PostViewSet) #2개 URL을 만들어준다.
#router.urls #url pattern list

urlpatterns = [
    path('public/',views.public_post_list),
    path('', include(router.urls)),
    path('mypost/<int:pk>/', views.PostDetailAPIView.as_view()),
]
