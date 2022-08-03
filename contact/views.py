from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.



def send_massage(request):
    
    if request.method == "POST":
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        messege = request.POST['messege']
        phone = request.POST['phone']
        send_mail(
        subject,
        messege,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        )
    return render(request, 'contact/contact.html', {})
