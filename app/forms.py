from django.forms import ModelForm

from app.models import Employee
class MyForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name' , 'email' , 'address' , 'phone']
        
        
    def __init__(self, *args, **kwargs):
        super(MyForm,self).__init__(*args, **kwargs)
        
