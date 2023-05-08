#
# @author: Brian
#

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import make_aware
from django.conf import settings
from profileapp.models import ProfileApp, userProfile
from .models import UserApp, LoginApp, SignupForm, LoginForm
import pprint
import json
import datetime
import time
import random


def login(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    pathTo = '/images/'
    map = ['sky', 'wgs84', 'wgs84map']
    rand1 = random.randint(0, len(map) - 1)
    app = {"map": '%s%s.jpg'%(pathTo, map[rand1]), "info": "%s %s"%(now, map[rand1])}
    return render(
        request, 'loginindex.html', context={'pname': pname, 'message': now,
        'cards': map, 'app': app, 'ip': ip, 'year': year},
    )

def signin(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    pathTo = '/images/'
    map = ['sky', 'wgs84', 'wgs84map']
    rand1 = random.randint(0, len(map) - 1)
    app = {"map": '%s%s.jpg'%(pathTo, map[rand1]), "info": "%s %s"%(now, map[rand1])}
    info = "Signin: %s"%(now)
    if request.method == 'POST':
        qrb = request.POST
        try:
            userx = ProfileApp()
            userxp = UserApp()
            email = qrb['email'].strip()
            password = qrb['password'].strip()
            salt = userx.regencode(email, pname)
            pkey = userx.reghash(salt, password, pname)
            hashpassword = userx.reghash(email, pkey, pname)
            #userx.password = hashpassword
            #userx.email = email
            loginx = ProfileApp.objects.filter(email=email, password=hashpassword)
            accn = loginx[0].profile_number
            uname = loginx[0].username
            email = loginx[0].email
            id = loginx[0].id
            form = LoginForm(qrb)
            if form.is_valid():
                #userxp = UserApp.objects.filter(email=email, username=uname)
                #userxp = UserApp.objects.filter(email=email, username=uname).values()
                #userxp = userProfile()
                request.session['pemail'] = email
                request.session['puname'] = uname
                request.session['paccn'] = accn
                #backupXY(loginx.values(), qrb, 'signin')
                return render(
                    request, 'profile.html', context={'pname': pname, 'message': now,
                    'user':loginx.values(), 'userx': userxp, 'cards': map,
                    'app': app, 'ip': ip, 'year': year},
                )
        except Exception as e:
            print("Exception Signin: %s %s"%(now, e))
            info = ("Signin: %s %s"%(now, 'error...'))
            return render(
                request, 'loginindex.html', context={'pname': pname, 'message': info,
                'cards': map, 'app': app, 'ip': ip, 'year': year},
            )
    #return render(
    #    request, 'loginindex.html', context={'pname': pname, 'message': info,
    #    'cards': map, 'app': app, 'ip': ip, 'year': year},
    #)
    return render(
        request, 'profile.html', context={'pname': pname, 'message': now,
        'user':loginx.values(), 'userx': userxp, 'cards': map,
        'app': app, 'ip': ip, 'year': year},
    )

def logout(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    pathTo = '/images/'
    map = ['sky', 'wgs84', 'wgs84map']
    rand1 = random.randint(0, len(map) - 1)
    app = {"map": '%s%s.jpg'%(pathTo, map[rand1]), "info": "%s %s"%(now, map[rand1])}
    infox = "Logout: %s"%(now)
    try:
        request.session['pemail'] = " "
        request.session['puname'] = " "
        request.session['paccn'] = " "
        del request.session['pemail']
        del request.session['puname']
        del request.session['paccn']
        request.session.clear()
        request.session.flush()
    except Exception as e:
        print("logout: %s %s"%(now, e))
        infox = "Logout: %s %s"%(now, 'error....')
    return render(
        request, 'home.html', context={'pname': pname, 'message': infox,
        'cards': map, 'app': app, 'ip': ip, 'year': year},
    )

def signup(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    pathTo = '/images/'
    map = ['sky', 'wgs84', 'wgs84map']
    rand1 = random.randint(0, len(map) - 1)
    app = {"map": '%s%s.jpg'%(pathTo, map[rand1]), "info": "%s %s"%(now, map[rand1])}
    userx = ProfileApp()
    userxy = UserApp()
    accn = userx.account()
    userx.profile_number = accn
    print("accn: %s profile: %s"%(accn, userx.profile_number))
    return render(
        request, 'regindex.html', context={'pname': pname, 'message': now,
        'user': userx, 'userx': userxy, 'cards': map, 'app': app,
        'ip': ip, 'year': year},
    )

def register(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    pathTo = '/images/'
    map = ['sky', 'wgs84', 'wgs84map']
    rand1 = random.randint(0, len(map) - 1)
    app = {"map": '%s%s.jpg'%(pathTo, map[rand1]), "info": "%s %s"%(now, map[rand1])}
    userx = ProfileApp()
    userxy = UserApp()
    done = ("Singup: %s"%(now))
    if request.method == 'POST':
        qrb = request.POST
        try:
            userx.profile_number = userx.account()
            userx.username = qrb['username'].strip()
            userx.first_name = qrb['first_name'].strip()
            userx.last_name = qrb['last_name'].strip()
            userx.email = qrb['email'].strip()
            password = qrb['password'].strip()
            salt = userx.regencode(userx.email, pname)
            pkey = userx.reghash(salt, password, pname)
            hashpassword = userx.reghash(userx.email, pkey, pname)
            userx.password = hashpassword
            userx.usertype = qrb['usertype'].strip()
            #userx.usertypesa = qrb['usertypesa'].strip()
            phone_number = qrb['phone_number'].strip()
            userx.location = qrb['location'].strip()
            userx.longitude = qrb['location'].strip()
            userx.latitude = qrb['latitude'].strip()
            userx.address = qrb['address'].strip()
            userx.address_type = qrb['address_type'].strip()
            userx.language = qrb['language'].strip()
            #userx.admin = qrb['admin'].strip()
            #userx.company = qrb['company'].strip()
            userx.notes = qrb['notes'].strip()
            form = SignupForm(qrb)
            if form.is_valid():
                print("%s-%s-%s"%(now, userx.username, userx.email))
                userx.epverifieddate = now
                userx.date_added = now
                userx.date_modified = now
                done = userx.save()
                print("%s-%s-%s"%(now, userx.username, done))
                userxy = backupX(userx, qrb)
                backupXY(userx, qrb)
                done = "Singup done: %s-%s-%s"%(now, userx.username, done)
        except Exception as e:
            print("register: %s-%s"%(now, e))
            done = '# System offline: %s'%(mytime2())
    else:
        done = "Singup: %s"%(now)
    return render(
        request, 'regindex.html', context={'pname': pname, 'message': done,
        'user': userx, 'userx': userxy, 'cards': map, 'app': app,
        'ip': ip, 'year': year},
    )

def backupX(userx, requestx):
    pname = settings.PRO_NAME
    #urlp = "https://localhost"
    urlp = "http://localhost"
    now = mytime2a()
    year = now.year
    try:
        userxy = UserApp()
        #userxy.user.username = userx.username
        #userxy.user.email = userx.email
        #userxy.user.password = userx.password
        userxy.user_id = userx.id
        userxy.profile_number = userx.profile_number
        userxy.username = userx.username
        userxy.email = userx.email
        userxy.usertype = userx.usertype
        userxy.usertypesa = userx.usertypesa
        userxy.phone_number = userx.phone_number
        userxy.location = userx.location
        userxy.longitude = requestx['location'].strip()
        userxy.latitude = requestx['latitude'].strip()
        userxy.address = userx.address
        userxy.street = requestx['street'].strip()
        userxy.town = requestx['town'].strip()
        userxy.city = requestx['city'].strip()
        userxy.province = requestx['province'].strip()
        userxy.code = requestx['code'].strip()
        userxy.country = requestx['country'].strip()
        userxy.address_type = userx.address_type
        userxy.notes = userx.notes
        form = SignupForm(requestx)
        if form.is_valid():
            print("%s-%s-%s"%(now, userxy.username, userxy.email))
            userxy.date_added = now
            userxy.date_modified = now
            done = userxy.save()
            print("%s-%s-%s"%(now, userxy.username, done))
    except Exception as e:
        print("backupX: %s %s"%(now, e))
    return userxy

def backupXY(userx, requestx, logtype='signup'):
    pname = settings.PRO_NAME
    #urlp = "https://localhost"
    urlp = "http://localhost"
    now = mytime2a()
    year = now.year
    try:
        userxyz = LoginApp()
        userxyz.profile_number = userx.profile_number
        userxyz.username = userx.username
        userxyz.email = userx.email
        userxyz.log_type = logtype
        userxyz.user_type = userx.usertype
        notes = userx.notes
        if (logtype == 'login'):
            userxyz.date_login = now
        if (logtype == 'logout'):
            userxyz.date_logout = now
        if (logtype == 'signup'):
            userxyz.date_login = now
            userxyz.date_logout = now
        form = LoginForm(requestx)
        if form.is_valid():
            print("%s-%s-%s"%(now, userxyz.username, userxyz.email))
            done = userxyz.save()
            print("%s-%s-%s"%(now, userxyz.username, done))
    except Exception as e:
        print("backupXY: %s %s"%(now, e))

def mytime2():
    now = datetime.datetime.now()
    dnow = make_aware(now)
    utcnow = datetime.datetime.utcnow()
    unow = make_aware(utcnow)
    dt = (dnow - unow)
    print("UTC:  %s,   %s, %s-%s"%(utcnow, dt, unow, unow.tzinfo))
    print("Home: %s-%s,       %s-%s"%(now, now.tzinfo, dnow, dnow.tzinfo))
    return dnow

def mytime2a():
    now = datetime.datetime.now()
    dnow = make_aware(now)
    return dnow
