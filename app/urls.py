from django.urls import path
from .views import UserRegisterView, UserLoginView, DisplayContentView, CreateContentView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register-user'),
    path('login/', UserLoginView.as_view(), name='login-user'),
    path('create-content/', CreateContentView.as_view(), name='create-content'),
    path('update-content/<int:pk>', CreateContentView.as_view(), name='create-content'),
    path('content/', DisplayContentView.as_view(), name='display-content'),

]
