from django.shortcuts import render, redirect

from .data_handling import steemsql
from .models import User

# Create your views here.
def index(request):
    return render(request, 'friend/index.html', {})

def find_friends(request):
    if request.method == "POST":
        account = request.POST['account']
        friends = steemsql.get_best_friends(account)
        friends = friends[:10]
        return friends_results(request, account, friends)
    else:
        return render(request, 'friend/calculating.html', {})

def friends_results(request, account, friends):
    return render(request, 'friend/result.html', {'friends': friends})
