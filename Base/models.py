# Create your models here.
from django.db import models
from django.utils.timezone import now
from django.conf import settings
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.contrib import messages

#def validate_unique_choices(value):
#    existing_choices = webpages.objects.values_list('webpage_type', flat=True)
#    if value in existing_choices:
#        raise ValidationError(f"Choice {value} is already in use.")

class webpages(models.Model):
    ABOUT = "ABOUT"
    #TERMS = "TERMS"
    #PRIVACY = "PRIVACY"
    Webpage_Choices = [
        (ABOUT, "About"),
    ]
    webpage_type = models.CharField(max_length=8, choices=Webpage_Choices)
    #validators=[validate_unique_choices]
    HeaderTitle=models.CharField(max_length=100)
    Content = RichTextField(blank=True,null=True)
    def __str__(self): return self.HeaderTitle +' Webpage'

#MakeMigrations then migrate before planning, implementing and testing out Webpage functionality.
#Use if statement or sql filters in django to find the relevent webpage for the view/url
#homepage will use a webpage called homepage, about use about, terms use terms if terms 
# and conditions is to be implemented
# alongside privacy policy page.