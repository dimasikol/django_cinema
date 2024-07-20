from django.urls import path
from .views import index, users, show_bio, cinema, user_loging, sign_up, user_logout

urlpatterns = [
    path('',index,name='homepage'),
    path('users/',users,name='users'),
    path('bio/',show_bio,name='show_bio'),
    path('cinema/',cinema,name='cinema'),
    path('sign_up/',sign_up,name='sign_up'),
    path('sign_in/',user_loging,name='sign_in'),
    path('logout/',user_logout,name='logout')
]
