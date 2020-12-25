import re
from django.db import connection
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
# from WebSite.models import TranslateModel
from django.utils import translation

register = template.Library()

@register.filter
def intdot(value):
    orig = force_text(value)
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', orig)
    if orig == new:
        return new
    else:
        return intdot(new)


@register.filter
def StatusName(value):
    if value == 0 :
        return 'پیش نویس'
    elif value == 1 :
        return 'ارسال شده'
    elif value == 2 :
        return 'تایید شده'
    elif value == 3 :
        return 'تایید نشده'
    return value


@register.filter
def ShamsiToMiladi(Date, request):
    if request.user.language == True :
        date2=str(Date).replace("-", "/")
        with connection.cursor() as cursor:
            Date=cursor.execute("select cast(dbo.ShamsitoMiladi('{date2}') as nvarchar) as a".format(date2=date2)).fetchall()
            cursor.commit()
            for d in Date:
                t=d.a
            return t
    else:
        return Date


@register.filter
def MiladiToShamsi(Date, request):
        # date2=str(Date).replace("-", "/")
        with connection.cursor() as cursor:
            Date=cursor.execute("select cast(dbo.__MiladiToShamsi__('{date2}') as nvarchar) as a".format(date2=Date)).fetchall()
            cursor.commit()
            for d in Date:
                t=d.a
            return t