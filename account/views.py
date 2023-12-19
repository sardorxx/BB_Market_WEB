from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import SignUP, UpdateProfile
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail


User = get_user_model()


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        last_login = request.POST.get('last_login')
        is_superuser = request.POST.get('is_superuser')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        date_joined = request.POST.get('date_joined')
        first_name = request.POST.get('first_name')
        user = authenticate(request, username=username, password=password, last_login=last_login,
                            is_superuser=is_superuser,
                            last_name=last_name, email=email, date_joined=date_joined, first_name=first_name)
        if not user:
            messages.error(request, 'User not found')
            return render(request, 'account/login.html')
        login(request, user)
        messages.info(request, 'Login successfully')
        return redirect('marketface:home')

    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Log out successfully')
    return redirect('account:login')


def sign_up(request):
    if request.method == 'POST':
        form = SignUP(request.POST)
        if form.is_valid():
            user = form.save()
            # subject = 'Test project'
            # message = f"HI {user.username}, You are registered"
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [user.email]
            # send_mail(subject, message, email_from, recipient_list)

            messages.success(request, 'You are registered')
            return redirect('account:login')
        messages.warning(request, 'Please retry again')

    form = SignUP()
    context = {
        'form': form
    }

    return render(request, 'account/register.html', context)


@login_required()
def profile_user(request):

    profile = request.user
    context = {
        'profile': profile
    }
    return render(request, 'account/profile.html', context)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })


def update_view(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile updated successfully')
            return redirect('account:profile')
        messages.warning(request, 'Please retry again')

    form = UpdateProfile(instance=user)
    context = {
        'form': form
    }

    return render(request, 'account/update_profile.html', context)