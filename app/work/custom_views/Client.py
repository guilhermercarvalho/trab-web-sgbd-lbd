from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import ClientForm
from ..models import Client


@login_required
def client_list(request, template_name='work/client_list.html'):
    client = Client.objects.all()
    data = {}
    data['object_list'] = client
    return render(request, template_name, data)


@login_required
def client_create(request, template_name='work/client_form.html'):
    form_cli = ClientForm(request.POST or None)
    if form_cli.is_valid():
        client = form_cli.save(commit=False)
        client.user = request.user
        client.save()
        return redirect('work:client_list')
    return render(request, template_name, {'form': [form_cli]})


@login_required
def client_update(request, id_cli, template_name='work/client_form.html'):
    if request.user.is_superuser:
        client = get_object_or_404(Client, id_cli=id_cli)
    else:
        return redirect('work:client_list')

    form_cli = ClientForm(request.POST or None, instance=client)

    if form_cli.is_valid():
        form_cli.save()
        return redirect('work:client_list')
    return render(request, template_name, {'form': [form_cli]})


@login_required
def client_delete(request, id_cli, template_name='work/client_list.html'):
    client = get_object_or_404(Client, id_cli=id_cli)
    if request.method=='POST':
        client.delete()
        return redirect('work:client_list')
    return render(request, template_name, {'object':client})
