from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

#from emailsubmission.forms import EmailForm
from emailsubmission.models import Emails, EmailsForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailsForm(request.POST)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            
            send_mail(
                'Thank you!',
                'Welcome to the club! We are aiming to push out the service by June. We will be looking for beta testers and stylists. Feel free to contact us for any questions at clubmannercanada@gmail.com.',
                'clubmannercanada@gmail.com',
                [request.POST.get('email')],
                fail_silently=True,
            )
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailsForm()

    return render(request, 'index.html', {'form': form})

def get_about(request):
    return render(request, 'about.html')

def get_thanks(request):
    return render(request, 'thanks.html')