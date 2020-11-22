from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import Client_ServiceForm
from ..models import Client_Service


@login_required
def client_service_list(request, template_name='work/client_service_list.html'):
    client_service = Client_Service.objects.all()
    data = {}
    data['object_list'] = client_service
    return render(request, template_name, data)


@login_required
def client_service_create(request, template_name='work/client_service_form.html'):
    form_cli_ser = Client_ServiceForm(request.POST or None)
    if form_cli_ser.is_valid():
        form_cli_ser.save()
        return redirect('work:client_service_list')
    return render(request, template_name, {'form': [form_cli_ser]})


@login_required
def client_service_update(request, matr, template_name='work/client_service_form.html'):
    if request.user.is_superuser:
        client_service = get_object_or_404(Client_Service, matr=matr)
    else:
        return redirect('work:client_service_list')

    form_cli_ser = Client_ServiceForm(request.POST or None, instance=client_service)

    if form_cli_ser.is_valid():
        form_cli_ser.save()
        return redirect('work:client_service_list')
    return render(request, template_name, {'form': [form_cli_ser]})


@login_required
def client_service_delete(request, matr, template_name='work/client_service_confirm_delete.html'):
    if request.user.is_superuser:
        client_service = get_object_or_404(Client_Service, matr=matr)
    else:
        return redirect('work:client_service_list')
    if request.method == 'POST':
        Client_Service.delete()
        return redirect('work:client_service_list')
    return render(request, template_name, {'object': client_service})
