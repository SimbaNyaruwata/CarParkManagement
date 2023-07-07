
import statistics
import threading
import cv2
import numpy as np
import yaml
from imutils.object_detection import non_max_suppression
from . import Khare_utility_01 as util
from cv2 import HOGDescriptor_getDaimlerPeopleDetector
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.views.decorators import gzip
from django.http import StreamingHttpResponse


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import CreateUserForm
import subprocess
from django.http import JsonResponse


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'carparkman/login.html', context)


def logout_request(request):
    logout(request)
    return redirect('/login/')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('/login/')
    context = {'form': form}
    return render(request, 'carparkman/register.html', context)


@login_required(login_url='/login/')
def index(request):
    return render(request, 'carparkman/index.html')


@login_required(login_url='/login/')
def charts(request):
    subprocess.run(
        ["python", "C:/Users/hp/Desktop/Projects/CarParkManagement/carparkman/Simba Car Park Detection.py"])


@login_required(login_url='/login/')
def widgets(request):
    subprocess.run(
        ["python", "C:/Users/hp/Desktop/Projects/CarParkManagement/carparkman/Donne.py"])
    # return HttpResponse("Script executed!")
    return render(request, 'carparkman/widgets.html')
