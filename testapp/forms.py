from django import forms
from testapp.models import Employee 
class EmployeeForm(forms.ModelForm):
    name = forms.CharField()
    age = forms.IntegerField()
    sal = forms.FloatField()
    address = forms.CharField()
    class Meta:
        model = Employee
        fields = '__all__'