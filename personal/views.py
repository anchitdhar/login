from django.shortcuts import render
from personal.models import Question
from account.models import Account
# Create your views here.
def home_screen_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request,"personal/home.html",context= None)