from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Profile
from .forms import UserForm
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        # attempting to log in
        username = request.POST.get('username')  # POST['username']
        password = request.POST.get('password')  # POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "You are now logged in as {}".format(user.username))
            return redirect('all_statuses')
        else:
            return render(request,
                          'users/login.html',
                          {'failed': True,
                           'username': username})

    return render(request,
                  'users/login.html')


def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = user.password

            user.set_password(password)
            user.save()

            profile = Profile(
                user=user,
                password='password'
            )

            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            return redirect('all_statues')
    else:
        form = UserForm()
    return render(request, 'users/register.html',
                  {'form': form})
