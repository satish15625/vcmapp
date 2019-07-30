from django.forms import ModelForm
from home.models import ConsultingCustomer

class ConsultingForm(ModelForm):
    
    class Meta:
        model = ConsultingCustomer

        fields = ['name','email','number']
    
    # this function will be used for the validation 
    def clean(self): 
  
        # data from the form is fetched using super function 
        super(ConsultingForm, self).clean() 
     
        return self.cleaned_data 
