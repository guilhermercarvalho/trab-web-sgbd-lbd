from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from ..forms import AddressForm
from ..models import Address

@login_required
def create_address(request):
    form_addr = AddressForm(request.POST or None)
    if form_addr.is_valid():
        address = form_addr.save()
        return address.id_addr

def update_address(request, address_id):
    address_id: int(address_id)
    try:
        address_sel = Address.objects.get(id_addr=address_id)
    except Address.DoesNotExist:
        return redirect('index')

    address_form = AddressForm(request.POST or None,
                                 instance=address_sel)

    if address_form.is_valid():
        address_form.save()
        return redirect('index')
    return render(request, 'work/create_form.html',
                  {'create_form': address_form})


def delete_address(request, address_id):
    address_id = int(address_id)
    try:
        address_sel = Address.objects.get(id_addr=address_id)
    except Address.DoesNotExist:
        return redirect('index')
    address_sel.delete()
    return redirect('index')
