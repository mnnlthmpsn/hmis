from django import forms
from staffAuth.models import Role
from .models import Drug

class StaffForm(forms.Form):
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Staff Email'}))
    def_password = forms.CharField(label='Default Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter default password for staff'}), min_length=8)
    firstname = forms.CharField(label='Firstname', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Staff Firstname'}))
    lastname = forms.CharField(label='Lastname', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Staff Lastname'}))
    telephone = forms.CharField(label='Telephone Number', max_length=13, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Staff Phone Number'}))
    date_of_birth = forms.DateField(label='Date of Birth', required=True, widget=forms.SelectDateWidget(years=range(1900, 2100)))
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}))


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ('name', 'description', 'price', 'qty_in_stock')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Drug Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Drug Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': 0.10}),
            'qty_in_stock': forms.NumberInput(attrs={'class': 'form-control', 'min': 1})
        }