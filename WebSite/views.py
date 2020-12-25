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
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.utils import timezone
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, View
from rest_framework import generics
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from .forms import *
from .models import *
from jalali_date import datetime2jalali, date2jalali
import random
import string
import requests
from zeep import Client
# Just For Logout Of WebSite.


def logout_view(request):
    logout(request)
    return redirect('WebSite:login')


forms = {'productsForm': productsForm, 'productsFormUpdate': productsFormUpdate, 'productsgroupsform': productsgroupsform, 'productsgroupsFormUpdate': productsgroupsFormUpdate, 'productsbrandsform': productsbrandsform,
         'productsbrandsUpdate': productsbrandsUpdate, 'costForm': costForm, 'costFormUpdate': costFormUpdate, 'userinfocreate': userinfocreate, 'userinfoupdate': userinfoupdate, 'formslidercreate': formslidercreate, 'formsliderupdate': formsliderupdate,
         'firstpagebanersform': firstpagebanersform, 'firstpagebanersFormUpdate': firstpagebanersFormUpdate, 'aboutusForm': aboutusForm, 'aboutusFormUpdate': aboutusFormUpdate, 'centercontactusForm': centercontactusForm, 'centercontactusFormUpdate': centercontactusFormUpdate,
         'salecontactusForm': salecontactusForm, 'salecontactusFormUpdate': salecontactusFormUpdate, 'customerquestionsForm': customerquestionsForm, 'customerquestionsFormUpdate': customerquestionsFormUpdate, 'aboutusp1Form': aboutusp1Form, 'aboutusp1FormUpdate': aboutusp1FormUpdate,
         'firstpagehlform': firstpagehlform, 'firstpagehlUpdate': firstpagehlUpdate, 'ersalform': ersalform, 'osoolform': osoolform, 'osoolformupdate': osoolformupdate, 'ersalformupdate': ersalformupdate, 'lastnewsform': lastnewsform, 'lastnewsformupdate': lastnewsformupdate,
         'parametsaccountsform': parametsaccountsform, 'parametsaccountsformupdate': parametsaccountsformupdate, 'parametssasform': parametssasform, 'parametssasformupdate': parametssasformupdate, 'parametssupportform': parametssupportform, 'parametssupportformupdate': parametssupportformupdate, 'productscategoryform': productscategoryform, 'productscategoryformupdate': productscategoryformupdate, 'insideslidercreate': insideslidercreate, 'insidesliderupdate': insidesliderupdate, 'weblogform': weblogform, 'weblogformupdate': weblogformupdate}

# # Create your views here.

# Creat For All Views
# @login_required(login_url='login')

@login_required(login_url='login')
@permission_required('User.can_read_private_section')
def create(request, ModelName, form_name, redirect_path, html_name, context_name):
    error = []
    cerror = []
    form = forms[form_name]
    model = apps.get_model('WebSite', ModelName)
    Create_Uid = request.user.id
    Update_Uid = request.user.id
    costpid = request.POST.get('pid')
    brandid = request.POST.get('brand')
    checkcostpid = cost.objects.all().filter(pid=costpid)
    brandname = request.POST.get('name')
    checkbrandname = productsbrands.objects.all().filter(name=brandname)
    productname = request.POST.get('name')
    productserial = request.POST.get('serial')
    productgroup = request.POST.get('group')
    cname = request.POST.get('cname')
    checkcname = productscategory.objects.filter(cname=cname)
    cname1 = request.POST.get('cname1')
    cname2 = request.POST.get('cname2')
    cname3 = request.POST.get('cname3')
    checkproductname = products.objects.filter(
        Q(name=productname),  Q(group=productgroup))
    checkproductserial = products.objects.filter(
        Q(serial=productserial), Q(group=productgroup))
    productgroups = request.POST.get('Group_Name')
    checkproductgroups = productsgroups.objects.all().filter(Group_Name=productgroups)
    print('step1')
    if request.method == 'POST':
        print('step2')
        if (cname1 and (cname1 == cname2 or cname1 == cname3) or (cname2 and cname2 == cname3)):
            print('step3', cname1, cname2, cname3)
            cerror.append(
                ' توجه : کابر گرامی دسته بندی های انتخاب شده نباید یکسان باشند .'
            )
            context = form(request.POST)
            return render(request, '{}.html'.format(html_name), {'{}'.format(context_name): context, 'cerror': cerror})
        if checkcname:
            print('step4')
            error.append(
                'توجه : کاربر گرامی نام دسته بندی انتخاب شده تکراری می باشد .')
            context = form(request.POST)
            return render(request, '{}.html'.format(html_name), {'{}'.format(context_name): context, 'error': error})
        if checkproductname:
            print('step5')
            error.append(
                'توجه : کاربر گرامی نام محصول انتخاب شده در گروه جاری تکراری می باشد .')
            context = form(request.POST)
            return render(request, '{}.html'.format(html_name), {'{}'.format(context_name): context, 'error': error})
        if checkproductserial:
            print('step6')
            error.append(
                'توجه : کاربر گرامی سریال محصول انتخاب شده در گروه جاری می باشد .')
            context = form(request.POST)
            return render(request, '{}.html'.format(html_name), {'{}'.format(context_name): context, 'error': error})
        if checkproductgroups:
            print('step7')
            error.append(
                'توجه : کاربر گرامی نام گروه وارد شده تکراری می باشد .')
            context = form(request.POST)
            return render(request, '{}.html'.format(html_name), {'{}'.format(context_name): context, 'error': error})

        context = form(request.POST, request.FILES)
        if context.is_valid():
            print('step8(validation)')
            context.save()
            print('step9(save)')
            model.objects.filter(id=model.objects.latest('id').id).update(
                Create_Uid=Create_Uid, Update_Uid=Update_Uid)
            if ModelName == 'productsgroups':
                print('step10')
                with connection.cursor() as cursor:
                    cursor.execute(u"update  productsgroups set glevel=1 where gparentid=0 update  productsgroups set glevel=2 where gparentid in (select id from productsgroups where gparentid=0) update  productsgroups set glevel=3 where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0))")
            return redirect('WebSite:{}'.format(redirect_path))
    context = form(request.POST)
    groups = productsgroups.objects.all()
    return render(request, '{}.html'.format(html_name), {'{}'.format(context_name): context, 'groups': groups})


# Update For All Views
# @login_required(login_url='login')
@login_required(login_url='login')
@permission_required('User.can_read_private_section')
def update(request, ModelName, form_name, redirect_path, html_name, context_name, id):
    form = forms[form_name]
    model = apps.get_model('WebSite', ModelName)
    #product = model.objects.filter(id=id)
    ins_obj = get_object_or_404(model, pk=int(id))
    ins_obj2 = model.objects.filter(id=id)
    groups = productsgroups.objects.all()
    Customerslist = Customers.objects.all()
    categoryproduct = productsgroups.objects.filter(id=0)
    category = productscategory.objects.all()
    if ModelName == 'products':
        categoryproduct = productsgroups.objects.filter(
            id=ins_obj2[0].group_id)
    context = form(request.POST, request.FILES, instance=ins_obj)
    if request.method == 'POST':
        if context.is_valid():
            context.save()
            return redirect('WebSite:{}'.format(redirect_path))
    context = form(instance=ins_obj)
    # for a in ins_obj2:
    return render(request, '{}.html'.format(html_name), {'{}'.format(context_name): context, 'ins_obj2': ins_obj2, 'groups': groups, 'categoryproduct': categoryproduct, 'category': category,'Customerslist':Customerslist})


# Delete For All Views
# @login_required(login_url='login')
@login_required(login_url='login')
@permission_required('User.can_read_private_section')
def delete(request, ModelName, redirect_path, id):
    model = apps.get_model('WebSite', ModelName)
    to_delete = get_object_or_404(model, pk=int(id))
    to_delete.delete()
    return redirect('WebSite:{}'.format(redirect_path))


@login_required(login_url='login')
@permission_required('User.can_read_private_section')
def create_user(request):
    error = []
    checkusername = request.POST.get('username')
    if request.method == 'POST':
        Users = userinfocreate(request.POST, request.FILES)
        if User.objects.filter(username=checkusername):
            listUsers = User.objects.all()
            error.append(
                'توجه : کاربر گرامی نام کاربری {} تکراری می باشد .'.format(checkusername))
            return render(request, 'users_create.html',
                          {'Users': Users, 'listUsers': listUsers, 'error': error})
        if Users.is_valid():
            user = Users.save()
            user.set_password(user.password)
            user.save()
            return redirect('WebSite:usersreport')
    listUsers = User.objects.all()
    Users = userinfocreate(request.POST)
    Customerslist = Customers.objects.all()
    return render(request, 'users_create.html',
                  {'Users': Users, 'listUsers': listUsers,'Customerslist':Customerslist})


# user_update
@login_required(login_url='login')
@permission_required('User.can_read_private_section')
def update_user(request, id):
    error = []
    edit_user = get_object_or_404(User, pk=id)
    Customerslist = Customers.objects.all()
    userinfo=User.objects.filter(id=id)
    Users = userupdate(request.POST, request.FILES, instance=edit_user)
    customersid = request.POST.get('customersid', '')
    print('step 1 '+customersid)
    if request.method == 'POST':
        print('step 2')
        if Users.is_valid():
            print('step 3')
            Users.save()
            User.objects.filter(id=id).update(customersid=customersid)
      
            print('step 4')
            return redirect('WebSite:usersreport')
    Users = userinfoupdate(instance=edit_user)
    print('step 5')
    return render(request, 'users_update.html', {'Users': Users, 'error': error,'Customerslist':Customerslist,'userinfo':userinfo})


@login_required(login_url='login')
@permission_required('User.can_read_private_section')
def Delete_User(request, id):
    User_to_delete = get_object_or_404(User, pk=int(id))
    User_to_delete.delete()
    return redirect('WebSite:usersreport')


@login_required(login_url='login')
@permission_required('User.can_read_private_section')
def DeleteRecords(request, list_ids, ModelName, RedirectPath):
    error = []
    deletelist = []
    try:
        model = apps.get_model('WebSite', ModelName)
    except:
        model = apps.get_model('auth', ModelName)
    l = list_ids.split(" ")
    counter = 0
    for ids in l:
        if len(ids) > 0:
            ModelName_delete = get_object_or_404(model, id=ids)
            try:
                ModelName_delete.delete()
                counter = counter + 1
                deletelist.append(ids)
            except ProtectedError:
                error.append(ids)
    return render(request, '{}.html'.format(RedirectPath), {
        '{}'.format(RedirectPath): model.objects.all(),
        'error': error,
        'deletelist': deletelist
    })


@login_required(login_url='login')
@permission_required('User.can_read_private_section')
def ChangePassword_AdminView(request, id):
    error = []
    report = []
    newpass1 = request.POST.get('newpass')
    newpass2 = request.POST.get('password')
    if request.method == 'POST':
        if newpass1 == newpass2:
            User.objects.filter(id=id).update(password=make_password(newpass2))
            report.append(
                'توجه : کاربر گرامی کلمه عبور با موفقیت تغییر یافت .')
            if request.user.id == id:
                user = authenticate(
                    username=request.user.username, password=newpass2)
                if user is not None:
                    login(request, user)
            return render(request, 'AdminChangePassword.html', {'report': report})
        error.append(
            'توجه : کاربر گرامی کلمه های عبور وارد شده یکسان نمی باشد .')
        return render(request, 'AdminChangePassword.html', {'error': error})
    return render(request, 'AdminChangePassword.html', {})


@login_required(login_url='login')
def ChangePassword_UserView(request):
    error = []
    report = []
    newpass1 = request.POST.get('newpass')
    newpass2 = request.POST.get('password')
    oldpassword = request.POST.get('oldpassword')
    user = User.objects.get(id=request.user.id)
    user_id = request.user.id
    if request.method == 'POST':
        if user.check_password(oldpassword):
            if newpass1 == newpass2:
                User.objects.filter(id=user_id).update(
                    password=make_password(newpass2))
                report.append(
                    'توجه : کاربر گرامی کلمه عبور با موفقیت تغییر یافت .')
                user = authenticate(
                    username=request.user.username, password=newpass2)
                if user is not None:
                    login(request, user)
                return render(request, 'AUserChangePassword.html', {'report': report})
            error.append(
                'توجه : کاربر گرامی کلمه های عبور وارد شده یکسان نمی باشد .')
            return render(request, 'AUserChangePassword.html', {'error': error})
        error.append('توجه : کاربر گرامی کلمه عبور فعلی صحیح نمی باشد .')
        return render(request, 'AUserChangePassword.html', {'error': error})
    return render(request, 'AUserChangePassword.html', {})


