from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_jalali.db import models as jmodels
# from django.contrib.auth.models import User


# Create your models here.


class Customers(models.Model):
    FAccId = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    Name = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    Family = models.CharField(default=0,max_length=200, verbose_name=_('نام خانوادگی'), null=True, blank=True)
    CellPhone = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    PhoneNo = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    FaxNo = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    SCode = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    Email = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    EcCode = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    Address = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    ZipCode = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    UserId = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    TRes = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    CSex = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    FPId = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    class Meta:
        verbose_name = _('مشتری')
        verbose_name_plural = _('مشتری ها')
        db_table = 'Customers'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return self.Name


class PayRcvCheck(models.Model):
    CheckId = models.BigIntegerField(default=0, verbose_name=_('کد چک'), null=True, blank=True)
    PayRcvId = models.BigIntegerField(default=0, verbose_name=_('کد رسید'), null=True, blank=True)


    class Meta:
        verbose_name = _('میانی')
        verbose_name_plural = _('میانی ها')
        db_table = 'PayRcvCheck'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return self.CheckId


class Check(models.Model):
    Id2 = models.CharField(default=0,max_length=200,  verbose_name=_('کد چک انتقالی'), null=True, blank=True)
    CheckNo = models.CharField(default=0,max_length=200,  verbose_name=_('شماره چک '), null=True, blank=True)
    CValue = models.CharField(default=0,max_length=200,  verbose_name=_('مبلغ'), null=True, blank=True)
    PayerFAccId = models.CharField(max_length=200,  verbose_name=_('نام پرداخت کننده'), null=True, blank=True)
    CDate = models.CharField(default=0,max_length=1024,  verbose_name=_('تاریخ چک'), null=True, blank=True)
    RcptDate = models.CharField(default=0,max_length=200,  verbose_name=_('تاریخ سررسید'), null=True, blank=True)
    VDate = models.CharField(default=0,max_length=1024,  verbose_name=_('تاریخ'), null=True, blank=True)
    CStatus = models.CharField(default=0,max_length=200,  verbose_name=_('وضعیت چک'), null=True, blank=True)
    CType = models.CharField(default=0,max_length=1024,  verbose_name=_('وضعیت یک'), null=True, blank=True)
    SType = models.CharField(default=0,max_length=1024,  verbose_name=_('وضعیت دو'), null=True, blank=True)
    CId = models.CharField(default=0,max_length=1024,  verbose_name=_('وضعیت دو'), null=True, blank=True)
    
    class Meta:
        verbose_name = _('ریز رسید ')
        verbose_name_plural = _('ریز رسید ها')
        db_table = 'Check'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return self.Id2


class PayRcv(models.Model):
    PNo = models.CharField(default=0,max_length=200,  verbose_name=_('شماره رسید'), null=True, blank=True)
    PayType = models.CharField(default=0,max_length=200,  verbose_name=_('نوع رسید'), null=True, blank=True)
    PDate = models.CharField(default=0,max_length=200,  verbose_name=_('تاریخ رسید'), null=True, blank=True)
    RcvrFAccId = models.CharField(default=0,max_length=200, verbose_name=_('نام خانوادگی'), null=True, blank=True)
    PDesc = models.CharField(default=0,max_length=200,  verbose_name=_('شرح رسید'), null=True, blank=True)
    CustomerId = models.CharField(default=0,max_length=200,  verbose_name=_('نام مشتری'), null=True, blank=True)
    PCValue = models.CharField(default=0,max_length=200,  verbose_name=_('مبلغ'), null=True, blank=True)
    SCommit = models.CharField(default=0,max_length=200,  verbose_name=_('نام مشتری'), null=True, blank=True)
    
    class Meta:
        verbose_name = _('رسید')
        verbose_name_plural = _('رسید ها')
        db_table = 'PayRcv'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return  self.PNo


