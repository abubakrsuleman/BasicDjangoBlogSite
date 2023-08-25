from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from .models import *
from Blogs.models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

class Home(ListView):
    model = Blog
    ordering = ['-id']
    def get_queryset(self):
        return Blog.objects.all()
    context_object_name = 'blogs'
    paginate_by = 3

class ViewBlog(DetailView):
    model = Blog
    context_object_name = 'blog'

def AboutPage(request):
    return render(request, 'About.html',{'page': webpages.objects.filter(webpage_type = 'ABOUT')})
def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('first_name') + " " + form.cleaned_data.get('last_name')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            email_addr = form.cleaned_data.get('email_address')
            fullMessage= "Full Name"+ name + " Subject: " + subject + " Message: " + message + " Contact Email "+email_addr
            recipinet_list = ['abubakrsuleman13alt@gmail.com']
            send_mail(subject,fullMessage,email_addr,recipinet_list,fail_silently=False)
            messages.success(request, f'Your inquiry, {name} has been sent!') 
            return redirect('Home')
    else: form = ContactForm()
    return render(request,'Contact.html',{'form':form})