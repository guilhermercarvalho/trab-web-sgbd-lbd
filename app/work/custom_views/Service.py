from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import ServiceForm
from ..models import Service


@login_required
def service_list(request, template_name='work/service_list.html'):
    service = Service.objects.all()
    data = {}
    data['object_list'] = service
    return render(request, template_name, data)


@login_required
def service_create(request, template_name='work/service_form.html'):
    form_cli = ServiceForm(request.POST or None)
    if form_cli.is_valid():
        service = form_cli.save(commit=False)
        service.save()
        return redirect('work:service_list')
    return render(request, template_name, {'form': [form_cli]})


@login_required
def service_update(request, id_ser, template_name='work/service_form.html'):
    if request.user.is_superuser:
        service = get_object_or_404(Service, id_ser=id_ser)
    else:
        return redirect('work:service_list')

    form_cli = ServiceForm(request.POST or None, instance=service)

    if form_cli.is_valid():
        form_cli.save()
        return redirect('work:service_list')
    return render(request, template_name, {'form': [form_cli]})


@login_required
def service_delete(request, id_ser, template_name='work/service_list.html'):
    service = get_object_or_404(Service, id_ser=id_ser)
    if request.method == 'POST':
        service.delete()
        return redirect('work:service_list')
    return render(request, template_name, {'object': service})