class SPArticle(models.Model):
    Id2 = models.CharField(default=0,max_length=200,  verbose_name=_('کد فاکتور انتقالی'), null=True, blank=True)
    SPId = models.CharField(default=0,max_length=200,  verbose_name=_('کد فاکتور'), null=True, blank=True)
    MerchandiseId = models.CharField(default=0,max_length=200,  verbose_name=_('کد کالا'), null=True, blank=True)
    Merchandisename = models.CharField(max_length=200,  verbose_name=_('نام کالا'), null=True, blank=True)
    Amount = models.IntegerField(default=0, verbose_name=_('تعداد'), null=True, blank=True)
    UnitId = models.CharField(default=0,max_length=200,  verbose_name=_('واحد شمارش'), null=True, blank=True)
    UnitPrice = models.IntegerField(default=0,  verbose_name=_('قیمت واحد'), null=True, blank=True)
    AuxAmount = models.CharField(default=0,max_length=200,  verbose_name=_('مقدار فرعی'), null=True, blank=True)
    SPADesc = models.CharField(default=0,max_length=1024,  verbose_name=_('شرح آرتیکل'), null=True, blank=True)
    VTax = models.IntegerField(default=0,  verbose_name=_('مالیات'), null=True, blank=True)
    VCharge = models.IntegerField(default=0,  verbose_name=_('عوارض'), null=True, blank=True)
    Percentage = models.IntegerField(default=0,  verbose_name=_('تخفیف'), null=True, blank=True)
    FPId = models.CharField(default=0,max_length=200,  verbose_name=_('دوره مالی'), null=True, blank=True)
    ATotal = models.BigIntegerField(default=0,  verbose_name=_('جمع کل'), null=True, blank=True) 

    class Meta:
        verbose_name = _('ریز فاکتور ')
        verbose_name_plural = _('ریز فاکتور ها')
        db_table = 'SPArticle'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return self.SPId


class SPFactor(models.Model):
    FactorNo = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    ReferenceNo = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    SPDate = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    FactorType = models.CharField(default=0,max_length=200, verbose_name=_('نام خانوادگی'), null=True, blank=True)
    CustomerId = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    Total = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    Discount = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    Expense = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    SPDesc = models.CharField(default=0,max_length=1024,  verbose_name=_('نام'), null=True, blank=True)
    CustomerName = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    CustomerPhoneNo = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    CustomerEcCode = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    CustomerAddress = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    FPId = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    SC = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    FStatus = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    FactorSubType = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    Committed = models.CharField(default=0,max_length=200,  verbose_name=_('نام'), null=True, blank=True)
    date1 = jmodels.jDateField(default='1300-01-01',  verbose_name=_('تاریخ اول'), null=True, blank=True)
    date2 = jmodels.jDateField(default='1500-01-01',  verbose_name=_('تاریخ دوم'), null=True, blank=True)
    
    class Meta:
        verbose_name = _('فاکتور')
        verbose_name_plural = _('فاکتور ها')
        db_table = 'SPFactor'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return  str(self.date1) and str(self.date2)



class slider(models.Model):
    objects = 'FirstPage_Carousel_pic_1', 'Create_Date', 'Update_Date', 'Create_Uid', 'Update_Uid'
    FirstPage_Carousel_pic_1 = models.ImageField(
        verbose_name='انتخاب عکس', null=False, blank=False)
    Create_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Update_Date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        verbose_name = _('اسلایدر ')
        verbose_name_plural = _('اسلایدر ها')
        db_table = 'slider'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.FirstPage_Carousel_pic_1)


class insideslider(models.Model):
    objects = 'slide', 'Create_Date', 'Update_Date', 'Create_Uid', 'Update_Uid'
    slide = models.ImageField(
        verbose_name='انتخاب عکس', null=False, blank=False)
    Create_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Update_Date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        verbose_name = _('اسلایدر ')
        verbose_name_plural = _('اسلایدر ها')
        db_table = 'insideslider'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.slide)


