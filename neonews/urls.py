from django.contrib import admin
from django.urls import path
from news.views import *
# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Neonews API",
        default_version='v1',
        description="API Neonews предоставляет доступ к различным запросам, требующим аутентификации с помощью токена Bearer. Для аутентификации включите 'Bearer {access_token}' в заголовок 'Authorization'.",
        terms_of_service="https://www.itcbootcamp.com/info_pages/privacy_policy",
        contact=openapi.Contact(
            name="Bekastan",
            url="https://instagram.com/5ekastan",
            email="5ekastan@gmail.com",
        ),
        license=openapi.License(
            name="BSD License",
            url="https://opensource.org/licenses/BSD",
        ),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # news
    path('news/list/', NewsAPIList.as_view(), name='news-list'),
    path('news/detail/<int:pk>/', NewsAPIDetail.as_view(), name='news-detail'),
    path('news/category/', CategoryAPIList.as_view(), name='news-category'),
    
    # Favorites
    path('favorites/', favorite_news_list, name='favorites-news-list'),
    path('favorites/<int:pk>/add/', add_to_favorite, name='add-to-favorite'),
    path('favorites/<int:pk>/remove/', remove_from_favorite, name='remove-from-favorite'),
    
    # Authentication
    path('users/register/', RegisterView.as_view(), name='users_register_create'),
    path('users/change-password/', ChangePasswordView.as_view(), name='users_change-password_update'),
    path('users/confirm-code/', ConfirmCodeView.as_view(), name='users_confirm-code_create'),
    path('users/login/', LoginView.as_view(), name='users_login_create'),
    path('users/login/refresh/', LoginRefreshView.as_view(), name='users_login_refresh_create'),
    path('users/me/', UserDetailView.as_view(), name='users_me_read'),
    path('users/user-profile/', UserProfileView.as_view(), name='users_user-profile_update'),
    path('users/resend-confirmation/', ResendConfirmationView.as_view(), name='users_resend-confirmation_create'),
    
    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
