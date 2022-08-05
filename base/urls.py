from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    # Home
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"),
    # User profile
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
    # Create Room
    path('create-room/', views.createRoom, name='create-room'),
    # Update Room
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    # Delete Room
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),

    # Delete Message
    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),
    # Edit Message
    path('update-message/<str:pk>', views.updateMessage, name='update-message'),

]