def customersquestions_create(request):
    Create_Uid = request.user.id
    Update_Uid = request.user.id
    if request.method == 'POST':
        cq = customerquestionsForm(request.POST, request.FILES)
        if cq.is_valid():
            cq.save()
            customerquestions.objects.filter(id=customerquestions.objects.latest(
                'id').id).update(Create_Uid=Create_Uid, Update_Uid=Update_Uid)
            return redirect('WebSite:contact')
    cq = customerquestionsForm(request.POST)
    fcontact = centercontactus.objects.all()
    uccontactus = centercontactus.objects.all()
    uscontactus = salecontactus.objects.all()
    spg = productsgroups.objects.filter(gparentid=0).order_by('id')[:7]
    spgid = list(productsgroups.objects.filter(
        gparentid=0).values_list('id', flat=True))
    spgt = productsgroups.objects.all()
    spgtr = productsgroups.objects.raw(
        'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
    spgtr2 = productsgroups.objects.raw(
        'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
    fhlogo = firstpagelogo.objects.all()
    return render(request, 'contact.html', {'fcontact': fcontact, 'cq': cq, 'uccontactus': uccontactus, 'uscontactus': uscontactus, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2, 'fhlogo': fhlogo})


class useraboutreportview(generic.ListView):
    model = aboutus
    context_object_name = 'about'
    template_name = 'about-2.html'
    queryset = aboutus.objects.all()

    def get_context_data(self, **kwargs):
        context = super(useraboutreportview, self).get_context_data(**kwargs)
        context['fcontact'] = centercontactus.objects.all()
        context['aboutusteam'] = aboutusp1.objects.all()
        context['aboutbrand'] = productsbrands.objects.all()
        context['form'] = User.objects.all()
        context['fhlogo'] = firstpagelogo.objects.all()
        context['spg'] = productsgroups.objects.filter(
            gparentid=0).order_by('id')[:9]
        context['spgid'] = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        context['spgt'] = productsgroups.objects.all()
        context['spgtr'] = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        context['spgtr2'] = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')

        return context


class showproductlist(generic.ListView):
    models = products
    context_object_name = 'productslist'
    template_name = 'products-category-boxed.html'

    def get(self, request, id):
        fehrests = productsgroups.objects.all()
        productslist = products.objects.all().filter(group=id)
        Cost = cost.objects.all()
        fhlogo = firstpagelogo.objects.all()
        return render(request, 'products-category-boxed.html', {'fhlogo': fhlogo, 'productslist': productslist, 'fehrests': fehrests, 'Cost': Cost})


class showproduct(generic.ListView):
    models = products
    context_object_name = 'showproduct'
    template_name = 'products.html'

    def get(self, request, id):
        fehrests = productsgroups.objects.all()

        a = ''
        replacedesc = products.objects.filter(id=id).values_list('desc')
        for b in replacedesc:
            a = b
        c = str(a)
        truedesc = c.replace('.', '<br/>')

        showproduct = products.objects.all().filter(id=id)
        gid = products.objects.all().values_list('group', flat=True).filter(id=id)
        groupproducts = products.objects.all().filter(group=gid[0])
        aboutproduct = products.objects.all().filter(id=id)
        technicalinfo = products.objects.all().filter(id=id)
        Cost = cost.objects.all()
        SellBascket = sellbascket.objects.filter(
            Create_Uid=request.user.id).order_by('-id')
        productsdetails = products.objects.all()
        sellbascketCount = sellbascket.objects.filter(
            Create_Uid=request.user.id).count()
        productdetailsDesc = productdetails.objects.filter(
            Create_Uid=request.user.id)
        spg = productsgroups.objects.filter(gparentid=0).order_by('id')[:9]
        spgid = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        spgt = productsgroups.objects.all()
        spgtr = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        spgtr2 = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        fhlogo = firstpagelogo.objects.all()
        # favoriteCount
        productdetailsDescCount = productdetails.objects.filter(
            Create_Uid=request.user.id, favorite=1).count()
        maxsale = cost.objects.values(
            'pid', 'priceorg').annotate(countpid=Count('pid'))
        sumBascketPriceoff = 0
        for p in sellbascket.objects.filter(Create_Uid=request.user.id):
            try:
                sumBascketPriceoff += cost.objects.get(
                    pid_id=p.pid_id).priceoff*p.pcount
            except:
                continue
        sumFavoritePriceoff = 0
        for p in productdetails.objects.filter(Create_Uid=request.user.id):
            try:
                sumFavoritePriceoff += cost.objects.get(
                    pid_id=p.pid_id).priceoff
            except:
                continue
        Comments = comment.objects.filter(pid_id=id, status=1)
        CommentCount = comment.objects.filter(pid_id=id, status=1).count()
        Users = User.objects.all()
        fcontact = centercontactus.objects.all()
        return render(request, 'products.html', {'truedesc': truedesc, 'fcontact': fcontact, 'technicalinfo': technicalinfo, 'aboutproduct': aboutproduct, 'showproduct': showproduct, 'fehrests': fehrests, 'Cost': Cost, 'groupproducts': groupproducts, 'SellBascket': SellBascket,
                                                 'sellbascketCount': sellbascketCount, 'sumBascketPriceoff': sumBascketPriceoff,
                                                 'productdetailsDesc': productdetailsDesc, 'productdetailsDescCount': productdetailsDescCount,
                                                 'sumFavoritePriceoff': sumFavoritePriceoff, 'productsdetails': productsdetails, 'Comments': Comments, 'CommentCount': CommentCount, 'Users': Users, 'id': id, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2, 'fhlogo': fhlogo})


class salebacket(generic.ListView):
    models = sellbascket
    context_object_name = 'sellbascket'
    template_name = 'cart.html'

    def get(self, request):
        userid = request.user.id
        user_info = User.objects.filter(id=userid)
        fehrests = productsgroups.objects.all()
        fhlogo = firstpagelogo.objects.all()
        sb = sellbascket.objects.all().filter(status=0, Create_Uid=userid)
        psb = products.objects.all()
        CostLV = cost.objects.all()
        spg = productsgroups.objects.filter(gparentid=0).order_by('id')[:9]
        spgid = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        spgt = productsgroups.objects.all()
        spgtr = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        spgtr2 = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        sumBascketPriceoff = 0
        for p in sellbascket.objects.filter(Create_Uid=request.user.id):
            try:
                sumBascketPriceoff += cost.objects.get(
                    pid_id=p.pid_id).priceoff*p.pcount
            except:
                continue
        return render(request, 'cart.html', {'user_info': user_info, 'fhlogo': fhlogo, 'sb': sb, 'fehrests': fehrests, 'psb': psb, 'CostLV': CostLV, 'sumBascketPriceoff': sumBascketPriceoff, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2})


@login_required(login_url='login')
def send_request(request):
    sumBascketPriceoff = 0
    for p in sellbascket.objects.filter(Create_Uid=request.user.id):
        try:
            sumBascketPriceoff += cost.objects.get(
                pid_id=p.pid_id).priceoff*p.pcount
        except:
            continue
    amount = sumBascketPriceoff
    email = request.user.email
    mobile = request.user.cellphone
    CallbackURL = 'http://localhost:8000/verify/' # Important: need to edit for realy server.
    description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
    MERCHANT = '39d8f7d2-51e6-11e9-a3e3-000c29344814'
    client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))

@login_required(login_url='login')
def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
class salebacketcheckout(View):
    models = finalcheckout

    def get(self, request):
        userid = request.user.username
        fhlogo = firstpagelogo.objects.all()
        sb = sellbascket.objects.all().filter(status=1)
        psb = products.objects.all()
        spg = productsgroups.objects.filter(gparentid=0).order_by('id')[:9]
        spgid = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        spgt = productsgroups.objects.all()
        userid = self.request.user.id
        UserInfo = User.objects.all().filter(id=userid)
        spgtr = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        spgtr2 = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        sumBascketPriceoff = 0
        for p in sellbascket.objects.filter(Create_Uid=request.user.id):
            try:
                sumBascketPriceoff += cost.objects.get(
                    pid_id=p.pid_id).priceoff*p.pcount
            except:
                continue
        return render(request, 'adminorderlist.html', {'UserInfo': UserInfo, 'fhlogo': fhlogo, 'sb': sb,  'psb': psb,  'sumBascketPriceoff': sumBascketPriceoff, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2})


class finalcheckout(generic.ListView):
    models = finalcheckout
    context_object_name = 'fc'
    template_name = 'fc.html'
    queryset = finalcheckout.objects.all()


class wishlist(generic.ListView):
    models = productdetails
    context_object_name = 'wishlist'
    template_name = 'wishlist.html'

    def get(self, request):
        userid = request.user.id
        fehrests = productsgroups.objects.all()
        sb = productdetails.objects.all().filter(Create_Uid=userid)
        psb = products.objects.all()
        sumBascketPriceoff = 0
        productdetailsDescCount = productdetails.objects.filter(
            Create_Uid=request.user.id, favorite=1).count()
        sumBascketPriceoff = 0
        for p in sellbascket.objects.filter(Create_Uid=request.user.id):
            try:
                sumBascketPriceoff += cost.objects.get(
                    pid_id=p.pid_id).priceoff*p.pcount
            except:
                continue
        sumFavoritePriceoff = 0
        for p in productdetails.objects.filter(Create_Uid=request.user.id):
            try:
                sumFavoritePriceoff += cost.objects.get(
                    pid_id=p.pid_id).priceoff
            except:
                continue
        return render(request, 'wishlist.html', {'sb': sb, 'fehrests': fehrests, 'psb': psb, })


