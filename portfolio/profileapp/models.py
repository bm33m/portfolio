#
#@Author: Brian
#

from django.db import models
#from django.core.mail import send_mail
from django.utils.timezone import make_aware
import datetime
import base64
import hashlib

# Create your models here.

class ProfileApp(models.Model):
    profile_number = models.CharField(max_length=64, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=256)
    usertype = models.CharField(default='Other', max_length=30)
    usertypesa = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=64, blank=True)
    location = models.TextField(blank=True)
    longitude = models.CharField(max_length=128, blank=True)
    latitude = models.CharField(max_length=128, blank=True)
    address = models.TextField(blank=True)
    address_type = models.CharField(default='home', max_length=30)
    language = models.CharField(max_length=30, blank=True)
    admin = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=60, blank=True)
    notes = models.TextField(blank=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    epverifieddate = models.DateTimeField(blank=True)
    epverificationcode = models.CharField(max_length=256, blank=True)
    notes = models.TextField(blank=True)
    date_added = models.DateTimeField(blank=True)
    date_modified = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.profile_number} {self.username}"

    def mytime(self):
        return mytime2a()

    def account(self):
        return account2()

    def regencode(self, email, pname):
        return regencode2(email, pname)

    def degencode(self, gcode):
        return degencode2(gcode)

    def reghash(self, saltGen1, keyReg, namex):
        return reghash2(saltGen1, keyReg, namex)

def userProfile():
    uprofile = [
       {'id': '1009', 'profile_number': '20230501111234123', 'username': 'cool',
        'email': 'cool@cool.org', 'first_name': 'Myname',
        'location': '-34.397,150.644', 'latitude': '-34.397', 'longitude': '150.644',
        'address': '23 MyStreet Str, MyTown, MyCity, MyState, 0000, MyCountry'},
      {'id': '2099', 'profile_number': '20230502121434123', 'username': 'awesome',
       'email': 'awesome@awesome.org', 'first_name': 'Myname2',
       'location': '62.323907,-150.109291', 'latitude': '62.323907', 'longitude': '-150.109291',
       'address': '67 MyAvenue Ave, MyTown, MyCity, MyProvince, 90000, MyCountry'},
    ]
    return uprofile


def mytime2():
    now = datetime.datetime.now()
    return now

def mytime2a():
    now = datetime.datetime.now()
    dnow = make_aware(now)
    return dnow

def account2():
    d2 = mytime2()
    d3 = d2.microsecond
    accn = "%d%d%d%d%d%d%d"%(d2.year, d2.month, d2.day,
        d2.hour, d2.minute, d2.second, d3%1000)
    sern = int(accn)
    return sern


def regencode2r(reg, name):
    t5 = reg[::-1]
    t6 = b"%s%s"%(name[0],t5)
    #t7b = t6.encode('utf-8')
    gen = base64.b64encode(t6)
    t8 = gen[::-1]
    t9 = b"%s%s"%(name[1],t8)
    #t10b = t9.encode('utf-8')
    gen2 = base64.b64encode(t9)
    #t11 = gencode.decode('utf-8', 'ignore')
    return gen2

def reghash2(gen1, reg, name):
    gen = regencode2(reg, name)
    ghash = hashlib.sha512()
    t9 = "%s%s%s"%(name[1], gen1, gen)
    t10b = t9.encode('utf-8')
    ghash.update(t10b)
    ghash2 = ghash.hexdigest()
    return ghash2

def degencode2(arg):
    try:
        tb = arg.encode('utf-8')
        dec1 = base64.b64decode(arg)
        t2a = dec1.decode('utf-8')
        t2 = t2a[1:]
        t1 = t2[::-1]
        tb1 = t1.encode('utf-8')
        dec2 = base64.b64decode(tb1)
        t5a = dec2.decode('utf-8')
        t5 = t5a[1:]
        t6 = t5[::-1]
        return t6
    except Exception as e:
        return "%s-%s"%(arg, e)

    return '0'

def regencode2(reg, name):
    t1 = reg[::-1]
    t2 = "%s%s"%(name[0],t1)
    tb = t2.encode('utf-8')
    gen1 = base64.b64encode(tb)
    t4a = gen1.decode('utf-8')
    t4 = t4a[::-1]
    t5 = "%s%s"%(name[1],t4)
    t5b = t5.encode('utf-8')
    gen2 = base64.b64encode(t5b)
    t6 = gen2.decode('utf-8')
    return t6
