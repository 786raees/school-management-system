from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

def Log_out_user(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('account_login')