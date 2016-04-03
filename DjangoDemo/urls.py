#coding: utf-8
"""DjangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from demo import views
from myweb import views as mywebViews

"""
正则表达式字符串的开头字母“r”。 它告诉Python这是个原始字符串，不需要处理里面的反斜杠（转义字符）
url路径参数 (?P<name>pattern),
添加一个新的app, myweb
"""

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^hello/$', views.hello),
    url(r"^time/$", views.curTime),
    url(r"^num/(?P<param>\d+)/$", views.printNum),
    url(r"^temp/$", views.temp),
    url(r"^json/$", views.printJson),

    url(r"^myweb/temp/$", mywebViews.temp)
]
