from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index.as_view()),
    path("product-details/<int:product_id>", views.Products.as_view(), name='products'),
    path("shop/<slug:slug>", views.Shop.as_view(), name='shop'),
    path("aromaty_home_shop/<slug:slug>", views.ShopSlave.as_view(), name='shop_slave'),
    path("contacts", views.contact),
]
