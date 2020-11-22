from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from ..forms import Service_OrderCreate
from ..models import Service_Order


def create_service_order(request):
    create = Service_OrderCreate()
    if request.method == 'POST':
        create = Service_OrderCreate(request.POST,
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
                      'model': 'Ordem de Serviço'
                  })


def update_service_order(request, service_order_id):
    service_order_id: int(service_order_id)
    try:
        service_order_sel = Service_Order.objects.get(num_os=service_order_id)
    except Service_Order.DoesNotExist:
        return redirect('index')

    service_order_form = Service_OrderCreate(request.POST or None,
                                   instance=service_order_sel)

    if service_order_form.is_valid():
        service_order_form.save()
        return redirect('index')
    return render(request, 'work/create_form.html',
                  {
                      'create_form': service_order_form,
                      'model': 'Ordem de Serviço'
                  })


def delete_service_order(request, service_order_id):
    service_order_id = int(service_order_id)
    try:
        service_order_sel = Service_Order.objects.get(num_os=service_order_id)
    except Service_Order.DoesNotExist:
        return redirect('index')
    service_order_sel.delete()
    return redirect('index')
