from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from static import *
from django.contrib.auth import login, authenticate

def home(request):
    return render(request,"index.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form})

# class SignUp(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("home")
#     template_name = "signup.html"