from django.shortcuts import render

# Create your views here.
def Employee_View(request):
    return render(request,'testapp/base.html')

from testapp.models import Employee
def Employee_Data(request):
    emp_data = Employee.objects.all()
    return render(request,'testapp/fulldata.html',{'emp_data':emp_data})

from testapp.forms import EmployeeForm
def Add_View(request):
    form = EmployeeForm()
    if request.method =='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return  Employee_View(request) 
    form = EmployeeForm()  
    return render(request,'testapp/form.html',{'form':form})
