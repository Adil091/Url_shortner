import random
from django.db import models
from django.utils import timezone

# Create your models here.
def code_generator(size=6, chars='abcdefghijklmnopqrstuvwxyz'):
    return ''.join(random.choice(chars) for _ in range(size))
class ShortzyURL(models.Model):
    url        =  models.CharField(max_length=220)
    shortcode  =  models.CharField(max_length=15,unique=True,null=True)
    updated    =  models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(default=timezone.now)
    #timestamp = models.DateTimeField(auto_now=false,auto_now_add=False)

    def save(self,*args,**kwargs):
        print("something")
        self.shortcode = code_generator()
        super(ShortzyURL,self).save(*args,**kwargs)



    def __str__(self):
        return str(self.url)
    def __unicode__(self):
        return str(self.url)
