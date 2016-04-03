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
#
# p2.name = "中文"
# p2.save()

pushlishs =  Pushlish.objects.filter(name='kevin')
print pushlishs

pushlishs =  Pushlish.objects.filter(name__contains='kevin')
print pushlishs

pushlishs =  Pushlish.objects.filter(name__startswith='kevin')
print pushlishs

#排序 order , 逆向排序字段前加-
pushlishs =  Pushlish.objects.filter(id__range=[3,4]).order_by("-id")
print pushlishs

#更新
pushlishs =  Pushlish.objects.filter(id__range=[3,4]).update(address="长沙")
print pushlishs

##获取单个对象， 不是单个则会异常
pushlishs = Pushlish.objects.get(name='kevin')
print pushlishs

#删除数据
pushlishs =  Pushlish.objects.filter(id=4).delete()
print pushlishs