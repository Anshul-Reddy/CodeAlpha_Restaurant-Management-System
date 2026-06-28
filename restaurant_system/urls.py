from django.contrib import admin
from django.urls import path
from restaurant.views import home,menu,reserve_table,make_reservation,place_order

urlpatterns = [
    path("",home,name="home"),
    path("menu/",menu,name="menu"),
    path("reserve/",reserve_table,name="reserve"),
    path("reserve/<int:table_id>/",make_reservation,name="make_reservation"),
    path("order/",place_order,name="order"),
    path('admin/', admin.site.urls),
]
