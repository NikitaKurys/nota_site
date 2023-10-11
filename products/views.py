from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ProductCards, SlaveCategory, MainCategory


class Index(ListView):
    model = MainCategory
    template_name = 'store/index.html'
    context_object_name = "maincategory"


class Products(DetailView):
    model = ProductCards
    pk_url_kwarg = "product_id"
    template_name = 'store/product-details.html'
    context_object_name = 'products'


class Shop(DetailView):
    model = MainCategory
    slug_url_kwarg = "slug"
    template_name = 'store/shop.html'
    context_object_name = "category"


class ShopSlave(DetailView):
    model = SlaveCategory
    slug_url_kwarg = "slug"
    template_name = 'store/shop.html'
    context_object_name = "slave_category"


def contact(request):
    return render(request, 'store/contact.html')