class productscategory(models.Model):
    onjects = 'cname', 'cparentid', 'cdesc', 'Create_Date', 'Update_Date', 'Create_Uid', 'Update_Uid'

    cname = models.CharField(max_length=100, verbose_name=_('نام دسته بندی'), null=False, blank=False)
    cparentid = models.IntegerField(default=0, verbose_name=_('نام سطح بالادست'), null=True, blank=True)
    cdesc = models.TextField(max_length=100, verbose_name=_('شرح دسته بندی'), null=True, blank=True)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)


    class Meta:
        ordering = ['id']
        verbose_name = _('دسته بندی')
        verbose_name_plural = _('دسته بندی ها')
        db_table = 'productscategory'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.cname)


class productsgroups(models.Model):
    objects = 'gparentid', 'glevel', 'group_img', 'Group_Name', 'Group_Desc', 'Create_Date', 'Update_Date', 'Create_Uid', 'Update_Uid' \
        ,'cname1', 'cname2', 'cname3'

    cname1 = models.ForeignKey(productscategory ,on_delete=models.PROTECT , related_name='cname1', verbose_name=_('نام دسته بندی1') , null=True, blank=True)
    cname2 = models.ForeignKey(productscategory ,on_delete=models.PROTECT , related_name='cname2', verbose_name=_('نام دسته بندی2') , null=True, blank=True)
    cname3 = models.ForeignKey(productscategory ,on_delete=models.PROTECT , related_name='cname3', verbose_name=_('نام دسته بندی3') , null=True, blank=True)
    gparentid = models.IntegerField(default=0, verbose_name=_('کد گروه سطح بالاتر'),null=True, blank=True)
    glevel = models.IntegerField(default=0, verbose_name=_('سطح گروه'), null=True, blank=True)
    group_img = models.ImageField(verbose_name=_('عکس گروه کالا'), null=True, blank=True )
    Group_Name = models.CharField(
        max_length=200, verbose_name=_('نام گروه'), null=True, blank=True)
    Group_Desc = models.TextField(max_length=4000, verbose_name=_(
        'توضیح گروه'), null=True, blank=True)
    Group_Desc_1 = models.TextField(max_length=4000, verbose_name=_(
        'توضیح گروه بالای صفحه جزئیات'), null=True, blank=True)
    group_img_1 = models.ImageField(verbose_name=_('عکس گروه کالا بالای صفحه جزئیات'), null=True, blank=True )
    Create_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Update_Date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('گروه')
        verbose_name_plural = _('گروه ها')
        db_table = 'productsgroups'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return self.Group_Name


class productsbrands(models.Model):
    objects = 'name', 'img', 'Create_Date', 'Update_Date', 'Create_Uid', 'Update_Uid'
    name = models.TextField(
        max_length='200', verbose_name='نام برند', null=False, blank=False)
    img = models.ImageField(verbose_name='تصویر', null=False, blank=False)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('برند محصول')
        verbose_name_plural = _('برند محصول ها')
        db_table = 'productsbrands'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.name)


