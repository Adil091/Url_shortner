from django.db import models


# Create your models here.
class ShortzyURL(models.Model):
    url        =  models.CharField(max_length=220)
    shortcode  =  models.CharField(max_length=15,unique=True,null=True)
    updated    =  models.DateTimeField(auto_now=True)
    timestamp  =  models.DateTimeField(auto_now_add=True)
    #timestamp = models.DateTimeField(auto_now=false,auto_now_add=False)


    def __str__(self):
        return str(self.url)
    def __unicode__(self):
        return str(self.url)
