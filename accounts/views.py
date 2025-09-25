from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import login

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'user_form': form})
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('profile')
        return render(request, 'accounts/register.html', {'user_form': form})
        