from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import ItemForm, Service_ItemForm
from ..models import Item, Service_Item


@login_required
def item_list(request, template_name='work/item_list.html'):
    item = Item.objects.all()
    data = {}
    data['object_list'] = item
    return render(request, template_name, data)


@login_required
def item_create(request, template_name='work/item_form.html'):
    form_item = ItemForm(request.POST or None)
    if form_item.is_valid():
        form_item.save()
        return redirect('work:item_list')
    return render(request, template_name, {'form': [form_item]})


@login_required
def item_update(request, id_item, template_name='work/item_form.html'):
    if request.user.is_superuser:
        item = get_object_or_404(Item, id_item=id_item)
    else:
        return redirect('work:item_list')

    form_item = ItemForm(request.POST or None, instance=item)

    if form_item.is_valid():
        form_item.save()
        return redirect('work:item_list')
    return render(request, template_name, {'form': [form_item]})


@login_required
def item_delete(request, id_item, template_name='work/item_list.html'):
    item = get_object_or_404(Item, id_item=id_item)
    if request.method == 'POST':
        item.delete()
        return redirect('work:item_list')
    return render(request, template_name, {'object': item})
