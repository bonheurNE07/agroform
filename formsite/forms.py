from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import FormData

class SingUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Second Name'}))

    class Metta:
        model = "User"
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ('names', 'birthdate', 'sex', 'national_id','phone_number', 'province',
                  'district','sector','cellule','species','initial_qts','villages')
        labels = {
            "names":"Amazina / Names",
            "birthdate":"Itariki yavutseho / Date of Birth",
            "sex":"Igitsina / Sex",
            "national_id":"Indagamunu / Nationaal ID No",
            "phone_number" : "Phone Number",
            "province" : "Province",
            "district" : "District",
            "sector" : "Sector",
            "cellule" : "Cellule",
            "species" : "Tree Species",
            "initial_qts" : "Qts",
            "villages" : "Villages"
        }
        widgets = {
        "names": forms.TextInput(attrs={"class": "form-control", "placeholder": "Names"}),
        "birthdate": forms.DateInput(attrs={"class": "form-control", "placeholder": "Date of Birth"}),
        "sex": forms.TextInput(attrs={"class": "form-control", "placeholder": "Sex"}),
        "national_id": forms.TextInput(attrs={"class": "form-control", "placeholder": "National ID"}),
        "phone_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
        "province": forms.TextInput(attrs={"class": "form-control", "placeholder": "Province"}),
        "district": forms.TextInput(attrs={"class": "form-control", "placeholder": "District"}),
        "sector": forms.TextInput(attrs={"class": "form-control", "placeholder": "Sector"}),
        "cellule": forms.TextInput(attrs={"class": "form-control", "placeholder": "Cellule"}),
        "species" : forms.TextInput(attrs={"class": "form-select", "placeholder": "Tree Species"}),
        "initial_qts" : forms.TextInput(attrs={"class": "form-select", "placeholder": "Initial Qts"}),
        "villages" : forms.TextInput(attrs={"class": "form-select", "placeholder": "Villages"})
        }
