#!/usr/bin/python
#coding:utf-8

"""
@function: 
@notice:
@author: xiangjie
@file: urls.py
@time: 2016/4/4 20:50
"""

from django.conf.urls import include, url
from myweb import views as mywebViews

urlpatterns = [
    url(r"^temp/$", mywebViews.temp),
    url(r"^test/$", mywebViews.test),
    url(r"^login/$", mywebViews.login)

]