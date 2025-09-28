from django.urls import path
from . views import *

urlpatterns = [
    path("",adminhome, name='admins'),
    path("productlist/",productlist, name='productlist'),
    path('addproduct/',addproduct,name='addproduct'),
    path('updateproduct/<int:product_id>',updateproduct, name='updateproduct'),
    path('deleteproduct/<int:product_id>', deleteproduct,name='deleteproduct'),
    path('categorylist/',categorylist,name='categorylist'),
    path('addcategory/',addcategory, name='addcategory'),
    path('updatecategory/<int:category_id>', updatecategory,name='updatecategory'),
    path('deletecategory/<int:category_id>', deletecategory,name='deletecategory'),   
]