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
                'THIS IS A TEST',
                'FYI: SINCE WE HAVE YET TO LAUNCH, YOUR INFO WILL BE DELETED DAILY AS WE CONTINUE TO BUILD OUT OUR SYSTEM',
                'clubmannercanada@gmail.com',
                [request.POST.get('email')],
                fail_silently=False,
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