class products(models.Model):
    objects = 'name','brand', 'serial','group', 'desc', 'img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'Create_Date', \
        'Update_Date', 'Create_Uid', 'Update_Uid', 'cname1', 'cname2', 'cname3', 'guarantee', 'supportaftersale', \
           'supportaftersalecount' , 'guaranteecount','numberofgoods'

    cname1 = models.ForeignKey(productscategory , related_name='cname4',on_delete=models.PROTECT , verbose_name=_('نام دسته بندی1') , null=True, blank=True)
    cname2 = models.ForeignKey(productscategory , related_name='cname5',on_delete=models.PROTECT , verbose_name=_('نام دسته بندی2') , null=True, blank=True)
    cname3 = models.ForeignKey(productscategory , related_name='cname6',on_delete=models.PROTECT , verbose_name=_('نام دسته بندی3') , null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name=_(
        'نام محصول'), null=False, blank=False)
    group = models.ForeignKey(productsgroups, on_delete=models.PROTECT, max_length=200, verbose_name=_('نام گروه'),
                              null=False, blank=False)
    brand = models.ForeignKey(productsbrands, on_delete=models.PROTECT, max_length=200, verbose_name=_('نام برند'),
                              null=False, blank=False)
    serial = models.CharField(max_length=200, verbose_name=_(
        'شماره سریال'), null=False, blank=False)
    desc = models.TextField(max_length=4000, verbose_name=_(
        'توضیحات'), null=True, blank=True)
    guarantee = models.BooleanField(
        default=False, verbose_name=_('گارانتی'), null=True, blank=True)
    guaranteecount = models.IntegerField(default=0, verbose_name=_(
        'مدت گارانتی (به سال)'), null=True, blank=True)    
    supportaftersale = models.BooleanField(
        default=False, verbose_name=_('خدمات پس از فروش'), null=True, blank=True)
    supportaftersalecount = models.IntegerField(default=0, verbose_name=_(
        'مدت خدمات پس از فروش (به سال)'), null=True, blank=True) 
    goods = models.BooleanField(
        default=0, verbose_name=_('موجودی'), null=False, blank=False) 
    numberofgoods = models.IntegerField(default=0, verbose_name=_(
        'تعداد کالا'), null=False, blank=False) 
    img1 = models.ImageField(verbose_name='تصویر1', null=False, blank=False)
    img2 = models.ImageField(verbose_name='تصویر2', null=True, blank=True)
    img3 = models.ImageField(verbose_name='تصویر3', null=True, blank=True)
    img4 = models.ImageField(verbose_name='تصویر4', null=True, blank=True)
    img5 = models.ImageField(verbose_name='تصویر5', null=True, blank=True)
    img6 = models.ImageField(verbose_name='تصویر6', null=True, blank=True)

    desc_1 = models.TextField(max_length=4000, verbose_name=_(
        'درباره محصول شرح 1'), null=True, blank=True)
    img_desc_1 = models.ImageField(verbose_name=' عکس شرح 1', null=True, blank=True)
    desc_2 = models.TextField(max_length=4000, verbose_name=_(
        'درباره محصول شرح 2'), null=True, blank=True)
    img_desc_2 = models.ImageField(verbose_name='عکس شرح 2', null=True, blank=True)
    desc_3 = models.TextField(max_length=4000, verbose_name=_(
        'توضیحات محصول'), null=True, blank=True)
    img_desc_3 = models.ImageField(verbose_name='عکس توضیحات محصول', null=True, blank=True)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('محصول')
        verbose_name_plural = _('محصول ها')
        db_table = 'products'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return self.name


class cost(models.Model):
    objects = 'pid', 'priceorg', 'priceoff', 'desc', 'specialcell', 'effdate', 'Create_Date', 'Update_Date', 'Create_Uid', 'Update_Uid'
    pid = models.ForeignKey(products, on_delete=models.PROTECT,  verbose_name=_('نام محصول'),
                            null=False, blank=False)
    priceorg = models.BigIntegerField(verbose_name=_(
        'قیمت محصول'), null=True, blank=True)
    priceoff = models.BigIntegerField(verbose_name=_(
        'قیمت محصول پس از تخفیف'), null=False, blank=False)
    desc = models.TextField(max_length=4000, verbose_name=_(
        'توضیحات'), null=True, blank=True)
    specialcell = models.BooleanField(
        default=0, verbose_name=_('فروش ویژه'), null=True, blank=True)
    effdate = jmodels.jDateField(
        default='1900-01-01', verbose_name=_('تاریخ موثر'), null=True, blank=True)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('قیمت')
        verbose_name_plural = _('قیمت ها')
        db_table = 'cost'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.priceorg)


class comment(models.Model):
    objects = 'pid', 'com', 'status', 'Create_Date', 'Update_Date', 'Create_Uid', 'Update_Uid'
    statustypes = [
        (0, 'پیش نویس'),
        (1, 'تایید شده'),
        (2, 'رد شده'),
    ]
    pid = models.ForeignKey(products, on_delete=models.PROTECT, verbose_name=_('کد محصول'),
                            null=False, blank=False)
    Head = models.TextField(max_length=400, verbose_name=_(
        'تیتر'), null=True, blank=True)
    com = models.TextField(max_length=4000, verbose_name=_(
        'توضیحات'), null=True, blank=True)
    status = models.IntegerField(choices=statustypes, default=0, verbose_name=_(
        'وضعیت کامنت'), null=False, blank=False)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('کامنت')
        verbose_name_plural = _('کامنت ها')
        db_table = 'comment'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.pid)


