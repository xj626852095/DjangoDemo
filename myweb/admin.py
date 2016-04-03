#coding:utf-8
from django.contrib import admin

# Register your models here.

from myweb.models import Pushlish,Author,Book

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('email',)

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    #编辑表单字段顺序, 以及表单需要的字段
    #fields = ('title', 'author', 'publisher', 'publication_date',)
    #表单需要多选的字段 是选项垂直排列
    filter_horizontal = ('author',)
    #外键搜索
    raw_id_fields = ('publisher',)

admin.site.register(Pushlish)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)