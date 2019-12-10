from django.db import models

class enquiry(models.Model):
    Email = models.EmailField(default='')
    Enquiry = models.CharField(default='', max_length=200)
