#coding: utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime as dt
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import  json

"""
 一个视图就是Python的一个函数。这个函数第一个参数的类型是HttpRequest；它返回一个HttpResponse实例。
"""

def temp(request):
    """使用模板语言"""
    return render_to_response("temp_demo.html" , {"name":"kevin , this is my web"})

