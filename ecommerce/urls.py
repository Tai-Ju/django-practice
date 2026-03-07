from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path("", views.hello, name="hello"),
    path("home/", views.home, name="home"),
    path("home2/", views.home2, name="home2"),
    path("member/", views.member, name="member"),
    path("product/", views.product, name="product"),
]
