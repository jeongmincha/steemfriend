from django.shortcuts import render

from .models import User

# Create your views here.
def index(request):
    return render(request, 'friend/index.html', {})

def friends(request):
    return render(request, 'friends/result.html', {})
