from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from CMS.views import ResetPasswordView
import CMS.views as CMSViews
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,template_name='login.html'), name="login"),
    #path('MyProfile/<int:pk>',Accounts_views.MyProfile.as_view(template_name="MyProfile.html"),name="MyProfile"),
    path('',CMSViews.CMSHome,name='CMSHome'),
    path('ManageBlogs/',CMSViews.ManageBlogs.as_view(),name='ManageBlogs'),
    path('ManageWebPages/',CMSViews.ManageWebPages.as_view(),name='ManageWebPages'),
    path('CreateBlog/',CMSViews.CreateBlog.as_view(),name="CreateBlog"),
    path('CreateWebPages/',CMSViews.CreateWebPages.as_view(),name="CreateWebPages"),

    path('DeleteBlog/<int:pk>',CMSViews.DeleteBlog.as_view(),name="DeleteBlog"),
    path('DeleteWebPage/<int:pk>',CMSViews.DeleteWebPage.as_view(),name="DeleteWebPage"),

    path('UpdateBlog/<int:pk>',CMSViews.UpdateBlog.as_view(),name="UpdateBlog"),
    path('UpdateWebPage/<int:pk>',CMSViews.UpdateWebPage.as_view(),name="UpdateWebPage"),

    path('ManageProfile/<int:pk>/',CMSViews.ManageProfile.as_view(),name="ManageProfile"),

     path(
        'change_password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change_password.html',
            success_url = reverse_lazy('CMSHome')
        ),
        name='change_password'
    ),

]