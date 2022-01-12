from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
]