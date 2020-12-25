from django import forms
from django.contrib.auth.models import User
from WebSite.models import *
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q


# from persiandate.widgets import PersianDateInput
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control text-input', 'placeholder': 'نام کاربري'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control text-input', 'placeholder': 'کلمه عبور'}))
    captcha = ReCaptchaField(
        public_key='6Lci9fAZAAAAAILZqsHzf2vqe5DhsbuG8zMKBULo',
        private_key='6Lci9fAZAAAAAIMHxWfCJn-TFmJ6hvtWUqPiXuSR',
        widget=ReCaptchaV2Checkbox(
            attrs={

                'data-size': 'standard',

            },
            api_params={'hl': 'fa', 'onload': 'onLoadFunc'}
        ),
    )

# ايجاد يوزر از سمت کاربر


class RegisterFormClean(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'cellphone',
        ]

    def __init__(self, *args, **kwargs):
        super(RegisterFormClean, self).__init__(*args, **kwargs)
        self.fields['password'] = forms.IntegerField( initial=123 , required=False)
        # self.fields['effdate'].widget.attrs.update(
        #     {'class': 'jalali_date-date form-control', 'required': False})  


class LoginFormmobile(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control text-input', 'placeholder': 'نام کاربري'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control text-input', 'placeholder': 'کلمه عبور'}))
    captcha = ReCaptchaField(
        public_key='6Lci9fAZAAAAAILZqsHzf2vqe5DhsbuG8zMKBULo',
        private_key='6Lci9fAZAAAAAIMHxWfCJn-TFmJ6hvtWUqPiXuSR',
        widget=ReCaptchaV2Checkbox(
            attrs={

                'data-size': 'standard',

            },
            api_params={'hl': 'fa', 'onload': 'onLoadFunc'}
        ),
    )

# ايجاد يوزر از سمت کاربر


class RegistermobileFormClean(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'cellphone',
        ]
    def __init__(self, *args, **kwargs):
        super(RegistermobileFormClean, self).__init__(*args, **kwargs)
        self.fields['password'] = forms.IntegerField( initial=123 , required=False)


