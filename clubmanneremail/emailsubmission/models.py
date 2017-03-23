from django.db import models
from django.forms import ModelForm
from django import forms
from django.core.validators import RegexValidator


# Create your models here.
class Emails(models.Model):
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)

    class Meta:
        managed = True
        db_table = 'emails'


class EmailsForm(ModelForm):
    agree_term = forms.BooleanField(required=True, label='Agree to terms')
    class Meta:
        model = Emails
        fields = [ 'email' ]

        widgets = {
            'email': forms.TextInput(attrs={'class':'form-control input-lg', 'placeholder': 'Email Address'})
        }

