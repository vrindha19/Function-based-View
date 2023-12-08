from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return HttpResponse(f"Form submitted successfully! Username: {username}, Password: {password}")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
