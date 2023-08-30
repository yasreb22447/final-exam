from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost, Products


def blogpost(request):
  mymembers = BlogPost.objects.all().values()
  template = loader.get_template('blogpost.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def products(request):
  pro = Products.objects.all().values()
  template = loader.get_template('Product_list.html')
  context = {
    'pro': pro,
  }
  return HttpResponse(template.render(context, request))