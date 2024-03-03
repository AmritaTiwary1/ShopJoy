from django.db import models


#makemigrations - create changes and store in file
#migrate - apply pending changes created by makemigrations
class Contact(models.Model):
    name = models.CharField(max_length=122) 
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
#below syntax will allow us to change the name of table content(forms) from contact(0),contact(1).. to name/email of the user who submit it
    def __str__(self):
        return self.email
    
