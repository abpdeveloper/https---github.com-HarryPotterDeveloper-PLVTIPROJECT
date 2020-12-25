from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView
from django.urls import path, include, re_path

app_name = 'WebSite'
urlpatterns = [
    path('', views.loginuser , name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('mobillogin/', views.loginusermobile , name='loginusermobile'),
    path('mobillogin/register/', views.registermobile , name='registermobile'),

    path('quickView/', TemplateView.as_view(template_name="popup/quickView.html.html"), name='quickView'),
    path('dashboard/Pay/report/PayRcvDetaileJson/', views.PayRcvDetaileReportJson.as_view(), name='PayRcvDetaileReportJson'),

    # Creat For All
    path('Create/<str:ModelName>/<str:form_name>/<str:redirect_path>/<str:html_name>/<str:context_name>/', views.create , name='create'),
    # Update For All
    path('Update/<str:ModelName>/<str:form_name>/<str:redirect_path>/<str:html_name>/<str:context_name>/<int:id>/', views.update , name='update'),
    # Delete For All
    path('delete/<str:ModelName>/<str:redirect_path>/<int:id>/', views.delete , name='delete'),
    path('DeleteRecords/<list_ids>/<ModelName>/<RedirectPath>/', views.DeleteRecords, name='DeleteRecords'),
 
    # Creat For Users
    path('dashboard/create/user/', views.create_user , name='create_user'),
    # Update For Users
    path('dashboard/update/user/<int:id>/', views.update_user , name='update_user'),
    # Delete For Users
    path('dashboard/delete/user/<int:id>/', views.Delete_User , name='Delete_User'),

    #comments
    path('commentAccept/', views.commentAccept.as_view() , name='commentAccept'),
    path('commentReject/', views.commentReject.as_view() , name='commentReject'),
    path('commentDelete/', views.commentDelete.as_view() , name='commentDelete'),

    # customers_questions_create 
    path('dashboard/create/customersquestions_create/', views.customersquestions_create , name='customersquestions_create'),

    # Change Passwords
    path('dashboard/Admin/ChangePassword/<int:id>/', views.ChangePassword_AdminView, name='ChangePassword_AdminView'),
    path('dashboard/User/ChangePassword/', views.ChangePassword_UserView, name='ChangePassword_UserView'),

    # ReportskhabarLV
    
    path('dashboard/Admin/khabar/', views.khabarLV.as_view(), name='khabar'),
    path('dashboard/Admin/orderlist/', views.salebacketcheckout.as_view(), name='orderlist'),
    path('dashboard/product/report/', views.productss.as_view(), name='product'),
    path('dashboard/productsgroups/report/', views.productsgroupsreport.as_view(), name='productsgroupsLV'),
    path('dashboard/customer/report/', views.customerreport.as_view(), name='customerLV'),
    path('dashboard/customer/report/customerSync/', views.customerSync, name='customerSync'),
    path('dashboard/customer/report/UserSync/', views.UserSync, name='UserSync'),
    path('dashboard/customer/report/customerreportJson/', views.customerreportJson.as_view(), name='customerreportJson'),

    path('dashboard/Pay/report/', views.PayRcvreport.as_view(), name='PayRcvreport'),
    path('dashboard/Pay/report/PaySync/', views.PayRcvSync, name='PayRcvSync'),
    path('dashboard/Pay/report/PayreportJson/', views.PayRcvReportJson.as_view(), name='PayRcvReportJson'),

    path('dashboard/Factors/report/', views.Factorsreport.as_view(), name='factorreport'),
    path('dashboard/Factors/report/FactorSync/', views.FactorSync, name='FactorSync'),
    path('dashboard/Factors/report/FactorsreportJson/', views.FactorsreportJson.as_view(), name='factorreportJson'),
    path('dashboard/brand/report/', views.brandreport.as_view(), name='brandreport'),
    path('dashboard/cost/report/', views.costreport.as_view(), name='costreport'),
    path('dashboard/comment/report/', views.commentreport.as_view(), name='commentreport'),
    #path('dashboard/comment/report/commentreportJson/', views.commentreportJson.as_view(), name='commentreportJson'),
    path('dashboard/users/report/', views.usersreport.as_view(), name='usersreport'),
    path('dashboard/slider/report/', views.sliderreport.as_view(), name='slidersreport'),
    path('dashboard/insideslider/report/', views.insidesliderreport.as_view(), name='insideslidersreport'),
    path('products/', views.allproducts.as_view() , name='products'),
    path('ProductReportJson/', views.ProductReportJson.as_view(), name='ProductReportJson'),
    path('dashboard/logo/report/', views.logoreportview.as_view() , name='logoreport'),
    path('dashboard/ersal/report/', views.ersalreport.as_view() , name='ersalreport'),
    path('dashboard/osool/report/', views.osoolreport.as_view() , name='osoolreport'),
    path('ersal/report/', views.ersalreportusers.as_view() , name='ersalreportusers'),
    path('osool/report/', views.osoolreportusers.as_view() , name='osoolreportusers'),
    path('dashboard/banners/report/', views.bannersreportview.as_view() , name='bannersreportview'),
    path('dashboard/about/report/', views.aboutreportview.as_view() , name='aboutreport'),
    path('dashboard/aboutteam/report/', views.aboutteamreportview.as_view() , name='aboutteamreport'),
    path('dashboard/ccontactus/report/', views.ccontactusreportview.as_view() , name='ccontactusreport'),
    path('dashboard/scontactus/report/', views.scontactusreportview.as_view() , name='scontactusreport'),
    path('dashboard/bankaccount/report/', views.bankaccount.as_view() , name='bankreport'),
    path('dashboard/sasreport/report/', views.sasreportadmin.as_view() , name='sasreport'),
    path('dashboard/weblog/report/', views.weblogadmin.as_view() , name='weblogreport'),
    path('dashboard/supportreport/report/', views.supportreportadmin.as_view() , name='supportreport'),
    path('dashboard/customerquestions/report/', views.customerquestionsview.as_view() , name='customerquestionsreport'),
    path('contact/', views.customersquestions_create , name='contact'),
    path('stors/', views.stors.as_view() , name='stors'),
    path('about/', views.useraboutreportview.as_view(), name='about'),
    # path('category/', views.showshrouplist.as_view(), name='category-boxed'),
    path('category/productlist/<int:id>/', views.showproductlist.as_view(), name='productlist'),
    path('category/productlist/showproduct/<int:id>/', views.showproduct.as_view(), name='showproduct'),
    path('cart/', views.salebacket.as_view(), name='salebacket'),
    path('wishlist/', views.wishlist.as_view(), name='wishlist'),
    path('products/search_result/', views.search_box.as_view(), name='search_box'),
    path('weblog/', views.weblogusers.as_view() , name='weblog'),
    path('Bascket/', views.AddBascket.as_view() , name='AddBascket'),
    path('Bascketdelete/', views.Bascketdelete.as_view(), name='Bascketdelete'),
    path('Favorite/', views.AddFavorite.as_view() , name='AddFavorite'),
    path('Favoritedelete/', views.Favoritedelete.as_view(), name='Favoritedelete'),
    path('removepic/', views.removepic.as_view(), name='removepic'),
    path('removepicBanner/', views.removepicBanner.as_view(), name='removepicBanner'),
    path('AddComment/', views.AddComment.as_view(), name='AddComment'),
    path('updatecount/', views.UpdateCount.as_view(), name='UpdateCount'),
    path('dashboard/', views.usersfactors.as_view(), name='dashboard'),
    path('UserFactorsArticles/', views.usersarticle.as_view(), name='usersarticle'),
    path('UserPayRcvArticles/', views.userspayarticle.as_view(), name='userspayarticle'),
    path('factordetaile/<int:id>/', views.factordetail, name='factordetaile'),
    path('PayRcvDetaile/<int:id>/', views.PayRcvDetail, name='PayRcvDetail'),
    path('userchangeinfo/', views.userschangeinfo, name='userchangeinfo'),
    path('lastnewspage/', views.lastnewspage.as_view(), name='lastnewspage'),
    path('lastnewspage/<int:id>/', views.lastnewspageone.as_view(), name='lastnewspageone'),
    path('category/<int:id>/', views.treeshowgroup.as_view(), name='treeshowgroup'),
    path('category/create/<int:id>/', views.treeshowgroupcreate, name='treeshowgroupcreate'),
    path('dashboard/factordetaile/', views.sparticle.as_view(), name='factordetaile'),
    path('dashboard/PayDetaile/', views.AdminCheck.as_view(), name='AdminCheck'),
    path('dashboard/PayRcvDetaile/', views.userAdminCheck.as_view(), name='userAdminCheck'),
    path('bankreport/', views.bankreport.as_view(), name='footerbankreport'),
    path('sasreport/', views.sasreportfooter.as_view(), name='footersasreport'),
    path('supportreport/', views.supportreportfooter.as_view(), name='footersupportreport'),
    path('dashboard/Factors/report/َArticlereportJson/', views.ArticlereportJson.as_view(), name='ArticlereportJson'),    
    path('advancedsearchProducts/<int:id>/', views.advancedsearchProducts.as_view() , name='advancedsearchProducts'),
    path('advancedsearchProductsJson/', views.advancedsearchProductsJson.as_view() , name='advancedsearchProductsJson'),
    
    path('ProductCategoryJson/', views.ProductCategoryJson.as_view() , name='ProductCategoryJson'),
    path('resetpass/', views.resetpass.as_view() , name='resetpass'),
    
    path('productscategoryparent/<int:id>/', views.productscategoryparent, name='productscategoryparent'),
    path('productscategory/', views.productscategoryview.as_view() , name='productscategoryLV'),
    
    path('searchcustomerJson/', views.searchcustomerJson.as_view() , name='searchcustomerJson'),

    path('request/', views.send_request, name='request'),
    path('verify/', views.verify , name='verify'),

]

