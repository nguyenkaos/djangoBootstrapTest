from django.db import models

# Create your models here.
class utilisateur(models.Model):
    ### LOGIN ####
    userName = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    ### MODALES	#### 
    email = models.CharField(max_length=250,blank=True)	 
    def __str__(self):
        return   "userName:" + self.userName + "; Email :" + self.email