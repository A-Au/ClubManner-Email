from django.db import models
from django.forms import ModelForm
from django.core.validators import RegexValidator


# Create your models here.
class Emails(models.Model):
    alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')
    first_name = models.CharField(max_length=50, blank=False, null=False, validators=[alphabetic])
    last_name = models.CharField(max_length=50, blank=False, null=False, validators=[alphabetic])
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)
    agree_term = models.BooleanField()
    
    class Meta:
        managed = True
        db_table = 'emails'

class EmailsForm(ModelForm):
    class Meta:
        model = Emails
        fields = ['first_name', 'last_name', 'email', 'agree_term']

    def clean_agree_terms(self):
        data = self.clean_data['agree_term']
        if ! data :
            raise forms.ValidationError("You must agree to the terms")
        return data
