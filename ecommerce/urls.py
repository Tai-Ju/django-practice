from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path("home/", views.home, name="home"),
    path("home2/", views.home2, name="home2"),
    path("product/", views.product, name="product"),
    path("product/<int:product_id>/delete/", views.delete_product, name="delete_product"),
    path("product/<int:product_id>/edit/", views.edit_product, name="edit_product"),
    path("product/<int:product_id>/update/", views.update_product, name="update_product"),
]
