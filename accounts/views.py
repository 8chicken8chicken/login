from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('board:index')
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            auth_login(request, user)
            return redirect('board:index')
    else:
        form = UserCreationForm(data=request.POST)
    return render(request, 'accounts/signup.html', {
                  'form' : form
    })

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('board:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('board:index') 
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {
        'form':form
    })


def logout(request):
    auth_logout(request)
    return redirect('board:index')