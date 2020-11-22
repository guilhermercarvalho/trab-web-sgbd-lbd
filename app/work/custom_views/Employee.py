from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from ..forms import EmployeeCreate
from ..models import Employee


def create_employee(request):
    create = EmployeeCreate()
    if request.method == 'POST':
        create = EmployeeCreate(request.POST,
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
                      'model': 'Funcionário'
                  })


def update_employee(request, employee_id):
    employee_id: int(employee_id)
    try:
        employee_sel = Employee.objects.get(matr=employee_id)
    except Employee.DoesNotExist:
        return redirect('index')

    employee_form = EmployeeCreate(request.POST or None,
                                   instance=employee_sel)

    if employee_form.is_valid():
        employee_form.save()
        return redirect('index')
    return render(request, 'work/create_form.html',
                  {
                      'create_form': employee_form,
                      'model': 'Funcionário'
                  })


def delete_employee(request, employee_id):
    employee_id = int(employee_id)
    try:
        employee_sel = Employee.objects.get(matr=employee_id)
    except Employee.DoesNotExist:
        return redirect('index')
    employee_sel.delete()
    return redirect('index')
