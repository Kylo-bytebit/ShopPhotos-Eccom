from django import forms
from .models import Image
from .models import Payment
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'price', 'image']

        #widget ={
           # 'title': forms.TextInput(attrs={'class':'form-control' }),
            #'description': forms.Textarea(attrs={'class':'form-control'}),
            #'price': forms.FloatField(attrs={'class':'form-control'}),
          #  'image': forms.FileField(attrs={'class':'form-control'}),
           # }
            


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields =['card_number', 'expiry', 'cvc' ]