class commentdetails(models.Model):
    objects = 'cid', 'like', 'dislike', 'Create_Date', 'Update_Date', 'Create_Uid', 'Update_Uid'
    cid = models.ForeignKey(comment, on_delete=models.PROTECT, max_length=200, verbose_name=_('کد کامنت'),
                            null=False, blank=False)
    com = models.TextField(max_length=4000, verbose_name=_(
        'توضیحات'), null=True, blank=True)
    like = models.BooleanField(default=0, verbose_name='دوست داشتم')
    dislike = models.BooleanField(default=0, verbose_name='دوست نداشتم')
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('اعتبار کامنت')
        verbose_name_plural = _('اعتبار کامنت ها')
        db_table = 'commentdetails'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.cid)


class productdetails(models.Model):
    objects =  'favorite', 'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'
    pid = models.ForeignKey(products, on_delete=models.PROTECT, verbose_name=_('کد محصول'),
                            null=False, blank=False)
    favorite = models.BooleanField(default=0, verbose_name=_('مورد علاقه'))
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('اعتبار محصول')
        verbose_name_plural = _('اعتبار محصول ها')
        db_table = 'productdetails'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.pid)


class sellbascket(models.Model):
    objects = 'pid', 'status','pcount', 'pprise', 'pdiscount', 'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'
    statustypes = [
        (0, 'سفارش'),
        (1, 'پرداخت شده'),
        (2, 'منصرف شده'),
    ]
    pid = models.ForeignKey(products, on_delete=models.PROTECT, max_length=200, verbose_name=_('کد محصول'),
                            null=False, blank=False)
    pcount = models.IntegerField(default=1, verbose_name=_('تعداد کالا'), null=False, blank=False)
    pprise = models.IntegerField(default=0, verbose_name=_('قیمت کالا'), null=False, blank=False)
    pdiscount = models.IntegerField(default=0, verbose_name=_('تخیف کالا'), null=True, blank=True)
    status = models.IntegerField(choices=statustypes, default=0, verbose_name=_(
        'وضعیت خرید'), null=False, blank=False)
    TrackingCode = models.IntegerField(default=0, verbose_name=_('کد رهگیری'), null=True, blank=True)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('سبد خرید')
        verbose_name_plural = _('سبد خرید ها')
        db_table = 'sellbascket'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.pid)


class finalcheckout(models.Model):
    objects = 'totalprise', 'Bankreceipt','TrackingCode', 'Create_Date', \
        'Update_Date', 'Create_Uid', 'Update_Uid'

    totalprise = models.IntegerField(default=0, verbose_name=_('مبلغ پرداخت شده'), null=True, blank=True) 
    Bankreceipt = models.IntegerField(default=0, verbose_name=_('شماره فیش بانکی'), null=True, blank=True) 
    TrackingCode = models.IntegerField(default=0, verbose_name=_('کد رهگیری'), null=True, blank=True)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('بررسی پرداخت')
        verbose_name_plural = _('بررسی های پرداخت ها')
        db_table = 'finalcheckout'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __int__(self):
        return self.totalprise


