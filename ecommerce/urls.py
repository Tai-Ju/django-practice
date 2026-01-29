from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    # 在这里添加你的 URL 模式
    path("",views.hello),
    path("home/",views.home),
    path("home2/",views.home2),
]
