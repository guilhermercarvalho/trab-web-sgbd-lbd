from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from ..forms import ItemCreate
from ..models import Item


def create_item(request):
    create = ItemCreate()
    if request.method == 'POST':
        create = ItemCreate(request.POST,
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
                      'model': 'Item'
                  })


def update_item(request, item_id):
    item_id: int(item_id)
    try:
        item_sel = Item.objects.get(id_item=item_id)
    except Item.DoesNotExist:
        return redirect('index')

    item_form = ItemCreate(request.POST or None,
                                   instance=item_sel)

    if item_form.is_valid():
        item_form.save()
        return redirect('index')
    return render(request, 'work/create_form.html',
                  {
                      'create_form': item_form,
                      'model': 'Item'
                  })


def delete_item(request, item_id):
    item_id = int(item_id)
    try:
        item_sel = Item.objects.get(id_item=item_id)
    except Item.DoesNotExist:
        return redirect('index')
    item_sel.delete()
    return redirect('index')
