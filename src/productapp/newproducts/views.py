# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
	print(request.user)
	print(args)
	return render(request,'home.html',{})

def contact_view(request,*args,**kwargs):
	return render(request,'contact.html',{})
def about_view(request,*args,**kwargs):
	context = {'myitems':{'1':"a","2":'b','c':'1'}}
	return render(request,'about.html',context)