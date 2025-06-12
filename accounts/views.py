from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm, CustomLoginForm



def customer_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Change to your actual homepage or dashboard
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/customer_register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('customer-dashboard')  # or seller-dashboard depending on role

    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")

            # Redirect based on role
            if user.role == 'CUSTOMER':
                return redirect('home')
            # elif user.role == 'SELLER':
            #     return redirect('seller-dashboard')
            # elif user.is_superuser:
            #     return redirect('/admin/')
            else:
                return redirect('home')  # fallback
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logout Successfully.")
    return redirect("/")