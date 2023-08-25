from django.db import models
from django.utils.timezone import now
from django.conf import settings
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
class Blog(models.Model):
    title=models.CharField(max_length=100)
    brief_description = models.CharField(max_length=160, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=now, editable=False)
    Text = RichTextField(blank=True,null=True)
    def __str__(self): return self.title

