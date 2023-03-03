from django import  forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form_control'}))
    phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form_control'}))
    