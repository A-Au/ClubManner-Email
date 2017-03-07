from django.db import models
from django.forms import ModelForm


# Create your models here.
class Emails(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.first_name

    class Meta:
        managed = True
        db_table = 'emails'

class EmailsForm(ModelForm):
    class Meta:
        model = Emails
        fields = ['first_name', 'last_name', 'email']
