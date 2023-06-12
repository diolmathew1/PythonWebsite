

from django.urls import path

from shopapp import views
app_name='shopapp'
urlpatterns = [
    path('',views.allProductCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProductCat,name='products_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='productDetail')
]