from django.shortcuts import get_object_or_404
from restaurant.models import MenuItem,Table,Order,Reservation,Inventory
from django.shortcuts import render,redirect
from .forms import ReservationForm

def home(request):
    return render(request,"restaurant/home.html")

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request,"restaurant/menu.html",{"menu_items":menu_items})

def reserve_table(request):
    tables = Table.objects.filter(is_available=True)
    return render(request,"restaurant/reserve.html",{"tables":tables})

def make_reservation(request,table_id):
    table = get_object_or_404(Table,id=table_id)
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.table = table
            reservation.save()
            table.is_available = False
            table.save()
            return redirect("reserve")
    form = ReservationForm()

    return render(request,"restaurant/reservation_form.html",{"table":table,"form":form})

def place_order(request):
    tables = Table.objects.filter(is_available=False)
    menu_items = MenuItem.objects.filter(available=True)
    if request.method == "POST":
        table = Table.objects.get(id=request.POST["table"])
        items = request.POST.getlist("items")
        total = 0

        for item_name in items:
            item = MenuItem.objects.get(name=item_name)
            total += item.price

            inventory = Inventory.objects.get(item=item)

            if inventory.quantity>0:
                inventory.quantity -= 1
                inventory.save()
        
        Order.objects.create(
            customer_name=request.POST["customer_name"],
            table = table,
            items=", ".join(items),
            total_price = total,
            status = "Pending"
        )
        return redirect("home")

    return render(request,"restaurant/order.html",{"tables":tables,"menu_items":menu_items})