from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def register(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'auth_app/register.html', {'form': UserRegisterForm()})

    form = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {username}!')
        return redirect('login')
    else:
        for key, value in form.error_messages.items():
            messages.warning(request, f'{(key.replace("_", " ")).capitalize()}: {value}')
            return redirect('register')
    
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'auth_app/logout.html')