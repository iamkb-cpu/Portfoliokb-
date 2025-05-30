from django.shortcuts import render
#from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
import logging

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

#def contact(request):
 #   return render(request, 'contact.html')

def services_view(request):
    return render(request, 'services.html')

def about_view(request):
    return render(request, 'about.html')



from django.views.decorators.csrf import csrf_protect

@csrf_protect

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Compose email
        subject = f'New Contact Form Submission from {name}'
        email_message = f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}'
        from_email = 'keerthana3154@gmail.com'  # Match with DEFAULT_FROM_EMAIL
        recipient_list = ['keerthana3154@gmail.com']  # Your email to receive submissions

        try:
            send_mail(subject, email_message, from_email, recipient_list, fail_silently=False)
            return render(request, 'index.html', {'status': 'Message sent successfully!'})
        except Exception as e:
            return render(request, 'index.html', {'status': f'Error sending message: {str(e)}'})
    return render(request, 'index.html')