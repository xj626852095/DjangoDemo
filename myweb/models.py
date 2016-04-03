#coding:utf-8
from django.db import models

# Create your models here.


class Pushlish(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField(verbose_name=u"网址")

    def __unicode__(self):
        return u"%s | %s | %s | %s | %s | %s"%(self.name,self.address,self.city,self.state_province,self.country,self.website)

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return  u"%s %s"%(self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Pushlish)
    publication_date = models.DateField()

