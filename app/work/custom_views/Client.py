from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from ..forms import ClientCreate
from ..models import Client


def create_client(request):
    create = ClientCreate()
    if request.method == 'POST':
        create = ClientCreate(request.POST,
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
                      'model': 'Cliente'
                  })


def update_client(request, client_id):
    client_id: int(client_id)
    try:
        client_sel = Client.objects.get(id_cli=client_id)
    except Client.DoesNotExist:
        return redirect('index')

    client_form = ClientCreate(request.POST or None,
                                   instance=client_sel)

    if client_form.is_valid():
        client_form.save()
        return redirect('index')
    return render(request, 'work/create_form.html',
                  {
                      'create_form': client_form,
                      'model': 'Cliente'
                  })


def delete_client(request, client_id):
    client_id = int(client_id)
    try:
        client_sel = Client.objects.get(id_cli=client_id)
    except Client.DoesNotExist:
        return redirect('index')
    client_sel.delete()
    return redirect('index')
