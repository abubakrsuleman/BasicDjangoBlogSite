from django.shortcuts import render,redirect
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView 
from django.views.generic.edit import DeleteView 
from django.views.generic.edit import UpdateView

from Blogs.models import *
from Base.models import *

# Create your views here.

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password-reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('Home')

def CMSHome(request):
    if request.user.is_superuser:
        return render(request, 'CMSHome.html',)
    else:
        return redirect('Home')

class ManageBlogs(UserPassesTestMixin,ListView):
    model = Blog
    paginate_by = 3
    def test_func(self):
        if self.request.user.is_superuser: return True
        else: return False
    template_name = 'ManageBlogs.html'
    context_object_name = 'blogs'

class ManageWebPages(UserPassesTestMixin,ListView):
    model = webpages
    paginate_by = 3
    def test_func(self):
        if self.request.user.is_superuser: return True
        else: return False
    template_name = 'ManageWebPages.html'
    context_object_name = 'webpages'

class CreateWebPages(UserPassesTestMixin, CreateView):
    model = webpages
    fields = ['HeaderTitle','Content','webpage_type']
    success_url = reverse_lazy('ManageWebPages')
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form) 
    def test_func(self):
        if self.request.user.is_superuser: return True
        else: return False
    template_name = 'CreateWebPages.html'

class CreateBlog(UserPassesTestMixin, CreateView):
    model = Blog
    fields = ['title','brief_description','Text']
    exclude = ['author','date_created']

    success_url = reverse_lazy('ManageBlogs')
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form) 
    def test_func(self):
        if self.request.user.is_superuser: return True
        else: return False
    template_name = 'CreateBlog.html'

class DeleteBlog(UserPassesTestMixin,DeleteView):
    model = Blog
    def test_func(self):
        if self.request.user.is_superuser: return True
        else: return False
    success_url = reverse_lazy('ManageBlogs') 
    template_name = 'DeleteBlog.html'

class DeleteWebPage(UserPassesTestMixin,DeleteView):
    model = webpages
    def test_func(self):
        if self.request.user.is_superuser: return True
        else: return False
    success_url = reverse_lazy('ManageWebPages') 
    template_name = 'DeleteWebPage.html'

class UpdateBlog(UserPassesTestMixin,UpdateView): 
    model = Blog
    fields = ['title','brief_description','Text']
    exclude = ['author','date_created']
    def test_func(self):
        if self.request.user.is_superuser: return True
        else: return False
    success_url = reverse_lazy('ManageBlogs') 
    template_name = 'UpdateBlog.html'

class UpdateWebPage(UserPassesTestMixin,UpdateView): 
    model = webpages
    fields = ['HeaderTitle','Content','webpage_type']
    exclude = ['author','date_created']
    def test_func(self):
        if self.request.user.is_superuser: return True
        else: return False
    success_url = reverse_lazy('ManageWebPages') 
    template_name = 'UpdateWebPage.html'


class ManageProfile(UserPassesTestMixin,UpdateView):
    model = User
    fields = ['username','email',]
    context_object_name = 'user'
    template_name = "ManageProfile.html"
    def test_func(self):
        if self.request.user.is_superuser: return True
        else: return False
    success_url = reverse_lazy('CMSHome')