class firstpagebaners(models.Model):
    objects = 'baner1', 'baner2', 'baner3', 'baner4', 'baner5', 'baner6', 'baner7', 'baner8', 'baner9', 'baner10', 'baner11',\
        'group1', 'group2', 'group3', 'group4', 'group5', 'group6', 'group7', 'group8', 'group9', 'group10', 'group11',\
         'Create_Date', 'Update_Date', 'Create_Uid', 'Update_Uid'

    baner1 = models.ImageField(verbose_name='بنر 1', null=True, blank=True)
    group1 = models.ForeignKey(productsgroups,related_name='group1',verbose_name=_('گروه بنر 1'),on_delete=models.PROTECT, null=True, blank=True)
    baner2 = models.ImageField(verbose_name='بنر 2', null=True, blank=True)
    group2 = models.ForeignKey(productsgroups,related_name='group2',verbose_name=_('گروه بنر 2'),on_delete=models.PROTECT, null=True, blank=True)
    baner3 = models.ImageField(verbose_name='بنر 3', null=True, blank=True)
    group3 = models.ForeignKey(productsgroups,related_name='group3',verbose_name=_('گروه بنر 3'),on_delete=models.PROTECT, null=True, blank=True)
    baner4 = models.ImageField(verbose_name='بنر 4', null=True, blank=True)
    group4 = models.ForeignKey(productsgroups,related_name='group4',verbose_name=_('گروه بنر 4'),on_delete=models.PROTECT, null=True, blank=True)
    baner5 = models.ImageField(verbose_name='بنر 5', null=True, blank=True)
    group5 = models.ForeignKey(productsgroups,related_name='group5',verbose_name=_('گروه بنر 5'),on_delete=models.PROTECT, null=True, blank=True)
    baner6 = models.ImageField(verbose_name='(پایین صفحه)بنر شش', null=True, blank=True)
    group6 = models.ForeignKey(productsgroups,related_name='group6',verbose_name=_('گروه بنر 6'),on_delete=models.PROTECT, null=True, blank=True)
    baner7 = models.ImageField(verbose_name='بنر هفت(پایین صفحه)', null=True, blank=True)
    group7 = models.ForeignKey(productsgroups,related_name='group7',verbose_name=_('گروه بنر 7'),on_delete=models.PROTECT, null=True, blank=True)
    baner8 = models.ImageField(verbose_name='بنر 8', null=True, blank=True)
    group8 = models.ForeignKey(productsgroups,related_name='group8',verbose_name=_('گروه بنر 8'),on_delete=models.PROTECT, null=True, blank=True)
    baner9 = models.ImageField(verbose_name='بنر 9', null=True, blank=True)
    group9 = models.ForeignKey(productsgroups,related_name='group9',verbose_name=_('گروه بنر 9'),on_delete=models.PROTECT, null=True, blank=True)
    baner10 = models.ImageField(verbose_name= 'بنر 10', null=True, blank=True)
    group10 = models.ForeignKey(productsgroups,related_name='group10',verbose_name=_('گروه بنر 10'),on_delete=models.PROTECT, null=True, blank=True)
    baner11 = models.ImageField(verbose_name= 'بنر 11', null=True, blank=True)
    group11 = models.ForeignKey(productsgroups,related_name='group11',verbose_name=_('گروه بنر 11'),on_delete=models.PROTECT, null=True, blank=True)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('بنر')
        verbose_name_plural = _('بنر ها')
        db_table = 'firstpagebaners'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return self.baner1


class firstpagelogo(models.Model):
    objects = 'Logo', 'Create_Date', \
        'Update_Date', 'Create_Uid', 'Update_Uid'

    Logo = models.ImageField(verbose_name='لوگو', null=False, blank=False)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('لوگو')
        verbose_name_plural = _('لوگو ها')
        db_table = 'firstpagelogo'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return self.Logo


class aboutusp1(models.Model):
    objects = 'whoweare', 'personelimg', 'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'

    whoweare = models.CharField(max_length=2000, verbose_name=_('ما که هستیم'), null=True, blank=True)
    teamimg = models.ImageField(verbose_name='عکس گروه', null=False, blank=False)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('درباره ما بخش اول')
        verbose_name_plural = _('درباره ما ها بخش اول')
        db_table = 'aboutusp1'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.whoweare)


class aboutus(models.Model):
    objects ='personelimg', 'pposision', 'ptitle', 'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'

    personelimg = models.ImageField(verbose_name='عکس گروه', null=False, blank=False)
    pposision = models.CharField(max_length=100, verbose_name=_('نام'), null=False, blank=False)
    ptitle = models.CharField(max_length=100, verbose_name=_('سمت'), null=False, blank=False)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('دریاره ما')
        verbose_name_plural = _('درباره ما ها')
        db_table = 'aboutus'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.pposision)