# Login
def loginuser(request):
    spg = productsgroups.objects.filter(gparentid=0).order_by('id')[:9]
    spgid = list(productsgroups.objects.filter(
        gparentid=0).values_list('id', flat=True))
    spgt = productsgroups.objects.all()
    spgtr = productsgroups.objects.raw(
        'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
    spgtr2 = productsgroups.objects.raw(
        'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
    fcontact = centercontactus.objects.all()
    bankreport = parametsaccounts.objects.all()
    fehrests = productsgroups.objects.all()
    productsdetails = products.objects.all()
    brand = productsbrands.objects.all()
    result = products.objects.all()
    Cost1 = cost.objects.all()
    sliders = slider.objects.all()
    Latestproducts = products.objects.all().order_by('-id')[:6]

    ng = products.objects.all()
    salecount = sellbascket.objects.all().filter(status=0).values_list('pid_id', flat=True)
    if salecount:
        for count in salecount:
            if count:
                salescount = sellbascket.objects.filter(pid_id=count).aggregate(Sum=Sum('pcount'))['Sum']
                numberofgoods = products.objects.get(id=count).numberofgoods
            if (numberofgoods - salescount) < 0:
                zero = numberofgoods - salescount       
    else:
        zero = 1

            

    newproducts = products.objects.all().order_by('-id')[:6]
    register = User.objects.all()
    banner = firstpagebaners.objects.all()
    SellBascket = sellbascket.objects.filter(
        Create_Uid=request.user.id).order_by('-id')
    sellbascketCount = sellbascket.objects.filter(
        Create_Uid=request.user.id).count()
    productdetailsDesc = productdetails.objects.filter(
        Create_Uid=request.user.id)
    productgrouppage = productsgroups.objects.all()
    subslidergroup = productsgroups.objects.all().filter(
        gparentid=0).order_by('id')[:4]
    khabar = lastnews.objects.all().order_by('-id')[:3]
    fhlogo = firstpagelogo.objects.all().order_by('-id')[:1]
    bestssale = sellbascket.objects.raw("select top(6) a.pid_id as id,sum(a.pcount) as count ,case when b.goods<>0 then b.numberofgoods-(select SUM(sb.pcount) from sellbascket sb where sb.pid_id=a.pid_id and sb.status=0) else 0 end as existing ,b.img1,b.name,(select c.Group_Name from productsgroups c where c.id=b.group_id) as groupname ,(select name from productsbrands where id=b.brand_id) as brand from sellbascket a join products b on a.pid_id=b.id group by pid_id ,b.img1,b.name,b.group_id,b.brand_id, b.goods,b.numberofgoods order by sum(a.pcount) desc")
    # favoriteCount
    productdetailsDescCount = productdetails.objects.filter(
        Create_Uid=request.user.id, favorite=1).count()
    sumBascketPriceoff = 0
    for p in sellbascket.objects.filter(Create_Uid=request.user.id):
        try:
            sumBascketPriceoff += cost.objects.get(
                pid_id=p.pid_id).priceoff*p.pcount
        except:
            continue
    sumFavoritePriceoff = 0
    for p in productdetails.objects.filter(Create_Uid=request.user.id):
        try:
            sumFavoritePriceoff += cost.objects.get(pid_id=p.pid_id).priceoff
        except:
            continue
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
                    return render(request, 'index.html', {'zero': zero, 'ng': ng,'error_list': error_list, 'bankreport': bankreport, 'fcontact': fcontact, 'form': form, 'error_list': error_list,
                                                          'fehrests': fehrests, 'productsdetails': productsdetails, 'brand': brand,
                                                          'result': result, 'Cost': Cost1, 'sliders': sliders, 'newproducts': newproducts,
                                                          'Latestproducts': Latestproducts, 'register': register, 'SellBascket': SellBascket,
                                                          'sellbascketCount': sellbascketCount, 'sumBascketPriceoff': sumBascketPriceoff,
                                                          'productdetailsDesc': productdetailsDesc, 'productdetailsDescCount': productdetailsDescCount,
                                                          'sumFavoritePriceoff': sumFavoritePriceoff, 'banner': banner, 'bestssale': bestssale,
                                                          'productgrouppage': productgrouppage, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2,
                                                          'fhlogo': fhlogo, 'subslidergroup': subslidergroup, 'khabar': khabar})
            error_list.append(' کلمه عبور وارد شده اشتباه می باشد.')
            return render(request, 'index.html', {'zero': zero, 'ng': ng,'error_list': error_list, 'bankreport': bankreport, 'fcontact': fcontact, 'form': form, 'error_list': error_list,
                                                  'fehrests': fehrests, 'productsdetails': productsdetails, 'brand': brand,
                                                  'result': result, 'Cost': Cost1, 'sliders': sliders, 'newproducts': newproducts,
                                                  'Latestproducts': Latestproducts, 'register': register, 'SellBascket': SellBascket,
                                                  'sellbascketCount': sellbascketCount, 'sumBascketPriceoff': sumBascketPriceoff,
                                                  'productdetailsDesc': productdetailsDesc, 'productdetailsDescCount': productdetailsDescCount,
                                                  'sumFavoritePriceoff': sumFavoritePriceoff, 'banner': banner, 'bestssale': bestssale,
                                                  'productgrouppage': productgrouppage, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2,
                                                  'fhlogo': fhlogo, 'subslidergroup': subslidergroup, 'khabar': khabar})
        error_list.append(' نام کاربری وارد شده اشتباه می باشد.')
        return render(request, 'index.html', {'zero': zero, 'ng': ng,'error_list': error_list, 'bankreport': bankreport, 'fcontact': fcontact, 'form': form, 'error_list': error_list,
                                              'fehrests': fehrests, 'productsdetails': productsdetails, 'brand': brand,
                                              'result': result, 'Cost': Cost1, 'sliders': sliders, 'newproducts': newproducts,
                                              'Latestproducts': Latestproducts, 'register': register, 'SellBascket': SellBascket,
                                              'sellbascketCount': sellbascketCount, 'sumBascketPriceoff': sumBascketPriceoff,
                                              'productdetailsDesc': productdetailsDesc, 'productdetailsDescCount': productdetailsDescCount,
                                              'sumFavoritePriceoff': sumFavoritePriceoff, 'banner': banner, 'bestssale': bestssale,
                                              'productgrouppage': productgrouppage, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2,
                                              'fhlogo': fhlogo, 'subslidergroup': subslidergroup, 'khabar': khabar})
 
    return render(request, 'index.html', {'zero': zero, 'ng': ng,'bankreport': bankreport, 'fcontact': fcontact, 'form': form, 'error_list': error_list,
                                          'fehrests': fehrests, 'productsdetails': productsdetails, 'brand': brand,
                                          'result': result, 'Cost': Cost1, 'sliders': sliders, 'newproducts': newproducts,
                                          'Latestproducts': Latestproducts, 'register': register, 'SellBascket': SellBascket,
                                          'sellbascketCount': sellbascketCount, 'sumBascketPriceoff': sumBascketPriceoff,
                                          'productdetailsDesc': productdetailsDesc, 'productdetailsDescCount': productdetailsDescCount,
                                          'sumFavoritePriceoff': sumFavoritePriceoff, 'banner': banner, 'bestssale': bestssale,
                                          'productgrouppage': productgrouppage, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2,
                                          'fhlogo': fhlogo, 'subslidergroup': subslidergroup, 'khabar': khabar})


class firstpageheaderlogo(generic.ListView):
    model = firstpagelogo
    context_object_name = 'fhlogo'
    template_name = 'index.html'
    queryset = firstpagelogo.objects.all()


class khabarLV(generic.ListView):
    model = firstpagelogo
    context_object_name = 'khabar'
    template_name = 'khabar.html'
    queryset = lastnews.objects.all()

    def get_context_data(self, **kuargs):
        context = super(khabarLV, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class khabarmasterpage(generic.ListView):
    model = firstpagelogo
    context_object_name = 'khabarmastepage'
    template_name = 'khabarmastepage.html'
    queryset = lastnews.objects.all()


class subgroupheader(generic.ListView):
    model = productsgroups

    def get(self, request):
        spg = productsgroups.objects.filter(gparentid=0).order_by('id')[:9]
        spgid = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        spgt = productsgroups.objects.all()
        spgtr = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        spgtr2 = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        return render(request, 'partials/firstpageheader.html', {'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2})


class treeshowgroup(View):
    models = productsgroups

    def get(self, request, id):
        x = id
        pg = productsgroups.objects.filter(gparentid=x)
        # pg2 = productsgroups.objects.filter(id=productsgroups.objects.filter(gparentid=x))
        prd = products.objects.filter(group_id=x)
        fhlogo = firstpagelogo.objects.all()
        spg = productsgroups.objects.filter(gparentid=0).order_by('id')[:9]
        spgid = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        spgt = productsgroups.objects.all()
        spgtr = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        spgtr2 = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        return render(request, 'product-category-boxed.html', {'fhlogo': fhlogo, 'pg': pg, 'prd': prd, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2})


def treeshowgroupcreate(request, id):
    if request.method == 'POST':
        group_report = productsgroupsform(request.POST, request.FILES)
        if group_report.is_valid():
            group_report.save()
            productsgroups.objects.filter(
                id=productsgroups.objects.latest('id').id).update(gparentid=id)
            with connection.cursor() as cursor:
                cursor.execute(u"update  productsgroups set glevel=1 where gparentid=0 update  productsgroups set glevel=2 where gparentid in (select id from productsgroups where gparentid=0) update  productsgroups set glevel=3 where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0))")
            return redirect('WebSite:productsgroupsLV')
    group_report = productsgroupsform(request.POST)
    return render(request, 'productsgroups_create.html', {'group_report': group_report})


def register(request):
    print("start register ...!")
    with connection.cursor() as cursor:
        cursor.execute(
            u"if not exists(select * from [Customers] where id=0) begin set identity_insert [Customers] on insert into [PLVTIProject].[dbo].[Customers]( [id],[Name],[Family],[Address],[CSex],[CellPhone],[EcCode],[Email],[FAccId])values( 0,0,0,0,0,0,0,0,0) set identity_insert [Customers] off end")
    registererror = []
    spg = productsgroups.objects.filter(gparentid=0).order_by('id')[:9]
    spgid = list(productsgroups.objects.filter(
        gparentid=0).values_list('id', flat=True))
    spgt = productsgroups.objects.all()
    spgtr = productsgroups.objects.raw(
        'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
    spgtr2 = productsgroups.objects.raw(
        'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
    fcontact = centercontactus.objects.all()
    fhlogo = firstpagelogo.objects.all().order_by('-id')[:1]
    khabar = lastnews.objects.all().order_by('-id')[:3]
    checkusername = request.POST.get('username')
    chellphonecheck = request.POST.get('cellphone')
    if request.method == 'POST':
        register = RegisterFormClean(request.POST)
        if User.objects.all().filter(username=checkusername):
            registererror.append(
                'توجه : نام کاربری وارد شده تکراری می باشد.')
            return render(request, 'index.html', {'khabar': khabar, 'fcontact': fcontact,'fhlogo': fhlogo, 'register': register, 'registererror': registererror, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2})
        if User.objects.all().filter(cellphone=chellphonecheck):
            registererror.append(
                'توجه : شماره تلفن همراه وارد شده تکراری می باشد.')
            return render(request, 'index.html', {'khabar': khabar, 'fcontact': fcontact,'fhlogo': fhlogo, 'register': register, 'registererror': registererror, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2})
        if register.is_valid():
            user = register.save()
            newpass = createpass(chellphonecheck)
            user.set_password(newpass)
            user.save()
            User.objects.filter(id=User.objects.order_by(
                '-id')[:1]).update(customersid=0)
            print("Hi!")
            return redirect('WebSite:login')
        else:
            print("validation error")
    register = RegisterFormClean(request.POST)
    return render(request, 'index.html', {'khabar': khabar,'fcontact': fcontact,'fhlogo': fhlogo, 'register': register, 'registererror': registererror, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2})


def registermobile(request):
    mregistererror = []
    mform = LoginFormmobile(request.POST)
    spg = productsgroups.objects.filter(gparentid=0).order_by('id')
    spgid = list(productsgroups.objects.filter(gparentid=0).values_list('id', flat=True))
    spgt = productsgroups.objects.all()
    spgtr = productsgroups.objects.raw(
        'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
    spgtr2 = productsgroups.objects.raw(
        'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
    fcontact = centercontactus.objects.all()
    fhlogo = firstpagelogo.objects.all().order_by('-id')[:1]
    khabar = lastnews.objects.all().order_by('-id')[:3]
    checkusername = request.POST.get('username')
    chellphonecheck = request.POST.get('cellphone')
    print('step 1')
    if request.method == 'POST':
        print('step 2')
        mregister = RegistermobileFormClean(request.POST)
        if User.objects.all().filter(username=checkusername):
            mregistererror.append(
                'توجه : نام کاربری وارد شده تکراری می باشد.')
            return render(request, 'login.html', {'khabar': khabar, 'fcontact': fcontact,'fhlogo': fhlogo, 'mregister': mregister, 'mregistererror': mregistererror,'mform':mform, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2})
        if User.objects.all().filter(cellphone=chellphonecheck):
            print('step 3')
            mregistererror.append(
                'توجه : شماره تلفن همراه وارد شده تکراری می باشد.')
            return render(request, 'login.html', {'khabar': khabar, 'fcontact': fcontact,'fhlogo': fhlogo,'mregister': mregister, 'mregistererror': mregistererror,'mform':mform, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2})
        print('step 4')
        if mregister.is_valid():
            print('step 5: validation')
            user = mregister.save()
            newpass = createpass(chellphonecheck)
            user.set_password(newpass)
            user.save()
            print('step 6:HI !')
            return redirect('WebSite:login')
    print('step 7')
    mregister = RegistermobileFormClean(request.POST)
    return render(request, 'login.html', {'khabar': khabar,'fcontact': fcontact,'fhlogo': fhlogo,'mregister': mregister,'mform':mform, 'mregistererror': mregistererror, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2})


def createpass(phone):
    url = "http://RestfulSms.com/api/Token?"

    payload = "{\r\n  \"UserApiKey\": \"b3039ef2668d9207a1ffa89d\",\r\n  \"SecretKey\": \"123Albas456\"\r\n}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text.encode('utf8'))
    token = response.json()["TokenKey"]
    # print(response.json()["TokenKey"])
    #####################################################

    # url = "http://RestfulSms.com/api/MessageSend"
    url = "http://RestfulSms.com/api/VerificationCode"
    letters = string.digits
    result_str = ''.join(random.choice(letters) for i in range(6))
    print("Random string of length", '6', "is:", result_str)

    # payload = "{\r\n  \"Messages\":[\""+result_str+"\"],\r\n  \"MobileNumbers\": [\""+phone +"\"],\r\n  \"LineNumber\": \"3000462277\",\r\n  \"SendDateTime\": \"\",\r\n  \"CanContinueInCaseOfError\": \"false\"\r\n}"

    payload = "{\r\n   \"Code\": \""+result_str+"\",\r\n   \"MobileNumber\": \""+phone +"\"\r\n} "

    headers = {
        'Content-Type': 'application/json',
        'x-sms-ir-secure-token': '{}'.format(token)
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
    return result_str


# Login


def loginusermobile(request):
    merror_list = []
    x = 0
    mform = LoginFormmobile(request.POST)
    if mform.is_valid() and request.user.is_authenticated == False:
        mcd = mform.cleaned_data
        if User.objects.filter(username=mcd['username']):
            if authenticate(username=mcd['username'], password=mcd['password']):
                user = authenticate(
                    username=mcd['username'], password=mcd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('WebSite:login')
                    merror_list.append('کاربر وارد شده غیر فعال می باشد.')
                    return render(request, 'login.html', {'mform': mform, 'merror_list': merror_list})
            merror_list.append(' کلمه عبور وارد شده اشتباه می باشد.')
            return render(request, 'login.html', {'mform': mform, 'merror_list': merror_list})
        merror_list.append(' نام کاربری وارد شده اشتباه می باشد.')
        return render(request, 'login.html', {'mform': mform, 'merror_list': merror_list})
    mfehrests = productsgroups.objects.all()
    return render(request, 'login.html', {'x': x, 'mform': mform, 'merror_list': merror_list, 'mfehrests': mfehrests})


def productscategoryparent(request, id):
    if request.method == 'POST':
        pcategory = productscategoryform(request.POST, request.FILES)
        if pcategory.is_valid():
            pcategory.save()
            productscategory.objects.filter(
                id=productscategory.objects.latest('id').id).update(cparentid=id)
            return redirect('WebSite:productscategoryLV')
    pcategory = productscategoryform(request.POST)
    return render(request, 'productscategory_create.html', {'pcategory': pcategory})


class productscategoryview(generic.ListView):
    model = productscategory
    context_object_name = 'productscategory'
    template_name = 'productscategoryLV.html'
    queryset = productscategory.objects.all()

    def get_context_data(self, **kuargs):
        context = super(productscategoryview, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class allproducts(generic.ListView):
    model = products
    context_object_name = 'Allproducts'
    template_name = 'category-boxed.html'
    queryset = products.objects.all()

    def get_context_data(self, **kuargs):
        context = super(allproducts, self).get_context_data(**kuargs)
        context['Cost'] = cost.objects.all()
        context['Latestproducts'] = products.objects.all().order_by('-id')[:1]
        context['fehrests'] = productsgroups.objects.all()
        spg = productsgroups.objects.filter(gparentid=0).order_by('id')[:9]
        spgid = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        spgt = productsgroups.objects.all()
        spgtr = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        spgtr2 = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')

        return context


class firstpagelogoview(generic.ListView):
    models = firstpagebaners
    context_object_name = 'logo'
    template_name = 'index.html'
    queryset = firstpagebaners.objects.all()


class bankreport(generic.ListView):
    model = parametsaccounts
    context_object_name = 'bankreport'
    template_name = 'bank_view.html'
    queryset = parametsaccounts.objects.all()

    def get_context_data(self, **kwargs):
        context = super(bankreport, self).get_context_data(**kwargs)
        context['fcontact'] = centercontactus.objects.all()
        context['fhlogo'] = firstpagelogo.objects.all()
        context['spg'] = productsgroups.objects.filter(
            gparentid=0).order_by('id')[:9]
        context['spgid'] = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        context['spgt'] = productsgroups.objects.all()
        context['spgtr'] = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        context['spgtr2'] = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')

        return context


class bankaccount(generic.ListView):
    model = parametsaccounts
    context_object_name = 'bankreport'
    template_name = 'bacnkaccount.html'
    queryset = parametsaccounts.objects.all()

    def get_context_data(self, **kuargs):
        context = super(bankaccount, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class sasreportfooter(generic.ListView):
    model = parametssas
    context_object_name = 'sasreport'
    template_name = 'after_sale_view.html'
    queryset = parametssas.objects.all()

    def get_context_data(self, **kwargs):
        context = super(sasreportfooter, self).get_context_data(**kwargs)
        context['fcontact'] = centercontactus.objects.all()
        context['fhlogo'] = firstpagelogo.objects.all()
        context['spg'] = productsgroups.objects.filter(
            gparentid=0).order_by('id')[:9]
        context['spgid'] = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        context['spgt'] = productsgroups.objects.all()
        context['spgtr'] = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        context['spgtr2'] = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        return context


class weblogadmin(generic.ListView):
    models = weblog
    context_object_name = 'weblogadmin'
    template_name = 'weblogadmin.html'
    queryset = weblog.objects.all()


class weblogusers(generic.ListView):
    models = weblog
    context_object_name = 'weblogs'
    template_name = 'weblog_view.html'
    queryset = weblog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(weblogusers, self).get_context_data(**kwargs)
        context['fcontact'] = centercontactus.objects.all()
        context['fhlogo'] = firstpagelogo.objects.all()
        context['spg'] = productsgroups.objects.filter(
            gparentid=0).order_by('id')[:9]
        context['spgid'] = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        context['spgt'] = productsgroups.objects.all()
        context['spgtr'] = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        context['spgtr2'] = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        return context


class sasreportadmin(generic.ListView):
    model = parametssas
    context_object_name = 'sas'
    template_name = 'after_sale_support.html'
    queryset = parametssas.objects.all()

    def get_context_data(self, **kuargs):
        context = super(sasreportadmin, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class supportreportfooter(generic.ListView):
    model = parametssupport
    context_object_name = 'supportreport'
    template_name = 'support_view.html'
    queryset = parametssupport.objects.all()

    def get_context_data(self, **kwargs):
        context = super(supportreportfooter, self).get_context_data(**kwargs)
        context['fcontact'] = centercontactus.objects.all()
        context['fhlogo'] = firstpagelogo.objects.all()
        context['spg'] = productsgroups.objects.filter(
            gparentid=0).order_by('id')[:9]
        context['spgid'] = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        context['spgt'] = productsgroups.objects.all()
        context['spgtr'] = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        context['spgtr2'] = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')

        return context


class supportreportadmin(generic.ListView):
    model = parametssupport
    context_object_name = 'support'
    template_name = 'support.html'
    queryset = parametssupport.objects.all()

    def get_context_data(self, **kuargs):
        context = super(supportreportadmin, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class sparticle(generic.ListView):
    model = SPArticle
    context_object_name = 'spa'
    template_name = 'factordetaile.html'
    queryset = SPArticle.objects.all()


class AdminCheck(generic.ListView):
    model = Check
    context_object_name = 'Check'
    template_name = 'PayRcvDetail.html'
    queryset = Check.objects.all()

class userAdminCheck(generic.ListView):
    model = Check
    context_object_name = 'Check'
    template_name = 'PayRcvDetaile.html'
    queryset = Check.objects.all()


class sparticleseprate(generic.ListView):
    model = SPArticle
    context_object_name = 'spas'
    template_name = 'factordetaileseprated.html'

    def get(self, request, id, *args, **kwargs):
        spas = SPArticle.objects.all().filter(SPId=id)
        return render(request, 'factordetaileseprated.html', {'spas': spas})

class PayRcvDetailseprate(generic.ListView):
    model = Check
    context_object_name = 'pds'
    template_name = 'PayRcvDetail.html'

    def get(self, request, id, *args, **kwargs):
        pds = Check.objects.all().filter(id2=id)
        return render(request, 'PayRcvDetail.html', {'pds': pds})

class paypage(generic.ListView):
    models = sellbascket
    context_object_name = 'paypage'
    template_name = 'checkout.html'

    def get(self, request):
        userid = request.user.id
        fehrests = productsgroups.objects.all()
        sb = sellbascket.objects.all().filter(status=0, Create_Uid=userid)
        psb = products.objects.all()
        spg = productsgroups.objects.filter(gparentid=0).order_by('id')[:9]
        spgid = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        spgt = productsgroups.objects.all()
        spgtr = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        spgtr2 = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        return render(request, 'cart.html', {'sb': sb, 'fehrests': fehrests, 'psb': psb, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2})


class cardcost(generic.ListView):
    models = cost
    context_object_name = 'CostLV'
    template_name = 'cart.html'
    queryset = cost.objects.all()


class stors(generic.ListView):
    model = salecontactus
    context_object_name = 'stor'
    template_name = 'stors.html'
    queryset = salecontactus.objects.all()

    def get_context_data(self, **kwargs):
        context = super(stors, self).get_context_data(**kwargs)
        context['fhlogo'] = firstpagelogo.objects.all()
        context['fehrests'] = productsgroups.objects.all()
        context['spg'] = productsgroups.objects.filter(
            gparentid=0).order_by('id')[:9]
        context['spgid'] = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        context['spgt'] = productsgroups.objects.all()
        context['spgtr'] = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        context['spgtr2'] = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')

        return context


class indexproductshow(generic.ListView):
    models = products
    context_object_name = 'indexshowproduct'
    template_name = 'indexproduct.html'

    def get(self, request, id):
        fehrests = productsgroups.objects.all()
        indexshowproduct = products.objects.all().filter(id=id)
        Cost = cost.objects.all()
        return render(request, 'indexproduct.html', {'indexshowproduct': indexshowproduct,
                                                     'fehrests': fehrests, 'Cost': Cost})


class logoreportview(generic.ListView):
    model = firstpagelogo
    context_object_name = 'Logo'
    template_name = 'logo.html'
    queryset = firstpagelogo.objects.all()

    def get_context_data(self, **kuargs):
        context = super(logoreportview, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class bannersreportview(generic.ListView):
    model = firstpagebaners
    context_object_name = 'logo'
    template_name = 'logo_report.html'
    queryset = firstpagebaners.objects.all()

    def get_context_data(self, **kuargs):
        context = super(bannersreportview, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class aboutreportview(generic.ListView):
    model = aboutus
    context_object_name = 'about'
    template_name = 'about.html'
    queryset = aboutus.objects.all()

    def get_context_data(self, **kuargs):
        context = super(aboutreportview, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class aboutteamreportview(generic.ListView):
    model = aboutusp1
    context_object_name = 'aboutteam'
    template_name = 'aboutteam.html'
    queryset = aboutusp1.objects.all()

    def get_context_data(self, **kuargs):
        context = super(aboutteamreportview, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class useraboutteamreportview(generic.ListView):
    model = aboutusp1
    context_object_name = 'aboutusteam'
    template_name = 'about-2.html'
    queryset = aboutusp1.objects.all()


class aboutbrandreport(generic.ListView):
    models = productsbrands
    context_object_name = 'aboutbrand'
    template_name = 'about-2.html'
    queryset = productsbrands.objects.all()


class ccontactusreportview(generic.ListView):
    model = centercontactus
    context_object_name = 'ccontactus'
    template_name = 'ccontactus.html'
    queryset = centercontactus.objects.all()

    def get_context_data(self, **kuargs):
        context = super(ccontactusreportview, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        context['spg'] = productsgroups.objects.filter(
            gparentid=0).order_by('id')[:9]
        context['spgid'] = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        context['spgt'] = productsgroups.objects.all()
        context['spgtr'] = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        context['spgtr2'] = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')

        return context


class scontactusreportview(generic.ListView):
    model = salecontactus
    context_object_name = 'scontactus'
    template_name = 'scontactus.html'
    queryset = salecontactus.objects.all()

    def get_context_data(self, **kuargs):
        context = super(scontactusreportview, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context
# about us in master page


class footercontactus(generic.ListView):
    model = centercontactus
    context_object_name = 'fcontact'
    template_name = 'index.html'
    queryset = centercontactus.objects.all()


class userccontactusreportview(generic.ListView):
    model = centercontactus
    context_object_name = 'uccontactus'
    template_name = 'contact.html'
    queryset = centercontactus.objects.all()


class userscontactusreportview(generic.ListView):
    model = salecontactus
    context_object_name = 'uscontactus'
    template_name = 'contact.html'
    queryset = salecontactus.objects.all()


class customerquestionsview(generic.ListView):
    model = customerquestions
    context_object_name = 'cq'
    template_name = 'cq.html'
    queryset = customerquestions.objects.all()

    def get_context_data(self, **kuargs):
        context = super(customerquestionsview, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class newestproducts(generic.ListView):
    model = products
    context_object_name = 'newproducts'
    template_name = 'index.html'
    queryset = products.objects.all().order_by('-id')[:6]


class latestproducts(generic.ListView):
    model = products
    context_object_name = 'Latestproducts'
    template_name = 'index.html'
    queryset = products.objects.all().order_by('-id')[:1]


class nonegoods(generic.ListView):
    model = products
    context_object_name = 'ng'
    template_name = 'index.html'
    queryset = products.objects.all()


class usersreport(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = User
    permission_required = 'can_read_private_section'
    context_object_name = 'users'
    template_name = 'users.html'
    queryset = User.objects.all()

    def get_context_data(self, **kuargs):
        context = super(usersreport, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class productfirstpage(generic.ListView):
    models = products
    context_object_name = 'productfirst'
    template_name = 'index.html'
    queryset = products.objects.all()


class productss(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    models = products
    permission_required = 'can_read_private_section'
    context_object_name = 'product'
    template_name = 'product.html'
    queryset = products.objects.all()

    def get_context_data(self, **kuargs):
        context = super(productss, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class productsgroupsreport(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    models = productsgroups
    permission_required = 'can_read_private_section'
    context_object_name = 'productsgroupsLV'
    template_name = 'productsgroupsLV.html'
    queryset = productsgroups.objects.all()

    def get_context_data(self, **kuargs):
        context = super(productsgroupsreport, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class customerreport(generic.ListView):
    models = Customers
    context_object_name = 'customerLV'
    template_name = 'customer_report.html'
    queryset = Customers.objects.raw(
        "select a.id as id1 ,b.id as id,b.FAccId,b.Name,b.Family,b.CellPhone,b.PhoneNo,b.FaxNo,b.SCode,b.Email,b.EcCode,b.Address,b.ZipCode,b.UserId,b.TRes,b.CSex,b.FPId from comment a right join CustomerReport () b on a.id=b.id")

    def get_context_data(self, **kuargs):
        context = super(customerreport, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class ersalreport(generic.ListView):
    models = parametrsersal
    context_object_name = 'ersal'
    template_name = 'ersal.html'
    queryset = parametrsersal.objects.all()

    def get_context_data(self, **kuargs):
        context = super(ersalreport, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class osoolreport(generic.ListView):
    models = parametrsosool
    context_object_name = 'osool'
    template_name = 'osool.html'
    queryset = parametrsosool.objects.all()

    def get_context_data(self, **kuargs):
        context = super(osoolreport, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class ersalreportusers(generic.ListView):
    models = parametrsersal
    context_object_name = 'ersalusers'
    template_name = 'ersal_report_users.html'
    queryset = parametrsersal.objects.all().order_by('-id')[:1]

    def get_context_data(self, **kwargs):
        context = super(ersalreportusers, self).get_context_data(**kwargs)
        context['fhlogo'] = firstpagelogo.objects.all()
        context['spg'] = productsgroups.objects.filter(
            gparentid=0).order_by('id')[:9]
        context['spgid'] = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        context['spgt'] = productsgroups.objects.all()
        context['spgtr'] = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        context['spgtr2'] = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        return context


class osoolreportusers(generic.ListView):
    models = parametrsosool
    context_object_name = 'osool'
    template_name = 'osool_report_users.html'
    queryset = parametrsosool.objects.all().order_by('-id')[:1]

    def get_context_data(self, **kwargs):
        context = super(osoolreportusers, self).get_context_data(**kwargs)
        context['fhlogo'] = firstpagelogo.objects.all()
        context['spg'] = productsgroups.objects.filter(
            gparentid=0).order_by('id')[:9]
        context['spgid'] = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        context['spgt'] = productsgroups.objects.all()
        context['spgtr'] = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        context['spgtr2'] = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        return context


class customerreportJson(BaseDatatableView):
    model = Customers
    # def get_initial_queryset(self):
    #     return Customers.objects.raw("select a.id as id1 ,b.id as id,b.FAccId,b.Name,b.Family,b.CellPhone,b.PhoneNo,b.FaxNo,b.SCode,b.Email,b.EcCode,b.Address,b.ZipCode,b.UserId,b.TRes,b.CSex,b.FPId from comment a right join CustomerReport () b on a.id=b.id")

    context_object_name = 'customerLV'
    columns = ['', 'id', 'FAccId', 'Name', 'Family', 'CellPhone', 'PhoneNo', 'FaxNo',
               'SCode', 'Email', 'EcCode', 'Address', 'ZipCode', 'UserId', 'TRes', 'CSex', 'FPId']
    order_columns = ['', 'id', 'FAccId', 'Name', 'Family', 'CellPhone', 'PhoneNo', 'FaxNo',
                     'SCode', 'Email', 'EcCode', 'Address', 'ZipCode', 'UserId', 'TRes', 'CSex', 'FPId']

    def render_column(self, row, column):
        return super(customerreportJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)

        if search:
            qs = qs.filter(Q(id__icontains=search) | Q(FAccId__icontains=search) | Q(Name__icontains=search) | Q(Family__icontains=search) | Q(CellPhone__icontains=search)
                           | Q(PhoneNo__icontains=search) | Q(FaxNo__icontains=search) | Q(SCode__icontains=search) | Q(Email__icontains=search) | Q(EcCode__icontains=search) | Q(Address__icontains=search) | Q(ZipCode__icontains=search)
                           | Q(UserId__icontains=search) | Q(TRes__icontains=search) | Q(CSex__icontains=search) | Q(FPId__icontains=search))

        #filter_customer = self.request.GET.get('customer', None)
    # c=productsgroups.objects.all()

    # with connection.cursor() as cursor:
    #     cursor.execute(u"select * from CustomerReport ()")
    #     c=cursor.fetchall()
        return qs


class Factorsreport(generic.ListView):
    models = SPFactor
    context_object_name = 'factorLV'
    template_name = 'factorLV.html'
    queryset = SPFactor.objects.all()

    def get_context_data(self, **kuargs):
        context = super(Factorsreport, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class PayRcvreport(generic.ListView):
    models = PayRcv
    context_object_name = 'PayRcvLV'
    template_name = 'PayRcvLV.html'
    queryset = PayRcv.objects.all()

    def get_context_data(self, **kuargs):
        context = super(PayRcvreport, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


def MiladiToShamsi(Date):
    # date2=str(Date).replace("-", "/")
    with connection.cursor() as cursor:
        Date = cursor.execute(
            "select cast(dbo.__MiladiToShamsi__('{date2}') as nvarchar) as a".format(date2=Date)).fetchall()
        cursor.commit()
        for d in Date:
            t = d.a
        return t


class FactorsreportJson(BaseDatatableView):
    model = SPFactor
    columns = ['', 'id', 'FactorNo', 'ReferenceNo', 'SPDate', 'FactorType', 'CustomerId', 'Total', 'Discount', 'Expense', 'SPDesc',
               'CustomerName', 'CustomerPhoneNo', 'CustomerEcCode', 'CustomerAddress', 'FPId', 'SC', 'FStatus', 'FactorSubType', 'Committed']
    order_columns = ['', 'id', 'FactorNo', 'ReferenceNo', 'SPDate', 'FactorType', 'CustomerId', 'Total', 'Discount', 'Expense', 'SPDesc',
                     'CustomerName', 'CustomerPhoneNo', 'CustomerEcCode', 'CustomerAddress', 'FPId', 'SC', 'FStatus', 'FactorSubType', 'Committed']

    def render_column(self, row, column):
        if column == 'SPDate':
            return escape('{0}'.format(MiladiToShamsi(row.SPDate)))
        else:
            return super(FactorsreportJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        #FactorNo = self.request.GET.get('FactorNo', None)
        if search:
            qs = qs.filter(Q(id__icontains=search) | Q(FactorNo__icontains=search) | Q(ReferenceNo__icontains=search) | Q(SPDate__icontains=search) | Q(FStatus__icontains=search) | Q(FactorSubType__icontains=search) | Q(Committed__icontains=search
                                                                                                                                                                                                                            ) | Q(FactorType__icontains=search) | Q(CustomerId__icontains=search) | Q(Total__icontains=search) | Q(Discount__icontains=search) | Q(Discount__icontains=search) | Q(Expense__icontains=search) | Q(SPDesc__icontains=search) |
                           Q(CustomerName__icontains=search) | Q(CustomerPhoneNo__icontains=search) | Q(FPId__icontains=search) | Q(CustomerEcCode__icontains=search) | Q(CustomerAddress__icontains=search) | Q(FStatus__icontains=search) | Q(SC__icontains=search))
        filter_customer = self.request.GET.get('FactorNo', None)
        return qs


class PayRcvReportJson(BaseDatatableView):
    model = PayRcv
    columns = ['', 'PNo', 'PayType', 'PDate', 'RcvrFAccId', 'PDesc', 'CustomerId', 'PCValue']
    order_columns = ['', 'PNo', 'PayType', 'PDate', 'RcvrFAccId', 'PDesc', 'CustomerId', 'PCValue']

    def render_column(self, row, column):
        if column == 'PDate':
            return escape('{0}'.format(MiladiToShamsi(row.PDate)))
        else:
            return super(PayRcvReportJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None) 
        if search:
            qs = qs.filter(Q(id__icontains=search) | Q(PNo__icontains=search) | Q(PayType__icontains=search) | Q(RcvrFAccId__icontains=search) | Q(PDesc__icontains=search) | Q(PCValue__icontains=search))
        filter_customer = self.request.GET.get('PNo', None)
        return qs

class PayRcvDetaileReportJson(BaseDatatableView):
    model = Check
    columns = ['','id','Stype', 'CheckNo', 'CValue', 'CDate', 'RcptDate', 'CStatus']
    order_columns = ['','id','Stype', 'CheckNo', 'CValue', 'CDate', 'RcptDate', 'CStatus']

    def render_column(self, row, column):
        # if column == 'CDate':
        #     return escape('{0}'.format(MiladiToShamsi(row.CDate)))
        # else:
        return super(PayRcvDetaileReportJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None) 
        if search:
            qs = qs.filter(Q(id__icontains=search) | Q(Stype__icontains=search) | Q(CheckNo__icontains=search) | Q(CType__icontains=search) | Q(RcptDate__icontains=search) | Q(CValue__icontains=search))
        filter_customer = self.request.GET.get('CheckNo', None)
        return qs


class ProductReportJson(BaseDatatableView):
    model = products
    columns = ['', 'id', 'name', 'brand', 'group', 'serial', 'desc', 'img1', 'img2', 'img3',
               'img4', 'img5', 'img6', 'Create_Date', 'Update_Date', 'Create_Uid', 'Update_Uid']
    order_columns = ['', 'id', 'name', 'brand', 'group', 'serial', 'desc', 'img1', 'img2',
                     'img3', 'img4', 'img5', 'img6', 'Create_Date', 'Update_Date', 'Create_Uid', 'Update_Uid']

    def render_column(self, row, column):
        # if column == 'SPDate':
        #     return escape('{0}'.format(MiladiToShamsi(row.SPDate)))
        # else:
        return super(ProductReportJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        col1 = self.request.GET.get('product1', None)
        list1 = col1.split(",")
        s1 = []
        for a in list1:
            if len(str(a)) > 0:
                s1.append(a)

        # col2 = self.request.GET.get('product2', None)
        # list2 = col2.split(",")
        col3 = self.request.GET.get('product3', None)
        # list3 = col3.split(",")
        col4 = self.request.GET.get('product4', None)
        # list4 = col4.split(",")
        col5 = self.request.GET.get('product5', None)
        # list5 = col5.split(",")
        col6 = self.request.GET.get('product6', None)
        # list6 = col6.split(",")
        # col7 = self.request.GET.get('product7', None)
        # list7 = col7.split(",")
        # col8 = self.request.GET.get('product8', None)
        # list8 = col8.split(",")
        # col9 = self.request.GET.get('product9', None)
        # list9 = col9.split(",")
        # col10 = self.request.GET.get('product10', None)
        # list10 = col10.split(",")
        # col11 = self.request.GET.get('product11', None)
        # list11 = col11.split(",")
        # col12 = self.request.GET.get('product12', None)
        # list12 = col12.split(",")
        # col13 = self.request.GET.get('product13', None)
        # list13 = col13.split(",")
        if search:
            qs = qs.filter(Q(id=search) | Q(name__icontains=search) | Q(serial__icontains=search) | Q(
                group__Group_Name__icontains=search) | Q(brand__name__icontains=search))
        if col1:
            qs = qs.filter(id__in=s1)
        if col3:
            qs = qs.filter(name__icontains=col3)
        if col4:
            qs = qs.filter(serial__icontains=col4)
        if col5:
            qs = qs.filter(group__Group_Name__icontains=col5)
        if col6:
            qs = qs.filter(brand__name__icontains=col6)

        #filter_customer = self.request.GET.get('FactorNo', None)
        return qs


class commentreport(generic.ListView):
    models = comment
    permission_required = 'can_read_private_section'
    context_object_name = 'commentLV'
    template_name = 'commentLV.html'
    queryset = comment.objects.all()

    def get_context_data(self, **kuargs):
        context = super(commentreport, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class costreport(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    models = cost
    permission_required = 'can_read_private_section'
    context_object_name = 'costLV'
    template_name = 'costLV.html'
    queryset = cost.objects.all()

    def get_context_data(self, **kuargs):
        context = super(costreport, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class brandreport(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    models = productsbrands
    permission_required = 'can_read_private_section'
    context_object_name = 'productsbrandsLV'
    template_name = 'productsbrandsLV.html'
    queryset = productsbrands.objects.all()

    def get_context_data(self, **kuargs):
        context = super(brandreport, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class brandreportfirstpage(generic.ListView):
    models = productsbrands
    context_object_name = 'brand'
    template_name = 'index.html'
    queryset = productsbrands.objects.all()


class users(generic.ListView):
    models = User
    context_object_name = 'users'
    template_name = 'index.html'
    queryset = User.objects.all()


# 0-1 first-page-slider-LV
class sliderreport(generic.ListView):
    models = slider
    context_object_name = 'slider'
    template_name = 'slider.html'
    queryset = slider.objects.all()

    def get_context_data(self, **kuargs):
        context = super(sliderreport, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


class insidesliderreport(generic.ListView):
    models = insideslider
    context_object_name = 'slider'
    template_name = 'insideslider.html'
    queryset = insideslider.objects.all()

    def get_context_data(self, **kuargs):
        context = super(insidesliderreport, self).get_context_data(**kuargs)
        userid = self.request.user.id
        context['UserInfo'] = User.objects.all().filter(id=userid)
        return context


# 0-1 first-page-slider-LV
class sliders(generic.ListView):
    models = insideslider
    context_object_name = 'sliders'
    template_name = 'advancedsearchProducts.html'
    queryset = insideslider.objects.all()


class advancsedbanner(generic.ListView):
    models = firstpagebaners
    context_object_name = 'advancb'
    template_name = 'advancedsearchProducts.html'
    queryset = firstpagebaners.objects.all()


class fehrest(generic.ListView):
    models = productsgroups
    context_object_name = 'fehrests'
    template_name = 'index.html'
    queryset = productsgroups.objects.all()


class fehrestdetail(generic.ListView):
    models = products
    context_object_name = 'productsdetails'
    template_name = 'index.html'
    queryset = products.objects.all()


class productsprice(generic.ListView):
    models = cost
    context_object_name = 'cost'
    template_name = 'index.html'
    queryset = cost.objects.all()

    def get_context_data(self, **kwargs):
        context = super(productsprice, self).get_context_data(**kwargs)
        context['cost'] = cost.objects.all()
        return context


class search_box(View):
    def get(self, request):
        if 'search' in request.GET:
            search_box = self.request.GET.get('search')
            if search_box:
                result = products.objects.filter(name__contains=search_box) or \
                    products.objects.filter(brand=productsbrands.objects.all().filter(name=search_box).values_list('id', flat=True).order_by('id')[:1]) or \
                    products.objects.filter(group=productsgroups.objects.all().filter(
                        Group_Name=search_box).values_list('id', flat=True).order_by('id')[:1])
            else:
                result = None
            fehrests = productsgroups.objects.all()
            Cost = cost.objects.all()
            spg = productsgroups.objects.filter(gparentid=0).order_by('id')[:9]
            spgid = list(productsgroups.objects.filter(
                gparentid=0).values_list('id', flat=True))
            spgt = productsgroups.objects.all()
            spgtr = productsgroups.objects.raw(
                'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
            spgtr2 = productsgroups.objects.raw(
                'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
            fhlogo = firstpagelogo.objects.all()
            return render(request, 'serach_result.html', {'fhlogo': fhlogo, 'result': result, 'fehrests': fehrests, 'Cost': Cost, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2})


class AddBascket(View):
    def get(self, request):
        id1 = request.GET.get('pid', None)
        userid = request.user.id
        print('step 1')
        goods=0
        sellbascketcountsells=0
        numberofgoods=0
        if products.objects.get(id=id1).goods:
            goods=1
            try:
                for a in  sellbascket.objects.get(pid_id=id1):
                    sellbascketcountsells+=a.pcount
            except:
                pass
                
            print('step 6')
            numberofgoods=(products.objects.get(id=id1).numberofgoods)-(sellbascketcountsells)
            print('step 7')
        if  goods==0 or numberofgoods==0 :
            return JsonResponse(data={'goods':goods,'numberofgoods':numberofgoods})
        elif sellbascket.objects.filter(Create_Uid=request.user.id, pid_id=id1 , status=0) or goods==0 or numberofgoods==0:
            return JsonResponse(data={'AddedBefor':1})
        else:
            obj = sellbascket.objects.create(
                pid_id=id1,
                status=0,
                Create_Uid=userid,
                Update_Uid=userid
            )
        print('step 2')
        i = products.objects.get(id=obj.pid_id).img1
        Bascket = {'id': obj.id, 'pid': obj.pid_id, 'name': products.objects.get(
            id=obj.pid_id).name, 'img1': str(i), 'Create_Uid': obj.Create_Uid, 'pcount': 1}
        sellbascketCount = sellbascket.objects.filter(
            Create_Uid=request.user.id).count()
        print('step 3')
        try:
            priceoff = cost.objects.get(pid_id=obj.pid_id).priceoff
        except:
            priceoff = 0
        print('step 4')
        sumBascketPriceoff = 0
        for p in sellbascket.objects.filter(Create_Uid=request.user.id):
            try:
                sumBascketPriceoff += cost.objects.get(
                    pid_id=p.pid_id).priceoff*p.pcount
            except:
                sumBascketPriceoff = sumBascketPriceoff
        print('step 5')
        data = {
            'Bascket': Bascket, 'sellbascketCount': sellbascketCount, 'priceoff': priceoff, 'sumBascketPriceoff': sumBascketPriceoff,'goods':goods,'numberofgoods':numberofgoods,'AddedBefor':0
        }
        return JsonResponse(data)


class Bascketdelete(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name = products.objects.get(
            id=sellbascket.objects.get(id=id1).pid_id).name
        sellbascket.objects.get(id=id1).delete()
        sellbascketCount = sellbascket.objects.filter(
            Create_Uid=request.user.id).count()
        sumBascketPriceoff = 0
        for p in sellbascket.objects.filter(Create_Uid=request.user.id):
            try:
                sumBascketPriceoff += cost.objects.get(
                    pid_id=p.pid_id).priceoff*p.pcount
            except:
                continue
        data = {
            'deleted': True, 'sellbascketCount': sellbascketCount, 'sumBascketPriceoff': sumBascketPriceoff, 'name': name
        }
        return JsonResponse(data)


class AddFavorite(View):
    def get(self, request):
        id1 = request.GET.get('pid', None)
        userid = request.user.id
        if productdetails.objects.filter(Create_Uid=request.user.id, pid_id=id1, favorite=0):
            obj = productdetails.objects.get(
                Create_Uid=request.user.id, pid_id=id1)
            obj.favorite = 1
            obj.Update_Uid = userid
            obj.save()
        elif productdetails.objects.filter(Create_Uid=request.user.id, pid_id=id1, favorite=1):
            return JsonResponse({})
        else:
            obj = productdetails.objects.create(
                pid_id=id1,
                favorite=1,
                Create_Uid=userid,
                Update_Uid=userid
            )
        i = products.objects.get(id=obj.pid_id).img1
        Favorite = {'id': obj.id, 'pid': obj.pid_id, 'name': products.objects.get(
            id=obj.pid_id).name, 'img1': str(i), 'Create_Uid': obj.Create_Uid}
        favoriteCount = productdetails.objects.filter(
            Create_Uid=request.user.id, favorite=1).count()

        try:
            priceoff = cost.objects.get(pid_id=obj.pid_id).priceoff
        except:
            priceoff = 0
        sumFavoritePriceoff = 0
        for p in productdetails.objects.filter(Create_Uid=request.user.id, favorite=1):
            try:
                sumFavoritePriceoff += cost.objects.get(
                    pid_id=p.pid_id).priceoff
            except:
                sumFavoritePriceoff = sumFavoritePriceoff
        data = {
            'Favorite': Favorite, 'favoriteCount': favoriteCount, 'priceoff': priceoff, 'sumFavoritePriceoff': sumFavoritePriceoff
        }
        return JsonResponse(data)


class removepic(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        img = request.GET.get('img', None)
        if img == 'img1':
            b = products.objects.filter(id=id1)
            b.update(img1='')
        elif img == 'img2':
            b = products.objects.filter(id=id1)
            b.update(img2='')
        elif img == 'img3':
            b = products.objects.filter(id=id1)
            b.update(img3='')
        elif img == 'img4':
            b = products.objects.filter(id=id1)
            b.update(img4='')
        elif img == 'img5':
            b = products.objects.filter(id=id1)
            b.update(img5='')
        elif img == 'img6':
            b = products.objects.filter(id=id1)
            b.update(img6='')
        data = {
            'img': img
        }
        return JsonResponse(data)


class removepicBanner(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        img = request.GET.get('img', None)
        if img == 'baner1':
            b = firstpagebaners.objects.filter(id=id1)
            b.update(baner1='')
        elif img == 'img2':
            b.update(banner1='')
        elif img == 'img3':
            b = firstpagebaners.objects.filter(id=id1)
            b.update(banner1='')
        elif img == 'img4':
            b = products.objects.filter(id=id1)
            b.update(img4='')
        elif img == 'img5':
            b = products.objects.filter(id=id1)
            b.update(img5='')
        elif img == 'img6':
            b = products.objects.filter(id=id1)
            b.update(img6='')
        data = {
            'img': img
        }
        return JsonResponse(data)


class Favoritedelete(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name = products.objects.get(
            id=productdetails.objects.get(id=id1).pid_id).name
        productdetails.objects.get(id=id1).delete()
        favoriteCount = productdetails.objects.filter(
            Create_Uid=request.user.id, favorite=1).count()
        sumFavoritePriceoff = 0
        for p in productdetails.objects.filter(Create_Uid=request.user.id, favorite=1):
            try:
                sumFavoritePriceoff += cost.objects.get(
                    pid_id=p.pid_id).priceoff
            except:
                continue
        data = {
            'deleted': True, 'favoriteCount': favoriteCount, 'sumFavoritePriceoff': sumFavoritePriceoff, 'name': name
        }
        return JsonResponse(data)


class usersarticle(View):
    models = SPArticle, SPFactor

    def get(self, request):
        userid = request.user.customersid_id
        factorsid = SPFactor.objects.all().filter(CustomerId=userid)
        userarticles = SPArticle.objects.all().filter(SPId__in=factorsid)
        return render(request, 'userarticles.html', {'userarticles': userarticles})


class userspayarticle(View):
    models = PayRcv, Check

    def get(self, request):
        userid = request.user.customersid_id
        print(userid)
        userarticles = Check.objects.all().filter(CId=userid)
        return render(request, 'userpayarticle.html', {'userarticles': userarticles})


class usersfactors(View):
    models = SPFactor, SPArticle

    def get(self, request):
        fcontact = centercontactus.objects.all()
        userid = request.user.id
        UserInfo = User.objects.all().filter(id=userid)
        userid = request.user.customersid_id
        spid = SPFactor.objects.filter(
            CustomerId=userid).values_list('id', flat=True)
        # totalcount = str(SPFactor.objects.all().filter(
        #     CustomerId=userid).filter().count())
        script1="select 0 as id, case when FactorType like 'خريد' then 'فروش' when FactorType like 'فروش' then 'فاکتور' when  FactorType like 'رسيد پرداخت' then 'رسید پرداخت' when FactorType like 'رسید دریافت' then  'رسيد دریافت'  when FactorType like 'برگشت از خريد' then  'برگشت از فروش' when FactorType like 'برگشت از فروش' then  'فاکتور برگشتی' end as FactorType,(select count(*) from SPArticle spa where spa.spid in (select id from SPFactor where FactorType=spf.FactorType and CustomerId  ={userid})) as totalcount,(select SUM(ATotal) from SPArticle spa where spa.spid in (select id from SPFactor where FactorType=spf.FactorType and CustomerId  ={userid})) as totalsale from SPFactor spf where CustomerId  ={userid} group by FactorType".format(userid=userid)
        print(script1)
        totalsale = SPArticle.objects.raw(script1)

        datein1 = request.GET.get('date1')
        datein2 = request.GET.get('date2')
        if request.method == 'GET':
            if datein1 == None or datein2 == None:
                datefilter = SPFactor.objects.raw(
                    "with tmp as(select id,1 as t,CustomerId,FactorNo,FactorType,cast(SPDate as date) as SPDate,CustomerName,Discount,Expense,Total from SPfactor union all select id,0 as t,CustomerId,PNo,PayType,cast(PDate as date) as SPDate,RcvrFAccId,0 as Discount,0 as Expense,PCValue from PayRcv)select id, case when FactorType like 'خريد' then 'فروش' when FactorType like 'فروش' then 'خريد' when  FactorType like 'رسيد پرداخت' then 'رسید پرداخت' when FactorType like 'رسید دریافت' then  'رسيد دریافت'  when FactorType like 'برگشت از خريد' then  'برگشت از فروش' when FactorType like 'برگشت از فروش' then  'برگشت از خريد' end as FactorType,CustomerId,FactorNo,SPDate,CustomerName,Discount,Expense,Total,t from tmp where CustomerId is not null and CustomerId={userid}order by SPDate".format(userid=userid))
            else:
                datef1 = datein1.replace("-", "/")
                datef2 = datein2.replace("-", "/")
                datefilter = SPFactor.objects.raw(
                    "with tmp as(select id,1 as t,CustomerId,FactorNo,FactorType,cast(SPDate as date) as SPDate,CustomerName,Discount,Expense,Total from SPfactor union all select id,0 as t,CustomerId,PNo,PayType,cast(PDate as date) as SPDate,RcvrFAccId,0 as Discount,0 as Expense,PCValue from PayRcv)select id, case when FactorType like 'خريد' then 'فروش' when FactorType like 'فروش' then 'خريد' when  FactorType like 'رسيد پرداخت' then 'رسید پرداخت' when FactorType like 'رسید دریافت' then  'رسيد دریافت'  when FactorType like 'برگشت از خريد' then  'برگشت از فروش' when FactorType like 'برگشت از فروش' then  'برگشت از خريد' end as FactorType,CustomerId,FactorNo,SPDate,CustomerName,Discount,Expense,Total,t from tmp where CustomerId is not null and spdate between dbo.ShamsitoMiladi('{date1}') and dbo.ShamsitoMiladi('{date2}') and CustomerId={userid}order by SPDate".format(date1=datef1, date2=datef2, userid=userid))

        
        spg = productsgroups.objects.filter(gparentid=0).order_by('id')[:9]
        spgid = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        spgt = productsgroups.objects.all()
        spgtr = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        spgtr2 = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        testform = filterdate1(request.GET)
        return render(request, 'dashboard.html', {'fcontact': fcontact, 'UserInfo': UserInfo, 'testform': testform, 'spg': spg, 'spgt': spgt, 'spgtr': spgtr, 'spgtr2': spgtr2, 'totalsale': totalsale,  'datefilter': datefilter, 'datein1': datein1, 'datein2': datein2})

@login_required(login_url='login')
def factordetail(request, id):
    fd = SPArticle.objects.all().filter(SPId=id)
    Amountsum = SPArticle.objects.filter(
        SPId=id).aggregate(Sum=Sum('Amount'))['Sum']
    UnitPricesum = SPArticle.objects.filter(
        SPId=id).aggregate(Sum=Sum('UnitPrice'))['Sum']
    VTaxsum = SPArticle.objects.filter(
        SPId=id).aggregate(Sum=Sum('VTax'))['Sum']
    VChargesum = SPArticle.objects.filter(
        SPId=id).aggregate(Sum=Sum('VCharge'))['Sum']
    Percentagesum = SPArticle.objects.filter(
        SPId=id).aggregate(Sum=Sum('Percentage'))['Sum']
    ATotalsum = SPArticle.objects.filter(
        SPId=id).aggregate(Sum=Sum('ATotal'))['Sum']
    return render(request, 'factordetail.html', {'fd': fd, 'Amountsum': Amountsum,
                                                 'UnitPricesum': UnitPricesum, 'VTaxsum': VTaxsum, 'VChargesum': VChargesum, 'Percentagesum': Percentagesum,
                                                 'ATotalsum': ATotalsum})

@login_required(login_url='login')
def PayRcvDetail(request, id):
    datefilter = Check.objects.raw('select * from dbo.[Check] c inner join PayRcvCheck pr on c.id2=pr.CheckId inner join PayRcv p on p.id=pr.PayRcvId where p.id = {}'.format(id))
    print(datefilter)
    return render(request, 'PayRcvDetail.html', {'datefilter': datefilter })


@login_required(login_url='login')
def userchangeinfo(request):
    success = []
    userid = request.user.id
    edit_user = get_object_or_404(User, pk=userid)
    userinfo = userinfoupdate(request.POST, request.FILES, instance=edit_user)
    if request.method == 'POST':
        if userinfo.is_valid():
            userinfo.save()
            success.append('کاربر گرامی اطلاعات شما با موفقیت ذخیره گردید .')
            userinfo = userinfoupdate(instance=edit_user)
            return render(request, 'partials/userschangeinfo.html', {'userinfo': userinfo, 'success': success})
    userinfo = userinfoupdate(instance=edit_user)
    return render(request, 'partials/userschangeinfo.html', {'userinfo': userinfo, 'success': success})


class AddComment(View):
    def get(self, request):
        Head1 = request.GET.get('Head', None)
        com1 = request.GET.get('com', None)
        pid1 = request.GET.get('pid', None)
        userid = request.user.id

        obj = comment.objects.create(
            pid_id=pid1,
            Head=Head1,
            com=com1,
            Create_Uid=userid,
            Update_Uid=userid
        )
        Create_Uid = request.user.first_name

        alarm = 'این نظر پس از تایید توسط مدیر سیستم در سایت نمایش داده خواهد شد.'

        comment1 = {
            'id': obj.id, 'pid': obj.pid_id, 'Head': obj.Head, 'com': obj.com, 'Create_Uid': obj.Create_Uid, 'Create_Date': obj.Create_Date
        }

        data = {
            'comment1': comment1, 'Create_Uid': Create_Uid, 'alarm': alarm,
        }
        return JsonResponse(data)


class commentAccept(View):
    def get(self, request):
        id1 = request.GET.get('id', None)

        obj = comment.objects.filter(id=id1).update(
            status=1, Update_Uid=request.user.id)

        data = {

        }
        return JsonResponse(data)


class commentReject(View):
    def get(self, request):
        id1 = request.GET.get('id', None)

        obj = comment.objects.filter(id=id1).update(
            status=2, Update_Uid=request.user.id)

        data = {

        }
        return JsonResponse(data)


class commentDelete(View):
    def get(self, request):
        id1 = request.GET.get('id', None)

        obj = comment.objects.filter(id=id1).delete()

        data = {

        }
        return JsonResponse(data)


class UpdateCount(View):
    def get(self, request):
        newcount = request.GET.get('newcount', None)
        pid = request.GET.get('pid', None)
        id = request.GET.get('id', None)
        obj = sellbascket.objects.get(id=id)
        goods=0
        sellbascketcountsells=0
        numberofgoods=0
        if products.objects.get(id=pid).goods:
            goods=1
            try:
                for a in  sellbascket.objects.get(pid_id=pid,status=1):
                    sellbascketcountsells+=a.pcount
            except:
                pass
                
            print('step 6')
            numberofgoods=(products.objects.get(id=pid).numberofgoods)-(sellbascketcountsells)
            print('step 7')
        isUpdated=1
        if  goods==0 or (goods==1 and numberofgoods < int(newcount)) :
            isUpdated=0
            newcount=min(obj.pcount,numberofgoods)
        obj.pcount = newcount
        obj.save()
        sumBascketPriceoff = 0
        for p in sellbascket.objects.filter(Create_Uid=request.user.id):
            try:
                sumBascketPriceoff += cost.objects.get(
                    pid_id=p.pid_id).priceoff*p.pcount
            except:
                continue
        Newtotalcost = sellbascket.objects.get(
            id=id).pcount * cost.objects.get(pid_id=pid).priceoff
        #countdetail = {'sumBascketPriceoff':sumBascketPriceoff}
        data = {
            'sumBascketPriceoff': sumBascketPriceoff, 'Newtotalcost': Newtotalcost, 'newcount': newcount ,'isUpdated':isUpdated
        }
        return JsonResponse(data)


@login_required(login_url='login')
@permission_required('User.can_read_private_section')
def customerSync(request):
    with connection.cursor() as cursor:
        cursor.execute(u"exec customerSync")
    data = {}
    return HttpResponseRedirect('/dashboard/customer/report/')


@login_required(login_url='login')
@permission_required('User.can_read_private_section')
def UserSync(request):
    with connection.cursor() as cursor:
        cursor.execute(u"exec SyncUser")
    data = {}
    return HttpResponseRedirect('/dashboard/customer/report/')

@login_required(login_url='login')
@permission_required('User.can_read_private_section')
def FactorSync(request):
    with connection.cursor() as cursor:
        cursor.execute(u"exec FactorSync")
    return HttpResponseRedirect('/dashboard/Factors/report/')

@login_required(login_url='login')
@permission_required('User.can_read_private_section')
def PayRcvSync(request):
    with connection.cursor() as cursor:
        cursor.execute(u"exec PayRcvSync")
    return HttpResponseRedirect('/dashboard/Pay/report/')


class ArticlereportJson(BaseDatatableView):
    model = SPArticle
    columns = ['', 'Id2', 'SPId', 'MerchandiseId', 'Amount', 'UnitId',
               'UnitPrice', 'SPADesc', 'VTax', 'VCharge', 'Percentage', 'ATotal']
    order_columns = ['', 'Id2', 'SPId', 'MerchandiseId', 'Amount',
                     'UnitId', 'UnitPrice', 'SPADesc', 'VTax', 'VCharge', 'Percentage', 'ATotal']

    def render_column(self, row, column):
        if column == 'SPDate':
            return escape('{0}'.format(MiladiToShamsi(row.SPDate)))
        else:
            return super(ArticlereportJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        #FactorNo = self.request.GET.get('FactorNo', None)
        if search:
            qs = qs.filter(Q(Id2__icontains=search) | Q(SPId__icontains=search) | Q(MerchandiseId__icontains=search) | Q(Amount__icontains=search) | Q(UnitId__icontains=search) | Q(UnitPrice__icontains=search)
                           | Q(SPADesc__icontains=search) | Q(VTax__icontains=search) | Q(VCharge__icontains=search) | Q(Percentage__icontains=search))
        filter_customer = self.request.GET.get('FactorNo', None)
        return qs


class lastnewspage(generic.ListView):
    model = lastnews
    context_object_name = 'lnp'
    template_name = 'last_news.html'
    queryset = lastnews.objects.all()


class lastnewspageone(generic.ListView):
    model = lastnews

    def get(self, request, id):
        lnp = lastnews.objects.all().filter(id=id)
        return render(request, 'last_news.html', {'lnp': lnp})


class advancedsearchProducts(generic.ListView):
    models = products
    context_object_name = 'products'
    template_name = 'advancedsearchProducts.html'
    queryset = products.objects.all()

    def get(self, request, id, *args, **kwargs):
        context = locals()
        level = productsgroups.objects.get(id=id).glevel
        with connection.cursor() as cursor:
            # if level==1:
            #     cheched=cursor.execute(u"select id from productsgroups where id={id} union all select id from productsgroups where gparentid={id} union all select id from productsgroups where gparentid in (select id from productsgroups where gparentid={id})".format(id=id))
            # elif level==2:
            #     cheched=cursor.execute(u"select gparentid from productsgroups where id={id} union all select id from productsgroups where id={id}  union all select id from productsgroups where  gparentid={id}".format(id=id))
            # elif level==3:
            #     cheched=cursor.execute(u"select id from productsgroups where  id in( select gparentid from productsgroups where id in( select gparentid from productsgroups where id={id})) union all select gparentid from productsgroups where id={id} union all select id from productsgroups where id={id}".format(id=id))
            cheched = cursor.execute(
                u"select id from productsgroups where id={id}".format(id=id))
            allchecked = cheched.fetchall()
            allcheckedList = []
            for a in allchecked:
                allcheckedList.append(a[0])
        context['allchecked'] = allchecked
        context['id'] = id
        context['sliders'] = insideslider.objects.all()
        context['khabar'] = lastnews.objects.all().order_by('-id')[:3]
        context['bestssale'] = sellbascket.objects.raw(
            "select top(4) a.pid_id as id,sum(a.pcount) as count ,b.img1,b.name,(select c.Group_Name from productsgroups c where c.id=b.group_id) as groupname ,(select name from productsbrands where id=b.brand_id) as brand  from sellbascket a join products b on a.pid_id=b.id where b.group_id in ({id}) group by pid_id ,b.img1,b.name,b.group_id,b.brand_id order by sum(a.pcount) desc".format(id=id))
        context['advancb'] = firstpagebaners.objects.all()
        context['fcontact'] = centercontactus.objects.all()
        context['spdesc'] = productsgroups.objects.all().filter(id=id)
        context['fhlogo'] = firstpagelogo.objects.all().order_by('-id')[:1]
        context['productsgroups'] = productsgroups.objects.filter(gparentid=0)
        context['productsgroups1'] = productsgroups.objects.raw(
            'select * from productsgroups where (id in ({id}) and glevel=2) or (id in (select gparentid from productsgroups where id={id} and glevel=3))'.format(id=id))
        # context['productsgroups2'] = productsgroups.objects.filter(glevel=3)
        context['productsgroups2'] = productsgroups.objects.raw(
            'select * from productsgroups where (id in ({id}) or gparentid in ({id}) or gparentid in (select gparentid from productsgroups where id in ({id}))) and glevel=3'.format(id=id))
        productslist = products.objects.raw('with tmp0 as (select * from productsgroups  where  id in ({Groups1})union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=2 )),tmp as(select * from productsgroups  where  id in ({Groups1}) union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and id not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 ) union all select * from productsgroups a where glevel=3 and gparentid in (select id from tmp0) and gparentid not in (select gparentid from productsgroups where id in (select id from tmp0) and glevel=3 ))select top 24 * from products where group_id in (select id from tmp) order by group_id'.format(Groups1=id))
        productslistKol = products.objects.raw('with tmp0 as (select * from productsgroups  where  id in ({Groups1})union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=2 )),tmp as(select * from productsgroups  where  id in ({Groups1}) union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and id not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 ) union all select * from productsgroups a where glevel=3 and gparentid in (select id from tmp0) and gparentid not in (select gparentid from productsgroups where id in (select id from tmp0) and glevel=3 ))select  * from products where group_id in (select id from tmp) order by group_id'.format(Groups1=id))

        context['products'] = productslist
        productsFilteredCount = 0
        for a in productslist:
            productsFilteredCount += 1
        productsFilteredCountKol = 0
        for a in productslistKol:
            productsFilteredCountKol += 1
        context['productsCount'] = productsFilteredCount
        context['productsCountKol'] = productsFilteredCountKol
        id1 = productsgroups.objects.get(id=id).gparentid
        context['productsbrands'] = productsbrands.objects.raw('with tmp0 as (select * from productsgroups  where  id in ({Groups1})union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=2 )),tmp as(select * from productsgroups  where  id in ({Groups1}) union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and id not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 ) union all select * from productsgroups a where glevel=3 and gparentid in (select id from tmp0) and gparentid not in (select gparentid from productsgroups where id in (select id from tmp0) and glevel=3 ))select * from productsbrands where id in (select brand_id from products where group_id in (select id from tmp) )'.format(Groups1=id1))
        context['pc1'] = productscategory.objects.raw('with tmp0 as (select * from productsgroups  where  id in ({Groups1})union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=2 )),tmp as(select * from productsgroups  where  id in ({Groups1}) union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and id not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 ) union all select * from productsgroups a where glevel=3 and gparentid in (select id from tmp0) and gparentid not in (select gparentid from productsgroups where id in (select id from tmp0) and glevel=3 ))select * from productscategory where id in (select cname1_id from products a where group_id in (select id from tmp) ) or id in (select (select cparentid from productscategory where id=a.cname1_id) from products a where group_id in (select id from tmp) )'.format(Groups1=id1))
        context['pc2'] = productscategory.objects.raw('with tmp0 as (select * from productsgroups  where  id in ({Groups1})union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=2 )),tmp as(select * from productsgroups  where  id in ({Groups1}) union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and id not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 ) union all select * from productsgroups a where glevel=3 and gparentid in (select id from tmp0) and gparentid not in (select gparentid from productsgroups where id in (select id from tmp0) and glevel=3 ))select * from productscategory where id in (select cname2_id from products where group_id in (select id from tmp) ) or id in (select (select cparentid from productscategory where id=a.cname2_id) from products a where group_id in (select id from tmp) )'.format(Groups1=id1))
        context['pc3'] = productscategory.objects.raw('with tmp0 as (select * from productsgroups  where  id in ({Groups1})union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=2 )),tmp as(select * from productsgroups  where  id in ({Groups1}) union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and id not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 ) union all select * from productsgroups a where glevel=3 and gparentid in (select id from tmp0) and gparentid not in (select gparentid from productsgroups where id in (select id from tmp0) and glevel=3 ))select * from productscategory where id in (select cname3_id from products where group_id in (select id from tmp) ) or id in (select (select cparentid from productscategory where id=a.cname3_id) from products a where group_id in (select id from tmp) )'.format(Groups1=id1))
        context['spg'] = productsgroups.objects.filter(
            gparentid=0).order_by('id')[:9]
        context['spgid'] = list(productsgroups.objects.filter(
            gparentid=0).values_list('id', flat=True))
        context['spgt'] = productsgroups.objects.all()
        context['spgtr'] = productsgroups.objects.raw(
            'select *,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        context['spgtr2'] = productsgroups.objects.raw(
            'select distinct gparentid as id,(select count(*) from productsgroups where gparentid=a.gparentid ) tedad from productsgroups a where gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0)) and a.id in (select top 5 id from productsgroups where gparentid=a.gparentid )  ')
        return render(request, self.template_name, context)


class advancedsearchProductsJson(View):
    def get(self, request):
        Groups = request.GET.get('Groups', None)
        id = request.GET.get('id', None)
        Groups1 = Groups[1:-1]
        if len(Groups1) > 0:
            #Groups1Check=productsgroups.objects.raw('select id from productsgroups a where  (glevel=1 and id in ({Groups1})) or (glevel=2 and id in ({Groups1}) and gparentid in ({Groups1}) )or (glevel=3 and id in ({Groups1}) and  gparentid in ({Groups1}) and (select gparentid from productsgroups where id in ( select gparentid from productsgroups where glevel=3  and id=a.id) and gparentid in ({Groups1}) ) in ({Groups1}))'.format(Groups1=Groups1))
            Groups1Check = productsgroups.objects.raw(
                'select id from productsgroups where id in ({Groups1}) '.format(Groups1=Groups1))

            Groups1 = '0'
            for a in Groups1Check:
                Groups1 += ','+str(a.id)

        if Groups[1:-1]:
            Groups = Groups[1:-1].split(',')
            Groups = list(map(int, Groups))
        Brands = request.GET.get('Brands', None)
        # Brands1 = Brands[1:-1]
        if Brands[1:-1]:
            Brands = Brands[1:-1].split(',')
            Brands = list(map(int, Brands))
        nb_page_items = request.GET.get('nb_page_items', None)
        pc1 = request.GET.get('pc1', None)
        if pc1[1:-1]:
            pc1 = pc1[1:-1].split(',')
            pc1 = list(map(int, pc1))
        pc2 = request.GET.get('pc2', None)
        if pc2[1:-1]:
            pc2 = pc2[1:-1].split(',')
            pc2 = list(map(int, pc2))
        pc3 = request.GET.get('pc3', None)
        if pc3[1:-1]:
            pc3 = pc3[1:-1].split(',')
            pc3 = list(map(int, pc3))

        if int(nb_page_items) == 24:
            f1 = 0
            f2 = 24
        elif int(nb_page_items) == 48:
            f1 = 0
            f2 = 48
        else:
            f1 = 0
            f2 = 1000

        selectProductSort = request.GET.get('selectProductSort', None)

        if selectProductSort == 'quantity:desc':
            f3 = '-cost__priceoff'
        elif selectProductSort == 'price:asc':
            f3 = 'cost__priceoff'
        elif selectProductSort == 'price:desc':
            f3 = '-cost__priceoff'
        elif selectProductSort == 'name:asc':
            f3 = 'name'
        elif selectProductSort == 'name:desc':
            f3 = '-name'
        elif selectProductSort == 'reference:asc':
            f3 = 'group'
        elif selectProductSort == 'reference:desc':
            f3 = '-group'

        userid = request.user.id
        # if len(Groups1)>0 :
        #productsgroups2 = productsgroups.objects.raw('select * from productsgroups a where glevel=2')
        #productsgroups3 = productsgroups.objects.raw('select * from productsgroups a where (id in ({id}) or gparentid in ({id}) or gparentid in (select gparentid from productsgroups where id in ({id}))) and glevel=3'.format(id=id))
        # else :
        #     productsgroups2 = productsgroups.objects.raw('select * from productsgroups a where gparentid in ({Groups1}) and gparentid in (select id from productsgroups where gparentid=0)'.format(Groups1=0))
        #     productsgroups3 = productsgroups.objects.raw('select * from productsgroups a where gparentid in ({Groups1}) and gparentid in (select id from productsgroups where gparentid in (select id from productsgroups where gparentid=0))'.format(Groups1=0))

        # productsgroups2Html=''
        # productsgroups3Html=''

        # for a in productsgroups2:
        #     checked=''

        #     if str(a.id) in list(Groups1.split(",")):
        #         checked='checked'
        #     productsgroups2Html += """<div class="checkbox SubGroup2in">                  <label class="col-12 "><input type="checkbox" rel="{id}" onchange="change();" {checked} />{Group_Name}<label></div>""".format(id=a.id,Group_Name=a.Group_Name,checked=checked)
        # for a in productsgroups3:
        #     checked=''
        #     if str(a.id) in list(Groups1.split(",")):
        #         checked='checked'
        #     productsgroups3Html += """<div class="checkbox SubGroup2in">                  <label class="col-12 "><input type="checkbox" rel="{id}" onchange="change({gid});" {checked} />{Group_Name}<label></div>""".format(id=a.id,Group_Name=a.Group_Name,checked=checked,gid=id)

        # if len(Groups1) == 0 and len(Brands1) > 0:
        #     productsFiltered = products.objects.raw(
        #         'select *,(select isnull(priceoff,0) from cost where pid_id=a.id) cost,(select Group_Name from productsgroups where id=a.group_id) GroupName from products a where brand_id in ({Brands1}) and group_id in (select id from productsgroups  where  (id in ({id}) or gparentid in ({id}) or gparentid in (select gparentid from productsgroups where id in ({id}))) and glevel=3 ) order by {f3} offset {f1} rows fetch next {f2} rows only'.format(Brands1=Brands1, id=id,f1=f1,f2=f2,f3=f3))
        # elif len(Groups1) > 0 and len(Brands1) == 0:
        #     productsFiltered = products.objects.raw('with tmp0 as (select * from productsgroups  where  id in ({Groups1})union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=2 )),tmp as(select * from productsgroups  where  id in ({Groups1}) union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and id not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 ) union all select * from productsgroups a where glevel=3 and gparentid in (select id from tmp0) and gparentid not in (select gparentid from productsgroups where id in (select id from tmp0) and glevel=3 ))select *,(select isnull(priceoff,0) from cost where pid_id=a.id) cost,(select Group_Name from productsgroups where id=a.group_id) GroupName from products a where group_id in (select id from tmp) order by {f3} offset {f1} rows fetch next {f2} rows only'.format(Groups1=Groups1,f1=f1,f2=f2,f3=f3))
        # elif len(Groups1) == 0 and len(Brands1) == 0:
        #     productsFiltered = products.objects.raw(
        #         'select *,(select isnull(priceoff,0) from cost where pid_id=a.id) cost,(select Group_Name from productsgroups where id=a.group_id) GroupName from products a where group_id in (select id from productsgroups  where  (id in ({id}) or gparentid in ({id}) or gparentid in (select gparentid from productsgroups where id in ({id}))) and glevel=3 ) order by {f3} offset {f1} rows fetch next {f2} rows only'.format(id=id,f1=f1,f2=f2,f3=f3))
        # else:
        #     productsFiltered = products.objects.raw('with tmp0 as (select * from productsgroups  where  id in ({Groups1})union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=2 )),tmp as(select * from productsgroups  where  id in ({Groups1}) union all select * from productsgroups a where glevel=3 and gparentid in ({Groups1}) and gparentid not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 )union all select * from productsgroups a where glevel=2 and gparentid in ({Groups1}) and id not in (select gparentid from productsgroups where id in ({Groups1}) and glevel=3 ) union all select * from productsgroups a where glevel=3 and gparentid in (select id from tmp0) and gparentid not in (select gparentid from productsgroups where id in (select id from tmp0) and glevel=3 ))select *,(select isnull(priceoff,0) from cost where pid_id=a.id) cost,(select Group_Name from productsgroups where id=a.group_id) GroupName from products a where group_id in (select id from tmp) and brand_id in ({Brands1}) order by {f3} offset {f1} rows fetch next {f2} rows only'.format(Groups1=Groups1, Brands1=Brands1,f1=f1,f2=f2,f3=f3))

        gparentid = productsgroups.objects.get(id=id).gparentid
        productsFiltered = products.objects.filter(Q(group_id=int(id)) | Q(group__gparentid=int(
            id)) | Q(group_id=int(gparentid)) | Q(group__gparentid=int(gparentid)))

        try:
            productsFiltered = products.objects.filter(
                Q(group__gparentid__in=Groups) | Q(group_id__in=Groups))
        except:
            pass

        try:
            productsFiltered = productsFiltered.filter(Q(brand_id__in=Brands))
        except:
            pass
        # productslist=[]
        # for a in productsFiltered:
        #     productslist.append(a.id)
        try:
            productsFiltered = productsFiltered.filter(cname1_id__in=list(pc1))
        except:
            pass
        try:
            productsFiltered = productsFiltered.filter(cname2_id__in=list(pc2))
        except:
            pass
        try:
            productsFiltered = productsFiltered.filter(cname3_id__in=list(pc3))
        except:
            pass

        # productsFiltered=productsFiltered.annotate(cost=sum('cost__priceoff'))

        try:
            productsFiltered = productsFiltered.all().order_by('{}'.format(f3))
            productsFilteredCount = productsFiltered.all().order_by('{}'.format(f3))
        except:
            pass

        try:
            productsFiltered = productsFiltered.all()[f1:f2]
        except:
            pass

        ProductsHtml = ''
        productsFilteredCountKol = 0
        for a in productsFilteredCount:
            productsFilteredCountKol += 1
        productsFilteredCount = 0
        for a in productsFiltered:
            productsFilteredCount += 1
            b = cost.objects.filter(pid_id=a.id)
            d = ''
            e = ''
            for c in b:
                d = str(c.priceoff)+'تومان '
                e = c.priceorg
            ProductsHtml += """<div style="display: inline-block;"                            class="product col-lg-3 col-md-3 col-6 border shadow rounded">                            <figure class="product-media ">                                <a href="/category/productlist/showproduct/{id}/">                                    <img   style="width: 100%; height: 200px;" src="/static/media/{img1}" alt="تصویر محصول"                                        class="product-image">                                </a>                                <div class="product-action-vertical">                                    <div onclick="addّFavorite({id},'{name}','{img1}')"                                        class="btn-product-icon btn-wishlist btn-expandable" style="cursor: pointer;">                                        <span>افزودن                                            به لیست علاقه مندی</span></div>                                </div><!-- End .product-action -->                                <div class="product-action action-icon-top">                                    <div onclick="addbascket({id},'{name}','{img1}')"                                        style="cursor: pointer;" class="text-decoration-none btn-product btn-cart"                                        title="افزودن به سبد خرید"><span>افزودن به سبد                                            خرید</span></div>                                </div><!-- End .product-action -->                            </figure><!-- End .product-media -->                            <div class="product-body">                                <div class="product-cat">                                    <a href="#">گروه محصول : {group}                                                                            </a>                                </div><!-- End .product-cat -->                                <h3 class="product-title"><a href="/category/productlist/showproduct/{id}/">نام کالا :                                        {name}</a></h3>                                <h3 class="product-title"><a href="#">برند کالا :                                        {brand}</a></h3>                                <!-- End .product-title -->                                <div class="product-price">                                                                    <span class="new-price">{priceoff}</span> <span class="old-price">{priceorg}</span>                                                                                                                                     </div><!-- End .product-price -->                                <div class="ratings-container">                                    <div class="ratings">                                        <div class="ratings-val" style="width: 0%;"></div>                                        <!-- End .ratings-val -->                                    </div><!-- End .ratings -->                                    <span class="ratings-text">( 0 دیدگاه )</span>                            </div><!-- End .rating-container -->                            </div><!-- End .product-body -->                        </div><!-- End .product -->""".format(id=a.id, img1=a.img1, name=a.name, group=a.group, brand=a.brand, priceoff=d, priceorg=e)
        data = {
            'filterd': True, 'ProductsHtml': ProductsHtml, 'productsFilteredCount': productsFilteredCount, 'productsFilteredCountKol': productsFilteredCountKol
        }
        return JsonResponse(data)


class ProductCategoryJson(View):
    def get(self, request):
        Groups = request.GET.get('Groups', None)
        userid = request.user.id
        gp = productsgroups.objects.filter(id=Groups)
        for g in gp:
            d1 = productscategory.objects.filter(cparentid=g.cname1_id)
            d2 = productscategory.objects.filter(cparentid=g.cname2_id)
            d3 = productscategory.objects.filter(cparentid=g.cname3_id)
            html1 = '<option value="">-----</option>'
            categoryname1 = str(g.cname1)
            for h in d1:
                html1 += '<option value="{id}">{cname}</option>'.format(
                    id=h.id, cname=h.cname)
            html2 = '<option value="">-----</option>'
            categoryname2 = str(g.cname2)
            for h in d2:
                html2 += '<option value="{id}">{cname}</option>'.format(
                    id=h.id, cname=h.cname)
            html3 = '<option value="">-----</option>'
            categoryname3 = str(g.cname3)
            for h in d3:
                html3 += '<option value="{id}">{cname}</option>'.format(
                    id=h.id, cname=h.cname)
        data = {
            'filterd': True, 'html1': html1, 'html2': html2, 'html3': html3, 'categoryname1': categoryname1, 'categoryname2': categoryname2, 'categoryname3': categoryname3}
        return JsonResponse(data)

class searchcustomerJson(View):
    def get(self, request):
        serachstatement = request.GET.get('serachstatement', None)
        if serachstatement:
            CustomersResult = Customers.objects.filter(Name__icontains=serachstatement)
        else:
            CustomersResult = Customers.objects.all()
            
        html1=''
        for g in CustomersResult:
            html1 += '<option value="{id}">{cname}</option>'.format(id=g.id, cname=g.Name)
        html1 += '<option value="">---------------------------------------------------------------------------------------------------</option>'
        data = {
            'filterd': True, 'html1': html1 }
        return JsonResponse(data)

@login_required(login_url='login')
def userschangeinfo(request):
    success = []
    userid = request.user.id
    edit_user = get_object_or_404(User, pk=userid)
    userinfo = usersinfoupdate(request.POST, request.FILES, instance=edit_user)
    if request.method == 'POST':
        if userinfo.is_valid():
            userinfo.save()
            success.append('کاربر گرامی اطلاعات شما با موفقیت ذخیره گردید .')
            userinfo = usersinfoupdate(instance=edit_user)
            return render(request, 'partials/userschangeinfo.html', {'userinfo': userinfo, 'success': success})
    userinfo = usersinfoupdate(instance=edit_user)
    return render(request, 'partials/userschangeinfo.html', {'userinfo': userinfo, 'success': success})



class resetpass(View):
    def get(self, request):
        tel = request.GET.get('tel', None)
        userforget =request.GET.get('userforget', None)
        filterd=False
        if User.objects.filter(cellphone=tel,username=userforget):
            newpass = createpass(tel)
            newpasshash =make_password(newpass)
            User.objects.filter(cellphone=tel,username=userforget).update(password=newpasshash)
            filterd=True
        data = {'filterd': filterd }
        return JsonResponse(data)