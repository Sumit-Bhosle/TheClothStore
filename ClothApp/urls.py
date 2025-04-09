from django.urls import path    # imports URL from PROJECT'S URL.py to APP's URL.py
from . import views

urlpatterns=[
    path('',views.home_page,name='home'),
    path('product-detail/<int:id>/',views.product_detail,name='product-detail'),
    path('category/<int:id>/',views.category_data,name='category_data'),
    path('search/',views.search_product,name='search'),
    path('setup/', views.setup),# url to TEMPERORY LOGIC FOR MIGRATIONS
]
