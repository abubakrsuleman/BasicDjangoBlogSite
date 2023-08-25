from django.urls import path
from . import views
from .views import Home,ViewBlog
urlpatterns = [
    path('About/', views.AboutPage, name="About"),
    #path('', views.Home, name="Home"),
    path('', Home.as_view(template_name = "Home.html"), name="Home"),
    path('ViewBlog/<int:pk>', ViewBlog.as_view(template_name = "ViewBlog.html"), name="ViewBlog"),
    path('Contact/',views.Contact, name="Contact"),


]