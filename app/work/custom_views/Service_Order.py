from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import Service_OrderForm
from ..models import Service_Order


@login_required
def service_order_list(request, template_name='work/service_order_list.html'):
    service_order = Service_Order.objects.all()
    data = {}
    data['object_list'] = service_order
    return render(request, template_name, data)


@login_required
def service_order_create(request, template_name='work/service_order_form.html'):
    form_so = Service_OrderForm(request.POST or None)
    if form_so.is_valid():
        form_so.save()
        return redirect('work:service_order_list')
    return render(request, template_name, {'form': [form_so]})


@login_required
def service_order_update(request, num_so, template_name='work/service_order_form.html'):
    if request.user.is_superuser:
        service_order = get_object_or_404(Service_Order, num_so=num_so)
    else:
        return redirect('work:service_order_list')

    form_so = Service_OrderForm(request.POST or None, instance=service_order)

    if form_so.is_valid():
        form_so.save()
        return redirect('work:service_order_list')
    return render(request, template_name, {'form': [form_so]})


@login_required
def service_order_delete(request, num_so, template_name='work/service_order_list.html'):
    service_order = get_object_or_404(Service_Order, num_so=num_so)
    if request.method == 'POST':
        service_order.delete()
        return redirect('work:service_order_list')
    return render(request, template_name, {'object': service_order})
