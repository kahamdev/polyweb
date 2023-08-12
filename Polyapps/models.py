from django.db import models


# Create your models here.
class About(models.Model):
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.description


class Contact(models.Model):
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=12)

    def __str__(self):
        return self.phone
    
    

class Specialist(models.Model):
      name=models.CharField(max_length=100)
      position=models.CharField(max_length=100)
      phone=models.IntegerField()
      email=models.EmailField(max_length=100)
      time=models.DateTimeField(auto_now_add=False)

      def __str__(self):
          return self.name
      


     