from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import RegistrationForm

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account is ready. Welcome to PlugListing!")
        return redirect("dashboard")
    return render(request, "accounts/register.html", {"form": form})