class centercontactus(models.Model):
    objects = 'internetsaletitle','internetsaledesc', 'internetimg', 'callinfo', 'address', 'tell', 'tell2','mobile','fax', 'email', 'wtworkstart', 'wtworkend', 'ltworkstart', 'ltworkend',\
         'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'

    callinfo = models.CharField(max_length=500, verbose_name=_('اطلاعات شرکت'), null=True, blank=True)
    address = models.CharField(max_length=200, verbose_name=_('آدرس شرکت'), null=True, blank=True)
    tell = models.CharField(max_length=200, verbose_name=_('تلفن شرکت'), null=True, blank=True)
    tell2 = models.CharField(max_length=200, verbose_name=_('تلفن دوم شرکت'), null=True, blank=True)
    mobile = models.CharField(max_length=200, verbose_name=_('تلفن همراه'), null=True, blank=True)
    fax = models.CharField(max_length=200, verbose_name=_('فکس'), null=True, blank=True)
    internetsaletitle = models.CharField(max_length=200, verbose_name=_('عنوان خدمات اینترنتی (پایین صفحه)'), null=True, blank=True)
    internetsaledesc = models.TextField(max_length=4000, verbose_name=_('توضیح خدمات اینترنتی (پایین صفحه)'), null=True, blank=True)
    internetimg = models.ImageField(verbose_name='عکس خدمات اینترنتی (پایین صفحه)', null=True, blank=True)
    email = models.EmailField(max_length=2000, verbose_name=_('ایمیل شرکت'), null=True, blank=True)
    wtworkstart = models.CharField(max_length=20, verbose_name=_('ساعت شروع کار در هفته'), null=True, blank=True)
    wtworkend = models.CharField(max_length=20, verbose_name=_('ساعت پایان کار در هفته'), null=True, blank=True)
    ltworkstart = models.CharField(max_length=20, verbose_name=_('ساعت شروع کار در پنج شنبه'), null=True, blank=True)
    ltworkend = models.CharField(max_length=20, verbose_name=_('ساعت پایان کار در پنج شنبه'), null=True, blank=True)  
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('ارتباط با ما')
        verbose_name_plural = _('ارتباط یا ما ها')
        db_table = 'centercontactus'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.callinfo)


class salecontactus(models.Model):
    objects = 'sallinfo', 'centerimg', 'saddress', 'stell', 'stell2','smobile','sfax' 'semail', 'swtworkstart', 'swtworkend', 'sltworkstart', 'sltworkend',\
         'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'
    centerimg = models.ImageField(verbose_name='عکس فروشگاه', null=True, blank=True)
    salecentername = models.CharField(max_length=500, verbose_name=_('نام مرکز'), null=True, blank=True)
    sallinfo = models.CharField(max_length=500, verbose_name=_('اطلاعات تماس'), null=True, blank=True)
    saddress = models.CharField(max_length=200, verbose_name=_('ادرس'), null=True, blank=True)
    stell = models.CharField(max_length=200, verbose_name=_('تلفن دفتر'), null=True, blank=True)
    stell2 = models.CharField(max_length=200, verbose_name=_('تلفن دوم شرکت'), null=True, blank=True)
    smobile = models.CharField(max_length=200, verbose_name=_('تلفن همراه'), null=True, blank=True)
    sfax = models.CharField(max_length=200, verbose_name=_('فکس'), null=True, blank=True)
    semail = models.EmailField(max_length=2000, verbose_name=_('ایمیل'), null=True, blank=True)
    swtworkstart = models.CharField(max_length=20, verbose_name=_('ساعت شروع کار در هفته'), null=True, blank=True)
    swtworkend = models.CharField(max_length=20, verbose_name=_('ساعت پایان کار در هفته'), null=True, blank=True)
    sltworkstart = models.CharField(max_length=20, verbose_name=_('ساعت شروع کار در پنج شنبه'), null=True, blank=True)
    sltworkend = models.CharField(max_length=20, verbose_name=_('ساعت پایان کار در پنج شنبه'), null=True, blank=True)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('ارتباط با ما')
        verbose_name_plural = _('ارتباط یا ما ها')
        db_table = 'salecontactus'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.scallinfo)


