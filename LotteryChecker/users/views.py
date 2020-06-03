from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/profile')

    if request.method == "POST":
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           raw_password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=raw_password)
           login(request, user)
           return redirect('/profile')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})
    