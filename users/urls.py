
from django.urls import path
from . import views

urlpatterns = [
    path('users/register/', views.UserView.as_view()),
    path('users/', views.UserView.as_view()),
    path('users/login/', views.LoginUserView.as_view()),
    path('users/<int:user_id>/', views.UserViewDetail.as_view())
]
