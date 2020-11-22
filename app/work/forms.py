from django.db.models import fields
from django.forms import ModelForm
from .models import Client, Client_Service, Employee, Item, Service, Service_Order, Service_Item

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' 
        exclude = ('user',)

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('user', 'qty_ser',)

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class Service_OrderForm(ModelForm):
    class Meta:
        model = Service_Order
        fields = '__all__'

class Service_ItemForm(ModelForm):
    class Meta:
        model = Service_Item
        fields = '__all__'

class Client_ServiceForm(ModelForm):
    class Meta:
        model = Client_Service
        fields = '__all__'