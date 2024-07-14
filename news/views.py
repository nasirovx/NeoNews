from rest_framework import generics, status
from .models import News, Category
from .serializers import NewsSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from .serializers import *

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"status": "password set"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmCodeView(generics.CreateAPIView):
    serializer_class = ConfirmCodeSerializer

    def create(self, request, *args, **kwargs):
        # Logic for confirming code
        return Response({"status": "code confirmed"}, status=status.HTTP_200_OK)

class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class LoginRefreshView(TokenRefreshView):
    pass

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

class ResendConfirmationView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        # Logic for resending confirmation
        return Response({"status": "confirmation resent"}, status=status.HTTP_200_OK)


class NewsAPIList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsAPIDetail(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'

class CategoryAPIList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@api_view(['GET'])
def favorite_news_list(request):
    queryset = News.objects.filter(is_favorite=True)
    serializer = NewsSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_favorite(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    news.is_favorite = True
    news.save()
    return Response({'is_favorite': news.is_favorite}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def remove_from_favorite(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    news.is_favorite = False
    news.save()
    return Response(status=status.HTTP_204_NO_CONTENT)