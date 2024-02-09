from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .models import*


def index(request):
    return render(request, 'index.html')

def about(request):
    about  = About.objects.all()
    return render(request, 'about.html', {'about' : about})



def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html',{'blog' :  blog})

def car(request):
    car = Car.objects.all()
    return render(request, 'car.html', {'car' : car})

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['password2']

        if password == confirm:
            email_exists = User.objects.filter(email=email).exists()
            username_exists = User.objects.filter(username=username).exists()
            if email_exists:
                messages.info(request, 'Email Already Used')
                return redirect(reverse('registration'))
            elif username_exists:
                messages.info(request,'Username already used')
                return redirect(reverse('registration'))
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords did not match each other')
            return redirect(reverse('registration'))
    else:
        return render(request, 'registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse('index'))
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect(reverse('login'))
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')



def contact(request):
    contact = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        from_email = request.POST.get('email')
        phone = request.POST.get('phone')
        message_body = f'\n {message} \n Sent By: {from_email}\n Phone Number={phone}'

        if name and message and from_email:
            try:
                send_mail('Subject', message_body, phone, ['shaxbozaxrorov01@gmail.com'])
                messages.success(request, 'Your message has been sent')
            except BadHeaderError:
                messages.warning(request, 'Invalid header found.')
        else:
            messages.warning(request, 'Make sure all fields are entered and valid.')
        return redirect('/')

    return render(request, 'contact.html', {'contact' : contact})

