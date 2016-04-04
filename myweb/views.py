#coding: utf-8
from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime as dt
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import  json
import django.forms
from django.contrib import auth

"""
 一个视图就是Python的一个函数。这个函数第一个参数的类型是HttpRequest；它返回一个HttpResponse实例。
"""

def temp(request):
    """使用模板语言"""
    print request.META
    return render_to_response("temp_demo.html" , {"name":"kevin , this is my web"})
    #return HttpResponseRedirect("http://www.baidu.com")


#表单校验
class UserInfoForm(forms.Form):
    name = forms.CharField()
    addr = forms.CharField()
    email = forms.EmailField(required=False)

def test(request):
    """"表单提交"""
    print request.COOKIES
    print request.session

    if "count" in request.session:
        count = int(request.session["count"])+1
        request.session["count"] = count
    else:
        request.session["count"] = 0

    result = {}
    if request.method == "GET":
        form = UserInfoForm(request.GET)
        if form.is_valid():
            result = form.cleaned_data
        else:
            result = {"msg":"数据格式有误"}
    jsonStr = json.dumps(result, sort_keys=True)
    return HttpResponse(jsonStr, content_type="application/json")


def login(request):
    """登录认证系统"""
    username = request.GET.get("username",'')
    password = request.GET.get("password",'')
    user = auth.authenticate(username=username, password=password)
    if not user==None and user.is_active:
        auth.login(request, user)
        return HttpResponse("已登录 user:%s"%(user))
    else:
        return HttpResponse("未登录")
