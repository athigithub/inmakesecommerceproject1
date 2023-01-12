from django.urls import path

from . import views
app_name='ecommerceapp'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.product_details,name='prodCatdetail'),
]