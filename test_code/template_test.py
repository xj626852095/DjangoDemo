#!/usr/bin/python
#coding:utf-8

"""
@function: 
@notice:
@author: xiangjie
@file: template_test.py
@time: 2016/3/12 21:07
"""

from django.conf import settings
from django import template
import os

#模板使用之前必须配置
settings.configure()

t = template.Template("""
    my name is {{name}},
    person：{{person.name}} {{person.age}}
    list: {{items.1}},
    {{noexist}}

    {% if person.name %}
        {{person.name}}存在
    {% else %}
        {{person.name}}不存在
    {% endif %}

    {% for item in items %}
        item: {{item}} {{forloop.counter}}
    {% empty %}
        items不存在
    {% endfor %}
""")
dict = {
    "name":"kevin",
    "person" : {
        "name" : "xiang",
        "age"  : 25
    },
    "items" : ["apples", "bananas"]

}
c = template.Context(dict)
result = t.render(c)
print type(result)
print result
