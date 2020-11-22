from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from ..forms import AddressCreate
from ..models import Address


def create_address(request):
    create = AddressCreate()
    if request.method == 'POST':
        create = AddressCreate(request.POST,
                               request.FILES)

        if create.is_valid():
            create.save()
            return redirect('index')
        else:
            return HttpResponse("""seu formulário está errado, tente novamente em \<a href = "{{url: 'index'}}">recarregar</a>""")

    return render(request,
                  'work/create_form.html',
                  {
                      'create_form': create,
                      'model': 'Endereço',
                  })


def update_address(request, address_id):
    address_id: int(address_id)
    try:
        address_sel = Address.objects.get(id_addr=address_id)
    except Address.DoesNotExist:
        return redirect('index')

    address_form = AddressCreate(request.POST or None,
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
