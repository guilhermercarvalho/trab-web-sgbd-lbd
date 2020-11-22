from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from ..forms import ServiceCreate
from ..models import Service


def create_service(request):
    create = ServiceCreate()
    if request.method == 'POST':
        create = ServiceCreate(request.POST,
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
                      'model': 'Serviço'
                  })


def update_service(request, service_id):
    service_id: int(service_id)
    try:
        service_sel = Service.objects.get(id_ser=service_id)
    except Service.DoesNotExist:
        return redirect('index')

    service_form = ServiceCreate(request.POST or None,
                                   instance=service_sel)

    if service_form.is_valid():
        service_form.save()
        return redirect('index')
    return render(request, 'work/create_form.html',
                  {
                      'create_form': service_form,
                      'model': 'Serviço'
                  })


def delete_service(request, service_id):
    service_id = int(service_id)
    try:
        service_sel = Service.objects.get(id_ser=service_id)
    except Service.DoesNotExist:
        return redirect('index')
    service_sel.delete()
    return redirect('index')
