from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'age', 'birthday', 'email', 'phone_number', 'is_cell', 'comments',)