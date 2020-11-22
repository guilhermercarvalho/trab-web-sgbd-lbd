from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import Service_ItemForm
from ..models import Service_Item


@login_required
def service_item_list(request, template_name='work/service_item_list.html'):
    service_item = Service_Item.objects.all()
    data = {}
    data['object_list'] = service_item
    return render(request, template_name, data)


@login_required
def service_item_create(request, template_name='work/service_item_form.html'):
    form_item = Service_ItemForm(request.POST or None)
    if form_item.is_valid():
        form_item.save()
        return redirect('work:service_item_list')
    return render(request, template_name, {'form': [form_item]})


@login_required
def service_item_update(request, matr, template_name='work/service_item_form.html'):
    if request.user.is_superuser:
        service_item = get_object_or_404(Service_Item, matr=matr)
    else:
        return redirect('work:service_item_list')

    form_item = Service_ItemForm(request.POST or None, instance=service_item)

    if form_item.is_valid():
        form_item.save()
        return redirect('work:service_item_list')
    return render(request, template_name, {'form': [form_item]})


@login_required
def service_item_delete(request, matr, template_name='work/service_item_confirm_delete.html'):
    if request.user.is_superuser:
        service_item = get_object_or_404(Service_Item, matr=matr)
    else:
        return redirect('work:service_item_list')
    if request.method == 'POST':
        Service_Item.delete()
        return redirect('work:service_item_list')
    return render(request, template_name, {'object': service_item})
