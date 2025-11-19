from django import forms

from .models import Profile

class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required':'required'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required':'required'}))


class SignUpForm(forms.ModelForm):

    class Meta :

        model = Profile

        fields = ['first_name','last_name','email']

        widgets = {

            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
        }