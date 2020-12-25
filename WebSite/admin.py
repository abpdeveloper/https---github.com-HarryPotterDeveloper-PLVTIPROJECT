from .models import *
from django.contrib import admin
# from django_jalali.admin.filters import JDateFieldListFilter


# class GroupAdmin(admin.ModelAdmin):
#     list_display = ('Group_Name', 'Group_Modir')
#     list_filter = ('Group_Name', 'Group_Modir', 'Group_Desc')
#     ordering = ['Group_Name', 'Group_Modir']
#     search_fields = ('Group_Name', 'Group_Modir')


# class Group_DetailAdmin(admin.ModelAdmin):
#     list_display = ('group_paren_id', 'dgroup_name', 'dgroup_desc')
#     list_filter = ('group_paren_id', 'dgroup_name', 'dgroup_desc')
#     ordering = ['group_paren_id', 'dgroup_name', 'dgroup_desc']
#     search_fields = ('group_paren_id', 'dgroup_name', 'dgroup_desc')




admin.site.register(productsgroups)
admin.site.register(products)
admin.site.register(slider)
admin.site.register(productsbrands)
admin.site.register(cost)
admin.site.register(comment)
admin.site.register(commentdetails)
admin.site.register(productdetails)
admin.site.register(sellbascket)
admin.site.register(SPFactor)