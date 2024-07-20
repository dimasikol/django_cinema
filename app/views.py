from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Genres, Actors, Cinema
from django.db.models import Q
from django.contrib.auth import logout, login, authenticate


def index(request):
    genres = Genres.objects.all()
    return render(request,'homepage.html',context={'cinema_type':genres})


def cinema(request,**kwargs):
    genres = Genres.objects.all()
    active = genres.first()
    data = []
    if request.GET:
        data = Cinema.objects.filter(Q(cinema__name=request.GET['genres']) | Q(cinema__name='fantastic'))
        active = request.GET['genres']
    return render(request,'cinema.html',context={'active':active,'cinema_type':genres,'data':data})


def users(request):
    genres = Genres.objects.all()

    return render(request,'users.html',context={'cinema_type':genres})

def show_bio(request):
    genres = Genres.objects.all()
    return render(request,'bio.html',context={'cinema_type':genres})


def user_logout(request):
    logout(request)
    return render(request, 'homepage.html', )


def user_reset_password(request):
    pass

def sign_up(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html',{"message":f'you are activate, {request.user.username} {request.user.email}'} )
    if request.POST:
        if request.POST['password']==request.POST['password2']:
            user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
            user.save()
            login(request,user=user)
            return render(request,'homepage.html',)
    return render(request,'sign_up.html')
def user_loging(request):
    if request.POST:
        print(request.POST)
        if user := authenticate(username=request.POST['username'],password=request.POST['password']):
            login(request,user)
            return render(request,'homepage.html',)
        print(user)

    if request.user.is_authenticated:
        return render(request, 'homepage.html',{"message":f'you are activate, {request.user.username} {request.user.email}'} )

    return render(request, 'sign_in.html')

