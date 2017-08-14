from django.shortcuts import render, redirect

from .data_handling import get_num_account_history, get_permlinks
from .models import User

# Create your views here.
def index(request):
    return render(request, 'friend/index.html', {})

def find_friends(request):
    if request.method == "POST":
        account = request.POST['account']
        if account == "":
            return redirect("/")
        else:
            data = [('a', 10),('b',9),('c',8),('d',7),('e',6),('f',5)]
            return friends_results(request, account, data)
    else:
        return render(request, 'friend/calculating.html', {})

def friends_results(request, account, friends):
    return render(request, 'friend/result.html', {'friends': friends})
