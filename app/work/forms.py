from django import forms
from .models import Address, Client, Employee, Item, Service, Service_Order

class EmployeeCreate(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' 

class AddressCreate(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class ClientCreate(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ServiceCreate(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class ItemCreate(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class Service_OrderCreate(forms.ModelForm):
    class Meta:
        model = Service_Order
        fields = '__all__'