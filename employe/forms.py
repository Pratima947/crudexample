from django import forms  
from employe.models import Employe 
class EmployeForm(forms.ModelForm):  
    class Meta:  
        model = Employe  
        fields = "__all__"  
def handle_uploaded_file(f): 
    with open('myapp/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)          