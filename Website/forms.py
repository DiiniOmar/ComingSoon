from Website.models import SignUp
from django import forms

class signUpForm(forms.ModelForm):
    
    class Meta:
        model = SignUp
        fields = ['name', 'email','phone']
