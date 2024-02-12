from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('register/', views.user_register_view, name = 'user_register'),
    path('verification/', views.email_verify_view, name = 'email_verify'),
    path('sendverification/', views.send_verification_link_view, name = 'send_verification'),
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('forgotpassword/', views.forgot_password_view, name='forgot_password'),
    path('sendforgotpasslink/', views.send_forgot_password_link_view, name = 'send_forgot_pass_link'),
    path('signin/', views.login_view, name = 'signin'),
]
