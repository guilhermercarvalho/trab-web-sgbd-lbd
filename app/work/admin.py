from django.contrib import admin

from .models import Employee, Client, Service, Item, Service_Order, Client_Service, Service_Item

# Register your models here.

# admin.site.register(User, UserAdmin)

admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Item)
admin.site.register(Service_Order)
admin.site.register(Client_Service)
admin.site.register(Service_Item)