class customerquestions(models.Model):
    objects = 'name', 'title', 'tell', 'email', 'desc', 'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'

    name = models.CharField(max_length=500, verbose_name=_('نام'), null=False, blank=False)
    title = models.CharField(max_length=200, verbose_name=_('موضوع'), null=True, blank=True)
    tell = models.CharField(max_length=200,verbose_name=_('تلفن'), null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name=_('ایمیل'), null=True, blank=True)
    desc = models.CharField(max_length=2000, verbose_name=_('شرح سوال'), null=False, blank=False)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('سوال')
        verbose_name_plural = _('سوال ها')
        db_table = 'customerquestions'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.name)


class parametrsersal(models.Model):
    objects = 'ersal', 'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'
    
    ersal = models.CharField(max_length=1000, verbose_name=_('روش ارسال'), null=False, blank=False)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('پارامتر')
        verbose_name_plural = _('پارامتر ها')
        db_table = 'parametrsersal'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.ersal)


class parametrsosool(models.Model):
    objects = 'osool', 'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'
    
    osool = models.CharField(max_length=1000, verbose_name=_('خط مشی'), null=False, blank=False)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('پارامتر')
        verbose_name_plural = _('پارامتر ها')
        db_table = 'parametrsosool'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.osool)


class lastnews(models.Model):
    objects = 'title', 'descriptions', 'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'
    

    title = models.CharField(max_length=200, verbose_name=_('موضوع'), null=False, blank=False)
    khdesc = models.CharField(max_length=200, verbose_name=_('خلاصه شرح'), null=False, blank=False)
    descriptions = models.CharField(max_length=4000, verbose_name=_('شرح خبر'), null=False, blank=False)
    newsimg = models.ImageField(verbose_name='عکس خبر', null=True, blank=True)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('خبر')
        verbose_name_plural = _('خبر ها')
        db_table = 'lastnews'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.title)


class parametsaccounts(models.Model):
    objects = 'account', 'accountimg', 'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'
    
    account = models.CharField(max_length=1000, verbose_name=_('حساب'), null=False, blank=False)
    accountimg = models.ImageField(verbose_name='عکس بانک', null=True, blank=True)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('حساب')
        verbose_name_plural = _('حساب ها')
        db_table = 'parametsaccounts'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.account)


class parametssas(models.Model):
    objects = 'title', 'desc', 'img', 'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'
    
    title =  models.CharField(max_length=200, verbose_name=_('عنوان'), null=False, blank=False)
    desc = models.TextField(max_length=4000, verbose_name=_('شرح'), null=False, blank=False)
    img = models.ImageField(verbose_name='عکس ', null=True, blank=True)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('خدمات پس از فروش')
        verbose_name_plural = _('خدمات های پس از فروش')
        db_table = 'parametssas'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.title)


class parametssupport(models.Model):
    objects = 'title', 'desc', 'img', 'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'
    
    title =  models.CharField(max_length=200, verbose_name=_('عنوان'), null=False, blank=False)
    desc = models.TextField(max_length=4000, verbose_name=_('شرح'), null=False, blank=False)
    img = models.ImageField(verbose_name='عکس ', null=True, blank=True)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('خدمات پس از فروش')
        verbose_name_plural = _('خدمات های پس از فروش')
        db_table = 'parametssupport'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.title)


class weblog(models.Model):
    objects = 'title', 'desc', 'img', 'Update_Date', 'Create_Date', 'Create_Uid', 'Update_Uid'

    title =  models.CharField(max_length=200, verbose_name=_('عنوان'), null=False, blank=False)
    desc = models.TextField(max_length=4000, verbose_name=_('شرح'), null=False, blank=False)
    img = models.ImageField(verbose_name='عکس ', null=True, blank=True)
    Create_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_(
        'کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _('وبلاگ')
        verbose_name_plural = _('وبلاگ ها')
        db_table = 'weblog'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
            ('user_watcher', 'User'),
        )

    def __str__(self):
        return str(self.title)