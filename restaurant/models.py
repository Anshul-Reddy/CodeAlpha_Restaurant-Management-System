from datetime import date
from django.utils.ipv6 import MAX_IPV6_ADDRESS_LENGTH
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number}"

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.customer_name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey(Table,on_delete=models.CASCADE)
    items = models.TextField()
    total_price = models.DecimalField(max_digits=8,decimal_places=2)
    status = models.CharField(max_length=20,default="Pending")

    def __str__(self):
        return self.customer_name

class Inventory(models.Model):
    item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.item.name