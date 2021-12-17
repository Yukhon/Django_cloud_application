from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import hashlib

# Create your views here.
from .models import *


def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        # the same password
        # uname could be used
        username = request.POST['uname']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        if password_2 != password_1:
            return HttpResponse('password is not the same')
        m = hashlib.md5()
        m.update(password_1.encode())
        password_m = m.hexdigest()
        # hash algorithm
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('user name has been registered')
        try:

            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            print('--create user error %s' % e)
            return HttpResponse('user name has been registered in distributed system')

        # set session
        request.session['username'] = username
        request.session['uid'] = user.id
        request.session.set_expiry(60 * 60 * 24)
        return HttpResponseRedirect('/index')


def login_view(request):
    if request.method == 'GET':
        # check session and cookies
        if request.session.get('username') and request.session.get('uid'):
            # return HttpResponse('login successfully')
            return HttpResponseRedirect('/index')
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            # return HttpResponse('login successfully')
            return HttpResponseRedirect('/index')
        return render(request, 'user/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # # old_users = User.objects.filter(username=username)
        # if not old_users:
        #
        #     return HttpResponse('username does not exist')
        try:
            old_user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s' % e)
            return HttpResponse('invalid username')
        m = hashlib.md5()
        m.update(password.encode())
        password_m = m.hexdigest()
        if password_m != old_user.password:
            return HttpResponse('invalid password')

        request.session['username'] = username
        request.session['uid'] = old_user.id
        resp = HttpResponseRedirect('/index')
        if 'remember' in request.POST:
            resp.set_cookie('username', username, 3600 * 24 * 3)
            resp.set_cookie('uid', old_user.id, 3600 * 24 * 3)

        return resp
