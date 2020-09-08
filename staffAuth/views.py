from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import LoginForm
from .models import Staff
from administrator.helpers import get_all_staff

# Create your views here.
def index(request):
    logout(request)
    form = LoginForm()
    error = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            staff_ID = form.cleaned_data['staff_ID']
            password = form.cleaned_data['password']

            staff = authenticate(request, staff_ID=staff_ID, password=password)

            if staff is not None:
                login(request, staff)
                return HttpResponseRedirect(reverse('staffAuth:dashboard'))
        else:
            error = True
    return render(request, 'auth/login.html', {'form': form, 'error': error})

@login_required
def dashboard(request):
    all_staff = get_all_staff(Staff)
    return render(request, 'auth/dashboard.html', {'all_staff': all_staff})
