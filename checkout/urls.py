from django.urls import path
from . import views
urlpatterns = [
    path('checkout_page',views.checkout_page, name='checkout_page'),
    path('update_quantity',views.update_quantity,name='update_quantity'),
    path('remove_item/<int:cart_item_id>',views.remove_item,name='remove_item'),
    path('order_placement',views.final_order,name='order_placement'),
    path('update_create_order',views.update_create_order, name='update_create_order'),
    path('thank_you_page/', views.thank_you_page, name='thank_you_page'),
]