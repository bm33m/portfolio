#
# @author: Brian
#

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import make_aware
from django.conf import settings
from .models import ProfileApp, userProfile
from signupapp.models import UserApp, LoginApp, SignupForm, LoginForm, EditForm
import pprint
import json
import datetime
import time
import random

def index(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    pathTo = '/images/'
    map = ['sky', 'wgs84', 'wgs84map']
    rand1 = random.randint(0, len(map) - 1)
    app = {"map": '%s%s.jpg'%(pathTo, map[rand1]), "info": "%s %s"%(now, map[rand1])}
    users = map
    infox = "Welcome back: %s"%(now)
    try:
        users = userProfile()
        userp = ProfileApp()
        userx = UserApp()
        namex = userx.username
        print("01 namex: %s %s"%(namex, now))
        print("02 profile: %s, %s, %s"%(users, userp, userx))
        #users = ProfileApp.objects.all()
        #users = ProfileApp.objects.all().values()
    except Exception as e:
        print("Index %s %s"%(now, e))
        infox = ("Home: %s %s"%(now, 'system offline.'))
        users = userProfile()
    return render(
        request, 'home.html', context={'pname': pname, 'message': infox,
        'users': users, 'app': app, 'ip': ip, 'year': year},
    )

def profile(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    pathTo = '/images/'
    map = ['sky', 'wgs84', 'wgs84map']
    rand1 = random.randint(0, len(map) - 1)
    app = {"map": '%s%s.jpg'%(pathTo, map[rand1]), "info": "%s %s"%(now, map[rand1])}
    infox = now
    users = ProfileApp()
    try:
       userp = {}
       userp['pemail'] = request.session['pemail']
       userp['puname'] = request.session['puname']
       userp['paccn'] = request.session['paccn']
       users = ProfileApp.objects.filter(email=userp['pemail'], profile_number=userp['paccn']).values()
       userxy = UserApp.objects.filter(email=userp['pemail'], profile_number=userp['paccn']).values()
       return render(
           request, 'profile.html', context={'pname': pname, 'message': now,
           'user': users, 'userx': userxy, 'app': app, 'ip': ip, 'year': year},
       )
    except Exception as e:
        infox = "Profile: %s %s"%(now, 'Login...required...')
        print("Profile: %s %s"%(now, e))
    return render(
        request, 'loginindex.html', context={'pname': pname, 'message': infox,
        'cards': map, 'app': app, 'ip': ip, 'year': year},
    )

def deleteProfile(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    pathTo = '/images/'
    map = ['sky', 'wgs84', 'wgs84map']
    rand1 = random.randint(0, len(map) - 1)
    app = {"map": '%s%s.jpg'%(pathTo, map[rand1]), "info": "%s %s"%(now, map[rand1])}
    infox = now
    users = ProfileApp()
    try:
       userp = {}
       userp['pemail'] = request.session['pemail']
       userp['puname'] = request.session['puname']
       userp['paccn'] = request.session['paccn']
       users = ProfileApp.objects.filter(email=userp['pemail'], profile_number=userp['paccn']).values()
       userxy = UserApp.objects.filter(email=userp['pemail'], profile_number=userp['paccn']).values()
       return render(
           request, 'delete.html', context={'pname': pname, 'message': now,
           'user': users, 'userx': userxy, 'app': app, 'ip': ip, 'year': year},
       )
    except Exception as e:
        infox = "deleteProfile: %s %s"%(now, 'Login...required...')
        print("deleteProfile: %s %s"%(now, e))
    return render(
        request, 'loginindex.html', context={'pname': pname, 'message': infox,
        'cards': map, 'app': app, 'ip': ip, 'year': year},
    )


def profiles(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    pathTo = '/images/'
    map = ['sky', 'wgs84', 'wgs84map']
    rand1 = random.randint(0, len(map) - 1)
    app = {"map": '%s%s.jpg'%(pathTo, map[rand1]), "info": "%s %s"%(now, map[rand1])}
    infox = now
    try:
        userp = {}
        userp['email'] = request.session['pemail']
        userp['puname'] = request.session['puname']
        userp['paccn'] = request.session['paccn']
        return render(
            request, 'profiles.html', context={'pname': pname, 'message': now,
            'userp': userp, 'cards': map, 'app': app, 'ip': ip, 'year': year},
        )
    except Exception as e:
        infox = "Profiles: %s %s"%(now, 'Login...required...')
        print("Profiles: %s %s"%(now, e))
    return render(
        request, 'loginindex.html', context={'pname': pname, 'message': infox,
        'cards': map, 'app': app, 'ip': ip, 'year': year},
    )

def info(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    pathTo = '/images/'
    map = ['sky', 'wgs84', 'wgs84map']
    rand1 = random.randint(0, len(map) - 1)
    app = {"map": '%s%s.jpg'%(pathTo, map[rand1]), "info": "%s %s"%(now, map[rand1])}
    users = map
    infox = "Welcome back: %s"%(now)
    try:
        users = userProfile()
        userp = ProfileApp()
        userx = UserApp()
        namex = userx.username
        print("01 namex: %s %s"%(namex, now))
        print("02 profile: %s, %s, %s"%(users, userp, userx))
        try:
            users = ProfileApp.objects.all()
            #users = ProfileApp.objects.all().values()
        except Exception as e:
            print("info: %s %s"%(now, e))
    except Exception as e:
        print("Index %s %s"%(now, e))
        infox = ("Info: %s %s"%(now, 'system offline.'))
        users = userProfile()
    return render(
        request, 'info.html', context={'pname': pname, 'message': infox,
        'users': users, 'app': app, 'ip': ip, 'year': year},
    )

def edit(request):
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
    done = ("Edit: %s"%(now))
    if request.method == 'POST':
        qrb = request.POST
        try:
            #userx = ProfileApp.objects.filter(email=userx.email, profile_number=userx.profile_number)
            userp = {}
            userp['pemail'] = request.session['pemail']
            userp['puname'] = request.session['puname']
            userp['paccn'] = request.session['paccn']
            userx = ProfileApp.objects.filter(email=userp['pemail'], profile_number=userp['paccn']).values()
            userxy = UserApp.objects.filter(email=userp['pemail'], profile_number=userp['paccn']).values()
            #accn = userx[0].profile_number
            #uname = userx[0].username
            #email = userx[0].email
            #userx.profile_number = userx.account()
            #userx.username = qrb['username'].strip()
            userx.first_name = qrb['first_name'].strip()
            userx.last_name = qrb['last_name'].strip()
            #userx.email = qrb['email'].strip()
            #password = qrb['password'].strip()
            #salt = userx.regencode(userx.email, pname)
            #pkey = userx.reghash(salt, password, pname)
            #hashpassword = userx.reghash(userx.email, pkey, pname)
            #userx.password = hashpassword
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
            form = EditForm(qrb)
            if form.is_valid():
                print("%s-%s-%s"%(now, userx.username, userx.email))
                userx.date_modified = now
                done = userx.save()
                print("%s-%s-%s"%(now, userx.username, done))
                #userxy = backupX(userx, qrb)
                #backupXY(userx, qrb)
                done = "Edit done: %s-%s-%s"%(now, userx.username, done)
            return render(
                request, 'profile.html', context={'pname': pname, 'message': done,
                'user': users, 'userx': userxy, 'app': app, 'ip': ip, 'year': year},
            )
        except Exception as e:
            print("Edit: %s-%s"%(now, e))
            done = '# System offline: %s'%(mytime2())
    else:
        done = "Login: %s"%(now)
    return render(
        request, 'home.html', context={'pname': pname, 'message': done,
        'users': users, 'app': app, 'ip': ip, 'year': year},
    )

def delete(request):
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
    done = ("Delete: %s"%(now))
    if request.method == 'POST':
        qrb = request.POST
        try:
            userp = {}
            userp['pemail'] = request.session['pemail']
            userp['puname'] = request.session['puname']
            userp['paccn'] = request.session['paccn']
            userx = ProfileApp.objects.filter(email=userp['pemail'], profile_number=userp['paccn']).values()
            userxy = UserApp.objects.filter(email=userp['pemail'], profile_number=userp['paccn']).values()
            userx.profile_number = userx.account()
            userx.username = qrb['username'].strip()
            userx.first_name = qrb['first_name'].strip()
            userx.last_name = qrb['last_name'].strip()
            userx.email = qrb['email'].strip()
            #password = qrb['password'].strip()
            #salt = userx.regencode(userx.email, pname)
            #pkey = userx.reghash(salt, password, pname)
            #hashpassword = userx.reghash(userx.email, pkey, pname)
            #userx.password = hashpassword
            #userx.usertype = qrb['usertype'].strip()
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
            form = EditForm(qrb)
            if form.is_valid():
                print("%s-%s-%s"%(now, userx.username, userx.email))
                userx.date_modified = now
                #done = userx.save()
                done = userx.delete()
                print("%s-%s-%s"%(now, userx.username, done))
                #userxy = backupX(userx, qrb)
                #backupXY(userx, qrb)
                done = "Delete done: %s-%s-%s"%(now, userx.username, done)
        except Exception as e:
            print("Delete: %s-%s"%(now, e))
            done = '# System offline: %s'%(mytime2())
    else:
        done = "Login: %s"%(now)
    return render(
        request, 'home.html', context={'pname': pname, 'message': done,
        'users': users, 'app': app, 'ip': ip, 'year': year},
    )

def mytime2():
    now = datetime.datetime.now()
    dnow = make_aware(now)
    utcnow = datetime.datetime.utcnow()
    unow = make_aware(utcnow)
    dt = (dnow - unow)
    print("UTC:  %s,   %s, %s-%s"%(utcnow, dt, unow, unow.tzinfo))
    print("Home: %s-%s,       %s-%s"%(now, now.tzinfo, dnow, dnow.tzinfo))
    return dnow