class ChangePassword_Admin(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'password',
            'newpass',
        ]
        widgets = {
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'newpass': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ChangePassword_User(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'password',
            'newpass',
            'oldpassword',
        ]
        widgets = {
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'newpass': forms.TextInput(attrs={'class': 'form-control'}),
            'oldpassword': forms.TextInput(attrs={'class': 'form-control'}),
        }


# ايجاد يوزر بوسيله ادمين
class userinfocreate(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'avatar',
            'cellphone',
            'is_staff',
            'is_superuser',
            'customersid',
        ]
        widgets = {
            'customersid': forms.Select(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'cellphone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class userinfoupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(userinfoupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['username'].queryset = User.objects.all()

    def save(self, commit=True):
        instance = super(userinfoupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'avatar',
            'cellphone',
            'is_staff',
            'is_superuser',
            'customersid',
        ]
        widgets = {
            'customersid': forms.Select(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'cellphone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class usersinfoupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(usersinfoupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['username'].queryset = User.objects.all()

    def save(self, commit=True):
        instance = super(usersinfoupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'cellphone',

        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'cellphone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ChangePassword_Admin(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'password',
            'newpass',
        ]
        widgets = {
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'newpass': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ChangePassword_User(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'password',
            'newpass',
            'oldpassword',
        ]
        widgets = {
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'newpass': forms.TextInput(attrs={'class': 'form-control'}),
            'oldpassword': forms.TextInput(attrs={'class': 'form-control'}),
        }


# اپ ديت يوزر ايجاد شده توسط ادمين و يا کاربر
class userupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(userupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['username'].queryset = User.objects.all()

    def save(self, commit=True):
        instance = super(userupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'cellphone',
            'is_active',
            'is_staff',
            'is_superuser',
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'cellphone': forms.TextInput(attrs={'class': 'form-control'}),
        }


# اپ ديت يوزر ايجاد شده توسط ادمين و يا کاربر
class user_update(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(user_update, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['username'].queryset = User.objects.all()

    def save(self, commit=True):
        instance = super(user_update, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'cellphone',
            'is_active',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'cellphone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class formslidercreate(forms.ModelForm):
    class Meta:
        model = slider
        fields = [
            'FirstPage_Carousel_pic_1',
            'Create_Uid',
            'Update_Uid'
        ]
        widgets = {
            'FirstPage_Carousel_pic_1': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class formsliderupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formsliderupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['FirstPage_Carousel_pic_1'].queryset = slider.objects.all()

    def save(self, commit=True):
        instance = super(formsliderupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = slider
        fields = [
            'FirstPage_Carousel_pic_1',
            'Create_Uid',
            'Update_Uid'
        ]
        widgets = {
            'FirstPage_Carousel_pic_1': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }



class insideslidercreate(forms.ModelForm):
    class Meta:
        model = insideslider
        fields = [
            'slide',
            'Create_Uid',
            'Update_Uid'
        ]
        widgets = {
            'slide': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class insidesliderupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(insidesliderupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['slide'].queryset = insideslider.objects.all()

    def save(self, commit=True):
        instance = super(insidesliderupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = insideslider
        fields = [
            'slide',
            'Create_Uid',
            'Update_Uid'
        ]
        widgets = {
            'slide': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class productsgroupsform(forms.ModelForm):
    class Meta:
        model = productsgroups
        fields = ['gparentid', 'glevel', 'group_img', 'Group_Name', 'Group_Desc', 'Group_Desc_1',
                  'group_img_1', 'Create_Uid', 'Update_Uid', 'cname1', 'cname2', 'cname3']
        widgets = {
            'cname1': forms.Select(attrs={'class': 'form-control'}),
            'cname2': forms.Select(attrs={'class': 'form-control'}),
            'cname3': forms.Select(attrs={'class': 'form-control'}),
            'gparentid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'glevel': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'group_img': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Group_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Group_Desc': forms.Textarea(attrs={'class': 'form-control'}),
            'Group_Desc_1': forms.Textarea(attrs={'class': 'form-control'}),
            'group_img_1': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }

    def __init__(self, *args, **kwargs):
        super(productsgroupsform, self).__init__(*args, **kwargs)
        a = list(productsgroups.objects.all(
        ).values_list('cname1_id', flat=True))
        b = list(productsgroups.objects.all(
        ).values_list('cname2_id', flat=True))
        c = list(productsgroups.objects.all(
        ).values_list('cname3_id', flat=True))
        aa = []
        for i in a:
            if i != None:
                aa.append(i)
        bb = []
        for i in b:
            if i != None:
                bb.append(i)
        cc = []
        for i in c:
            if i != None:
                cc.append(i)
        print(aa, bb, cc)
        self.fields['cname1'].queryset = productscategory.objects.filter(
            ~Q(id__in=bb), ~Q(id__in=cc),  cparentid=0)
        self.fields['cname2'].queryset = productscategory.objects.filter(
            ~Q(id__in=aa), ~Q(id__in=cc),  cparentid=0)
        self.fields['cname3'].queryset = productscategory.objects.filter(
            ~Q(id__in=aa), ~Q(id__in=bb),  cparentid=0)


class productsgroupsFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(productsgroupsFormUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['Group_Name'].queryset = productsgroups.objects.all()
        a = list(productsgroups.objects.all(
        ).values_list('cname1_id', flat=True))
        b = list(productsgroups.objects.all(
        ).values_list('cname2_id', flat=True))
        c = list(productsgroups.objects.all(
        ).values_list('cname3_id', flat=True))
        aa = []
        for i in a:
            if i != None:
                aa.append(i)
        bb = []
        for i in b:
            if i != None:
                bb.append(i)
        cc = []
        for i in c:
            if i != None:
                cc.append(i)
        print(aa, bb, cc)
        self.fields['cname1'].queryset = productscategory.objects.filter(
            ~Q(id__in=bb), ~Q(id__in=cc),  cparentid=0)
        self.fields['cname2'].queryset = productscategory.objects.filter(
            ~Q(id__in=aa), ~Q(id__in=cc),  cparentid=0)
        self.fields['cname3'].queryset = productscategory.objects.filter(
            ~Q(id__in=aa), ~Q(id__in=bb),  cparentid=0)

    def save(self, commit=True):
        instance = super(productsgroupsFormUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = productsgroups
        fields = ['gparentid', 'glevel', 'group_img', 'Group_Name', 'Group_Desc', 'Group_Desc_1',
                  'group_img_1', 'Create_Uid', 'Update_Uid', 'cname1', 'cname2', 'cname3']
        widgets = {
            'cname1': forms.Select(attrs={'class': 'form-control'}),
            'cname2': forms.Select(attrs={'class': 'form-control'}),
            'cname3': forms.Select(attrs={'class': 'form-control'}),
            'gparentid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'glevel': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'group_img': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Group_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Group_Desc': forms.Textarea(attrs={'class': 'form-control'}),
            'Group_Desc_1': forms.Textarea(attrs={'class': 'form-control'}),
            'group_img_1': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class productsForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ['name', 'brand', 'group',  'serial', 'desc', 'img1', 'img2', 'img3', 'desc_1', 'img_desc_1', 'desc_2', 'img_desc_2', 'desc_3', 'img_desc_3',
                  'img4', 'img5', 'img6', 'Create_Uid', 'Update_Uid', 'cname1', 'cname2', 'cname3',
                   'guarantee', 'supportaftersale',  'supportaftersalecount' , 'guaranteecount','numberofgoods','goods']
        widgets = {
            'cname1': forms.Select(attrs={'class': 'form-control'}),
            'cname2': forms.Select(attrs={'class': 'form-control'}),
            'cname3': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'serial': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'img1': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'img2': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'img3': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'img4': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'img5': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'img6': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'desc_1': forms.Textarea(attrs={'class': 'form-control'}),
            'img_desc_1': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'desc_2': forms.Textarea(attrs={'class': 'form-control'}),
            'img_desc_2': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'desc_3': forms.Textarea(attrs={'class': 'form-control'}),
            'img_desc_3': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'guarantee': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'goods': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'supportaftersale': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'guaranteecount': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'numberofgoods': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'supportaftersalecount': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class productsFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(productsFormUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['name'].queryset = products.objects.all()
            # c1,c2,c3=-1,-1,-1
            # try:
            #     if self.instance.cname1_id:
            #         c1=productscategory.objects.get(id=self.instance.cname1_id).cparentid
            #         self.fields['cname1'].queryset = productscategory.objects.filter(cparentid=c1)
            # except:
            #     pass
            # try:
            #     if self.instance.cname2_id:
            #         c2=productscategory.objects.get(id=self.instance.cname2_id).cparentid

            #         self.fields['cname2'].queryset = productscategory.objects.filter(cparentid=c2)
            # except:
            #     pass
            # try:
            #     if self.instance.cname3_id:
            #         c3=productscategory.objects.get(id=self.instance.cname3_id).cparentid
            #         self.fields['cname3'].queryset = productscategory.objects.filter(cparentid=c3)
            # except:
            #     pass

            # a=productsgroups.objects.get(id=self.instance.group_id).cname1_id
            # b=productsgroups.objects.get(id=self.instance.group_id).cname2_id
            # c=productsgroups.objects.get(id=self.instance.group_id).cname3_id
            # self.fields['cname1'].queryset = productscategory.objects.filter(cparentid=a)
            # self.fields['cname2'].queryset = productscategory.objects.filter(cparentid=b)
            # self.fields['cname3'].queryset = productscategory.objects.filter(cparentid=c)

    def save(self, commit=True):
        instance = super(productsFormUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = products
        fields = ['name', 'brand', 'group',  'serial', 'desc', 'img1', 'img2', 'img3', 'desc_1', 'img_desc_1', 'desc_2', 'img_desc_2', 'desc_3', 'img_desc_3',
                  'img4', 'img5', 'img6', 'Create_Uid', 'Update_Uid', 'cname1', 'cname2', 'cname3',
                   'guarantee', 'supportaftersale',  'supportaftersalecount' , 'guaranteecount','numberofgoods','goods']
        widgets = {
            'cname1': forms.Select(attrs={'class': 'form-control'}),
            'cname2': forms.Select(attrs={'class': 'form-control'}),
            'cname3': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'serial': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'img1': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'img2': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'img3': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'img4': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'img5': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'img6': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'desc_1': forms.Textarea(attrs={'class': 'form-control'}),
            'img_desc_1': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'desc_2': forms.Textarea(attrs={'class': 'form-control'}),
            'img_desc_2': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'desc_3': forms.Textarea(attrs={'class': 'form-control'}),
            'img_desc_3': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'guarantee': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'goods': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'supportaftersale': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'guaranteecount': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'numberofgoods': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'supportaftersalecount': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class productsbrandsform(forms.ModelForm):
    class Meta:
        model = productsbrands
        fields = ['name', 'img', 'Create_Uid', 'Update_Uid']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }

        def __init__(self, Create_Uid, Update_Uid, *args, **kwargs):
            super(productsbrandsform, self).__init__(*args, **kwargs)
            self.Create_Uid = Create_Uid
            self.Update_Uid = Update_Uid


class productsbrandsUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(productsbrandsUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['name'].queryset = productsbrands.objects.all()

    def save(self, commit=True):
        instance = super(productsbrandsUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = productsbrands
        fields = ['name', 'img', 'Create_Uid', 'Update_Uid']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class costForm(forms.ModelForm):
    class Meta:
        model = cost
        fields = ['pid', 'priceorg', 'priceoff', 'desc',
                  'specialcell',  'Create_Uid', 'Update_Uid']
        widgets = {
            'pid': forms.Select(attrs={'class': 'form-control'}),
            'priceorg': forms.TextInput(attrs={'class': 'form-control'}),
            'priceoff': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'specialcell': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(costForm, self).__init__(*args, **kwargs)
    #     self.fields['effdate'] = JalaliDateField(widget=AdminJalaliDateWidget)
    #     self.fields['effdate'].widget.attrs.update(
    #         {'class': 'jalali_date-date form-control', 'required': False})


class costFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(costFormUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['priceorg'].queryset = cost.objects.all()

    def save(self, commit=True):
        instance = super(costFormUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = cost
        fields = ['pid', 'priceorg', 'priceoff', 'desc',
                  'specialcell',  'Create_Uid', 'Update_Uid']
        widgets = {
            'pid': forms.Select(attrs={'class': 'form-control'}),
            'priceorg': forms.TextInput(attrs={'class': 'form-control'}),
            'priceoff': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'specialcell': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(costFormUpdate, self).__init__(*args, **kwargs)
    #     self.fields['effdate'] = JalaliDateField(
    #         widget=AdminJalaliDateWidget  # optional, for user default datepicker
    #     )
    #     self.fields['effdate'].widget.attrs.update(
    #         {'class': 'jalali_date-date form-control text-center', 'required': False})


class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['pid', 'com', 'status', 'Create_Uid', 'Update_Uid']
        widgets = {
            'pid': forms.Select(attrs={'class': 'form-control'}),
            'com': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class commentFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(commentFormUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['pid'].queryset = comment.objects.all()

    def save(self, commit=True):
        instance = super(commentFormUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = comment
        fields = ['pid', 'com', 'status', 'Create_Uid', 'Update_Uid']
        widgets = {
            'pid': forms.Select(attrs={'class': 'form-control'}),
            'com': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class commentdetailsform(forms.ModelForm):
    class Meta:
        model = commentdetails
        fields = ['cid', 'like', 'dislike', 'Create_Uid', 'Update_Uid']
        widgets = {

            'cid': forms.Select(attrs={'class': 'form-control type', 'onchange': "FormControl();"}),
            'like':  forms.CheckboxInput(attrs={'class': 'form-control'}),
            'dislike':  forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class commentdetailsformUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(commentdetailsformUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['cid'].queryset = commentdetails.objects.all()

    def save(self, commit=True):
        instance = super(commentdetailsformUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = commentdetails
        fields = ['cid', 'like', 'dislike', 'Create_Uid', 'Update_Uid']
        widgets = {
            'cid': forms.Select(attrs={'class': 'form-control type', 'onchange': "FormControl();"}),
            'like':  forms.CheckboxInput(attrs={'class': 'form-control'}),
            'dislike':  forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class productdetailsForm(forms.ModelForm):
    class Meta:
        model = productdetails
        fields = ['favorite', 'Create_Uid', 'Update_Uid']
        widgets = {
            'pid': forms.Select(attrs={'class': 'form-control type', 'onchange': "FormControl();"}),
            'favorite':  forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class productdetailsFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(productdetailsFormUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['pid'].queryset = productdetails.objects.all()

    def save(self, commit=True):
        instance = super(productdetailsFormUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = productdetails
        fields = ['favorite', 'Create_Uid', 'Update_Uid']
        widgets = {
            'pid': forms.Select(attrs={'class': 'form-control type', 'onchange': "FormControl();"}),
            # 'StarRating':  forms.IntegerField(),
            'favorite':  forms.CheckboxInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class sellbascketForm(forms.ModelForm):
    class Meta:
        model = sellbascket
        fields = ['pid', 'status', 'Create_Uid', 'Update_Uid']
        widgets = {
            'pid': forms.Select(attrs={'class': 'form-control type', 'onchange': "FormControl();"}),
            'status':  forms.TextInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class sellbascketFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(sellbascketFormUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['pid'].queryset = sellbascket.objects.all()

    def save(self, commit=True):
        instance = super(sellbascketFormUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = sellbascket
        fields = ['pid', 'status', 'Create_Uid', 'Update_Uid']
        widgets = {
            'pid': forms.Select(attrs={'class': 'form-control type', 'onchange': "FormControl();"}),
            'status':  forms.TextInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class firstpagebanersform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(firstpagebanersform, self).__init__(*args, **kwargs)
        self.fields['group1'].queryset = productsgroups.objects.filter(glevel=3)
        self.fields['group2'].queryset = productsgroups.objects.filter(glevel=3)
        self.fields['group3'].queryset = productsgroups.objects.filter(glevel=3)
        self.fields['group4'].queryset = productsgroups.objects.filter(glevel=3)
        self.fields['group5'].queryset = productsgroups.objects.filter(glevel=3)
        self.fields['group6'].queryset = productsgroups.objects.filter(glevel=3)
        self.fields['group7'].queryset = productsgroups.objects.filter(glevel=3)
        self.fields['group8'].queryset = productsgroups.objects.filter(glevel=3)
        self.fields['group9'].queryset = productsgroups.objects.filter(glevel=3)
        self.fields['group10'].queryset = productsgroups.objects.filter(glevel=3)
        self.fields['group11'].queryset = productsgroups.objects.filter(glevel=3)
    class Meta:
        model = firstpagebaners
        fields = ['baner1', 'baner2', 'baner3', 'baner4', 'baner5', 'baner6', 'baner7', 'baner8', 'baner9', 'baner10', 'baner11',
                  'group1', 'group2', 'group3', 'group4', 'group5', 'group6', 'group7', 'group8', 'group9', 'group10', 'group11',
                  'Create_Uid', 'Update_Uid']
        widgets = {
            'baner1': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner2': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner3': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner4': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner5': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner6': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner7': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner8': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner9': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner10': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner11': forms.FileInput(attrs={'class': 'img-thumbnail'}),

            'group1': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group2': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group3': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group4': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group5': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group6': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group7': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group8': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group9': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group10': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group11': forms.Select(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class firstpagebanersFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(firstpagebanersFormUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['baner1'].queryset = firstpagebaners.objects.all()
            self.fields['group1'].queryset = productsgroups.objects.filter(glevel=3)
            self.fields['group2'].queryset = productsgroups.objects.filter(glevel=3)
            self.fields['group3'].queryset = productsgroups.objects.filter(glevel=3)
            self.fields['group4'].queryset = productsgroups.objects.filter(glevel=3)
            self.fields['group5'].queryset = productsgroups.objects.filter(glevel=3)
            self.fields['group6'].queryset = productsgroups.objects.filter(glevel=3)
            self.fields['group7'].queryset = productsgroups.objects.filter(glevel=3)
            self.fields['group8'].queryset = productsgroups.objects.filter(glevel=3)
            self.fields['group9'].queryset = productsgroups.objects.filter(glevel=3)
            self.fields['group10'].queryset = productsgroups.objects.filter(glevel=3)
            self.fields['group11'].queryset = productsgroups.objects.filter(glevel=3)

    def save(self, commit=True):
        instance = super(firstpagebanersFormUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = firstpagebaners
        fields = ['baner1', 'baner2', 'baner3', 'baner4', 'baner5', 'baner6', 'baner7', 'baner8', 'baner9', 'baner10', 'baner11',
                  'group1', 'group2', 'group3', 'group4', 'group5', 'group6', 'group7', 'group8', 'group9', 'group10', 'group11',
                  'Create_Uid', 'Update_Uid']
        widgets = {
            'baner1': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner2': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner3': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner4': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner5': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner6': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner7': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner8': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner9': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner10': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'baner11': forms.FileInput(attrs={'class': 'img-thumbnail'}),

            'group1': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group2': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group3': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group4': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group5': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group6': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group7': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group8': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group9': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group10': forms.Select(attrs={'class': 'img-thumbnail'}),
            'group11': forms.Select(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class firstpagehlform(forms.ModelForm):
    class Meta:
        model = firstpagelogo
        fields = ['Logo', 'Create_Uid', 'Update_Uid']
        widgets = {
            'Logo': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class firstpagehlUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(firstpagehlUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['Logo'].queryset = firstpagelogo.objects.all()

    def save(self, commit=True):
        instance = super(firstpagehlUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = firstpagelogo
        fields = ['Logo', 'Create_Uid', 'Update_Uid']
        widgets = {
            'Logo': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class aboutusp1Form(forms.ModelForm):
    class Meta:
        model = aboutusp1
        fields = ['whoweare', 'teamimg', 'Create_Uid', 'Update_Uid']
        widgets = {
            'whoweare': forms.Textarea(attrs={'class': 'form-control'}),
            'teamimg': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class aboutusp1FormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(aboutusp1FormUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['whoweare'].queryset = aboutusp1.objects.all()

    def save(self, commit=True):
        instance = super(aboutusp1FormUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = aboutusp1
        fields = ['whoweare', 'teamimg', 'Create_Uid', 'Update_Uid']
        widgets = {
            'whoweare': forms.Textarea(attrs={'class': 'form-control'}),
            'teamimg': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class aboutusForm(forms.ModelForm):
    class Meta:
        model = aboutus
        fields = ['personelimg', 'pposision',
                  'ptitle', 'Create_Uid', 'Update_Uid']
        widgets = {
            'personelimg': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'pposision': forms.TextInput(attrs={'class': 'form-control'}),
            'ptitle': forms.TextInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class aboutusFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(aboutusFormUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['pposision'].queryset = aboutus.objects.all()

    def save(self, commit=True):
        instance = super(aboutusFormUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = aboutus
        fields = ['personelimg', 'pposision',
                  'ptitle', 'Create_Uid', 'Update_Uid']
        widgets = {
            'personelimg': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'pposision': forms.TextInput(attrs={'class': 'form-control'}),
            'ptitle': forms.TextInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class centercontactusForm(forms.ModelForm):
    class Meta:
        model = centercontactus
        fields = ['internetsaletitle', 'internetsaledesc', 'internetimg', 'callinfo', 'address', 'tell', 'email', 'wtworkstart', 'tell2', 'mobile', 'fax',
                  'wtworkend', 'ltworkstart', 'ltworkend', 'Create_Uid', 'Update_Uid']
        widgets = {
            'callinfo': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'tell': forms.TextInput(attrs={'class': 'form-control'}),
            'tell2': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'fax': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'wtworkstart': forms.TextInput(attrs={'class': 'form-control'}),
            'wtworkend': forms.TextInput(attrs={'class': 'form-control'}),
            'ltworkstart': forms.TextInput(attrs={'class': 'form-control'}),
            'ltworkend': forms.TextInput(attrs={'class': 'form-control'}),
            'internetsaletitle': forms.TextInput(attrs={'class': 'form-control'}),
            'internetsaledesc': forms.Textarea(attrs={'class': 'form-control'}),
            'internetimg': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class centercontactusFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(centercontactusFormUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['callinfo'].queryset = centercontactus.objects.all()

    def save(self, commit=True):
        instance = super(centercontactusFormUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = centercontactus
        fields = ['internetsaletitle', 'internetsaledesc', 'internetimg', 'callinfo', 'address', 'tell', 'email', 'wtworkstart', 'tell2', 'mobile', 'fax',
                  'wtworkend', 'ltworkstart', 'ltworkend', 'Create_Uid', 'Update_Uid']
        widgets = {
            'callinfo': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'tell': forms.TextInput(attrs={'class': 'form-control'}),
            'tell2': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'fax': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'wtworkstart': forms.TextInput(attrs={'class': 'form-control'}),
            'wtworkend': forms.TextInput(attrs={'class': 'form-control'}),
            'ltworkstart': forms.TextInput(attrs={'class': 'form-control'}),
            'ltworkend': forms.TextInput(attrs={'class': 'form-control'}),
            'internetsaletitle': forms.TextInput(attrs={'class': 'form-control'}),
            'internetsaledesc': forms.Textarea(attrs={'class': 'form-control'}),
            'internetimg': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class salecontactusForm(forms.ModelForm):
    class Meta:
        model = salecontactus
        fields = ['salecentername', 'centerimg', 'sallinfo', 'saddress', 'stell', 'stell2', 'smobile', 'sfax',
                  'semail', 'swtworkstart', 'swtworkend', 'sltworkstart', 'sltworkend', 'Create_Uid', 'Update_Uid']
        widgets = {
            'centerimg': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'salecentername': forms.TextInput(attrs={'class': 'form-control'}),
            'sallinfo': forms.TextInput(attrs={'class': 'form-control'}),
            'saddress': forms.TextInput(attrs={'class': 'form-control'}),
            'stell': forms.TextInput(attrs={'class': 'form-control'}),
            'stell2': forms.TextInput(attrs={'class': 'form-control'}),
            'smobile': forms.TextInput(attrs={'class': 'form-control'}),
            'sfax': forms.TextInput(attrs={'class': 'form-control'}),
            'semail': forms.TextInput(attrs={'class': 'form-control'}),
            'swtworkstart': forms.TextInput(attrs={'class': 'form-control'}),
            'swtworkend': forms.TextInput(attrs={'class': 'form-control'}),
            'sltworkstart': forms.TextInput(attrs={'class': 'form-control'}),
            'sltworkend': forms.TextInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class salecontactusFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(salecontactusFormUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['sallinfo'].queryset = salecontactus.objects.all()

    def save(self, commit=True):
        instance = super(salecontactusFormUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = salecontactus
        fields = ['salecentername', 'centerimg', 'sallinfo', 'saddress', 'stell', 'semail',
                  'swtworkstart', 'swtworkend', 'sltworkstart', 'sltworkend', 'Create_Uid', 'Update_Uid']
        widgets = {
            'centerimg':  forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'salecentername': forms.TextInput(attrs={'class': 'form-control'}),
            'sallinfo': forms.TextInput(attrs={'class': 'form-control'}),
            'saddress': forms.TextInput(attrs={'class': 'form-control'}),
            'stell': forms.TextInput(attrs={'class': 'form-control'}),
            'semail': forms.TextInput(attrs={'class': 'form-control'}),
            'swtworkstart': forms.TextInput(attrs={'class': 'form-control'}),
            'swtworkend': forms.TextInput(attrs={'class': 'form-control'}),
            'sltworkstart': forms.TextInput(attrs={'class': 'form-control'}),
            'sltworkend': forms.TextInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class customerquestionsForm(forms.ModelForm):
    class Meta:
        model = customerquestions
        fields = ['name', 'title', 'tell', 'email',
                  'desc', 'Create_Uid', 'Update_Uid']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tell': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class customerquestionsFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(customerquestionsFormUpdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['name'].queryset = customerquestions.objects.all()

    def save(self, commit=True):
        instance = super(customerquestionsFormUpdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = customerquestions
        fields = ['name', 'title', 'tell', 'email',
                  'desc', 'Create_Uid', 'Update_Uid']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tell': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class sellbascketformcreate(forms.ModelForm):
    class Meta:
        model = sellbascket
        fields = [
            'pid',
            'status',
            'pcount',
            'pprise',
            'pdiscount',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'pid': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'pcount': forms.TextInput(attrs={'class': 'form-control'}),
            'pprise': forms.TextInput(attrs={'class': 'form-control'}),
            'pdiscount': forms.TextInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class sellbascketformupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(sellbascketformupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['pid'].queryset = sellbascket.objects.all()

    def save(self, commit=True):
        instance = super(sellbascketformupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = sellbascket
        fields = [
            'pid',
            'status',
            'pcount',
            'pprise',
            'pdiscount',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'pid': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'pcount': forms.TextInput(attrs={'class': 'form-control'}),
            'pprise': forms.TextInput(attrs={'class': 'form-control'}),
            'pdiscount': forms.TextInput(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class ersalform(forms.ModelForm):
    class Meta:
        model = parametrsersal
        fields = [
            'ersal',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'ersal': forms.Textarea(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class ersalformupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ersalformupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['ersal'].queryset = parametrsersal.objects.all()

    def save(self, commit=True):
        instance = super(ersalformupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = parametrsersal
        fields = [
            'ersal',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'ersal': forms.Textarea(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class osoolform(forms.ModelForm):
    class Meta:
        model = parametrsosool
        fields = [
            'osool',
            'Create_Uid',
            'Update_Uid',

        ]
        widgets = {
            'osool': forms.Textarea(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class osoolformupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(osoolformupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['osool'].queryset = parametrsosool.objects.all()

    def save(self, commit=True):
        instance = super(osoolformupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = parametrsosool
        fields = [
            'osool',
            'Create_Uid',
            'Update_Uid',

        ]
        widgets = {
            'osool': forms.Textarea(attrs={'class': 'form-control'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class filterdate1(forms.ModelForm):
    class Meta:
        model = SPFactor
        fields = [
            'date1',
            'date2',
        ]

    def __init__(self, *args, **kwargs):
        super(filterdate1, self).__init__(*args, **kwargs)
        self.fields['date1'] = JalaliDateField(
            widget=AdminJalaliDateWidget  # optional, for user default datepicker
        )
        self.fields['date1'].widget.attrs.update(
            {'class': 'jalali_date-date  col-lg-12 col-md-12 col-sm-12 col-xs-12 form-control', 'required': False})

        self.fields['date2'] = JalaliDateField(
            widget=AdminJalaliDateWidget  # optional, for user default datepicker
        )
        self.fields['date2'].widget.attrs.update(
            {'class': 'jalali_date-date col-lg-12 col-md-12 col-sm-12 col-xs-12  form-control', 'required': False})


class lastnewsform(forms.ModelForm):
    class Meta:
        model = lastnews
        fields = [
            'title',
            'khdesc',
            'descriptions',
            'newsimg',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'khdesc': forms.TextInput(attrs={'class': 'form-control'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control'}),
            'newsimg': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class lastnewsformupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(lastnewsformupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['title'].queryset = lastnews.objects.all()

    def save(self, commit=True):
        instance = super(lastnewsformupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = lastnews
        fields = [
            'title',
            'khdesc',
            'descriptions',
            'newsimg',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'khdesc': forms.TextInput(attrs={'class': 'form-control'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control'}),
            'newsimg': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class parametsaccountsform(forms.ModelForm):
    class Meta:
        model = parametsaccounts
        fields = [
            'account',
            'accountimg',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'account': forms.TextInput(attrs={'class': 'form-control'}),
            'accountimg': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class parametsaccountsformupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(parametsaccountsformupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['account'].queryset = parametsaccounts.objects.all()

    def save(self, commit=True):
        instance = super(parametsaccountsformupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = parametsaccounts
        fields = [
            'account',
            'accountimg',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'account': forms.TextInput(attrs={'class': 'form-control'}),
            'accountimg': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class parametssasform(forms.ModelForm):
    class Meta:
        model = parametssas
        fields = [
            'title',
            'desc',
            'img',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class parametssasformupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(parametssasformupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['title'].queryset = parametssas.objects.all()

    def save(self, commit=True):
        instance = super(parametssasformupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = parametssas
        fields = [
            'title',
            'desc',
            'img',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class parametssupportform(forms.ModelForm):
    class Meta:
        model = parametssupport
        fields = [
            'title',
            'desc',
            'img',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class parametssupportformupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(parametssupportformupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['title'].queryset = parametssupport.objects.all()

    def save(self, commit=True):
        instance = super(parametssupportformupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = parametssupport
        fields = [
            'title',
            'desc',
            'img',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class productscategoryform(forms.ModelForm):
    class Meta:
        model = productscategory
        fields = [
            'cname',
            'cdesc',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'cname': forms.TextInput(attrs={'class': 'form-control'}),
            'cdesc': forms.Textarea(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class productscategoryformupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(productscategoryformupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['title'].queryset = productscategory.objects.all()

    def save(self, commit=True):
        instance = super(productscategoryformupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = productscategory
        fields = [
            'cname',
            'cdesc',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'cname': forms.TextInput(attrs={'class': 'form-control'}),
            'cdesc': forms.Textarea(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class weblogform(forms.ModelForm):
    class Meta:
        model = weblog
        fields = [
            'title',
            'desc',
            'img',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class weblogformupdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(weblogformupdate, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['title'].queryset = weblog.objects.all()

    def save(self, commit=True):
        instance = super(weblogformupdate, self).save(commit=False)
        if commit:
            instance.save()
            return instance

    class Meta:
        model = weblog
        fields = [
            'title',
            'desc',
            'img',
            'Create_Uid',
            'Update_Uid',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'img-thumbnail'}),
            'Create_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'Update_Uid': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }