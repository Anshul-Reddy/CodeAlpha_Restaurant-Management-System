from django.contrib import admin
from .models import MenuItem,Table,Reservation,Order,Inventory

admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(Inventory)