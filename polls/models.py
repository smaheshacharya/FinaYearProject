from django.db import models
from django import forms

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.question_text
# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=form.PasswordInput)
class Products(models.Model):
    title = models.CharField(max_length=120 )
    description = models.TextField(blank=True,null=True)
    price = models.IntegerField(default=0)
    summary = models.TextField(blank=False,null=False)
    featured = models.BooleanField(default=True)
