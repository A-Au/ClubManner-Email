from django.db import models
from django.forms import ModelForm
from django import forms
from django.core.validators import RegexValidator


# Create your models here.
class Emails(models.Model):
    alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')
    first_name = models.CharField(max_length=50, blank=False, null=False, validators=[alphabetic])
    last_name = models.CharField(max_length=50, blank=False, null=False, validators=[alphabetic])
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)

    class Meta:
        managed = True
        db_table = 'emails'


class EmailsForm(ModelForm):
    agree_term = forms.BooleanField(required=True, label='Agree to terms')
    class Meta:
        model = Emails
        fields = ['first_name', 'last_name', 'email' ]
        """labels = {
            'first_name': _(''),
            'last_name': _(''),
            'email': _('')
        }
        help_texts = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'email': _('Email')
        }"""
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control input-lg'}),
            'last_name': forms.TextInput(attrs={'class':'form-control input-lg'}),
            'email': forms.TextInput(attrs={'class':'form-control input-lg'})
        }

