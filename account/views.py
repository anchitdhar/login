from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
# Create your views here.
from account.forms import RegisterationForm

def registeraion_view(request):
    context = {}
    if request.POST:
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email =email,password = raw_password)
            login(request,account)
            return redirect('home')
        else:
            context['registeration_form'] = form
    else:
        form = RegisterationForm()
        context['registeration_form'] = form
    return render(request,'account/register.html',context)

def logout_view(request):
    logout(request)
    return redirect('home')