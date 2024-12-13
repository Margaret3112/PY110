# urls.py in store

# urls.py in store

from django.urls import path
from .views import products_page_view, products_view, shop_view

urlpatterns = [
    path('product/<int:page>', products_page_view),

    path('product/<slug:page>.html', products_page_view),
    path('product/', products_view),
    path('', shop_view),
]