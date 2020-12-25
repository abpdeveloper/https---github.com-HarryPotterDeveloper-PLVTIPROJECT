import logging

from django.db.models import Q
from django.apps import apps
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.db import connection, migrations
from django.db.models import Avg, Count, Max, Min, ProtectedError, Q, Sum
from django.http import Http404, HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.utils import timezone
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, View
from rest_framework import generics
from django.contrib.auth import logout
from django.core.paginator import Paginator
from .forms import *
from .models import *

def categories_processor(request):
    error_list = []
    form = LoginForm(request.POST)
    if form.is_valid() and request.user.is_authenticated == False:
        cd = form.cleaned_data
        if User.objects.filter(username=cd['username']):
            if authenticate(username=cd['username'], password=cd['password']):
                user = authenticate(
                    username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('WebSite:login')
                    error_list.append('کاربر وارد شده غیر فعال می باشد.')
                    return render(request, 'index.html', {'form': form, 'error_list': error_list})
            error_list.append(' کلمه عبور وارد شده اشتباه می باشد.')
            return render(request, 'index.html', {'form': form, 'error_list': error_list})
        error_list.append(' نام کاربری وارد شده اشتباه می باشد.')
        return render(request, 'index.html', {'form': form, 'error_list': error_list})
    fehrests = productsgroups.objects.all()
    productsdetails = products.objects.all()
    brand = productsbrands.objects.all()
    result = products.objects.all()
    Cost1 = cost.objects.all()
    sliders = slider.objects.all()
    Latestproducts = products.objects.all().order_by('-id')[:1]
    newproducts = products.objects.all().order_by('-id')[:6]
    register = User.objects.all()
    banner = firstpagebaners.objects.all()
    SellBascket = sellbascket.objects.filter(Create_Uid=request.user.id).order_by('-id')
    sellbascketCount=sellbascket.objects.filter(Create_Uid=request.user.id).count()
    productdetailsDesc = productdetails.objects.filter(Create_Uid=request.user.id)
    #favoriteCount
    productdetailsDescCount = productdetails.objects.filter(Create_Uid=request.user.id,favorite=1).count()
    sumBascketPriceoff=0
    for p in sellbascket.objects.filter(Create_Uid=request.user.id):
            try:
                #print(cost.objects.get(pid_id=p.pid_id))
                sumBascketPriceoff+= cost.objects.get(pid_id=p.pid_id).priceoff*p.pcount
            except:
                continue
    sumFavoritePriceoff=0
    for p in productdetails.objects.filter(Create_Uid=request.user.id):
            try:
                #print(cost.objects.get(pid_id=p.pid_id))
                sumFavoritePriceoff+= cost.objects.get(pid_id=p.pid_id).priceoff
            except:
                continue
    return {'form': form,'error_list': error_list, 'fehrests': fehrests, 'productsdetails': productsdetails, 'brand': brand,
            'result': result, 'Cost': Cost1, 'sliders': sliders, 'newproducts': newproducts,
            'Latestproducts': Latestproducts, 'register': register,'SellBascket':SellBascket,
            'sellbascketCount':sellbascketCount,'sumBascketPriceoff':sumBascketPriceoff,
            'productdetailsDesc':productdetailsDesc,'productdetailsDescCount':productdetailsDescCount,
            'sumFavoritePriceoff':sumFavoritePriceoff, 'banner': banner}