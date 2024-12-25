# urls.py in store

# urls.py in store

from django.urls import path
from .views import products_page_view, products_view, shop_view
from .views import cart_view, cart_add_view, cart_del_view

app_name = 'store'

urlpatterns = [
    path('product/<int:page>', products_page_view),

    path('product/<slug:page>.html', products_page_view, name="products_page_view"),
    path('product/', products_view),
    path('', shop_view),
    path('cart/', cart_view),
    path('cart/add/<str:id_product>', cart_add_view),
    path('cart/del/<str:id_product>', cart_del_view),
]