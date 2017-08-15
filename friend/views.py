from django.shortcuts import render, redirect

from .data_handling import get_best_friend_factor
from .models import User

# Create your views here.
def index(request):
    return render(request, 'friend/index.html', {})

def find_friends(request):
    if request.method == "POST":
        account = request.POST['account']
        return render(request, 'friend/calculating.html', {'account': account})
    else:
        return render(request, 'friend/calculating.html', {})

def friends_results(request, account, friends):
    return render(request, 'friend/result.html', {'friends': friends})
