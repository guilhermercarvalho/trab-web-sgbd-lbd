from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import EmployeeForm
from ..models import Employee


@login_required
def employee_list(request, template_name='work/employee_list.html'):
    employee = Employee.objects.all()
    data = {}
    data['object_list'] = employee
    return render(request, template_name, data)



@login_required
def employee_create(request, template_name='work/employee_form.html'):
    form_ee = EmployeeForm(request.POST or None)
    if form_ee.is_valid():
        employee = form_ee.save(commit=False)
        employee.user = request.user
        employee.save()
        return redirect('work:employee_list')
    return render(request, template_name, {'form': [form_ee]})

@login_required
def employee_update(request, matr, template_name='work/employee_form.html'):
    if request.user.is_superuser:
        employee = get_object_or_404(Employee, matr=matr)
    else:
        employee = get_object_or_404(Employee, matr=matr, user=request.user)
    
    form_ee = EmployeeForm(request.POST or None, instance=employee)
    
    if form_ee.is_valid():
        form_ee.save()
        return redirect('work:employee_list')
    return render(request, template_name, {'form': [form_ee]})

@login_required
def employee_delete(request, matr, template_name='work/employee_confirm_delete.html'):
    if request.user.is_superuser:
        employee = get_object_or_404(Employee, matr=matr)
    else:
        employee = get_object_or_404(Employee, matr=matr, user=request.user)
    if request.method=='POST':
        employee.delete()
        return redirect('work:employee_list')
    return render(request, template_name, {'object':employee})
