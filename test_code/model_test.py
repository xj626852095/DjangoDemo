#!/usr/bin/python
#coding:utf-8

"""
@function: 
@notice:
@author: xiangjie
@file: model_test.py
@time: 2016/4/3 19:13
"""

from django.conf import settings

dbCfg = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "django_demo",
        'USER' : "root",
        "PASSWORD" : "",
        "HOST" : "127.0.0.1",
        "PORT" : "3306"
    }
}
settings.configure(DATABASES=dbCfg)
from myweb.models import Pushlish

# p1 = Pushlish(name='Apress', address='2855 Telegraph Avenue',
#           city='Berkeley', state_province='CA', country='U.S.A.',
#           website='http://www.apress.com/')
# p1.save()
#
# p2 = Pushlish(name="O'Reilly", address='10 Fawcett St.',
#            city='Cambridge', state_province='MA', country='U.S.A.',
#            website='http://www.oreilly.com/')
# p2.save()
pushlishs =  Pushlish.objects.all()
print pushlishs

