from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=25)
    last_name  = models.CharField(max_length=25)
    age = models.IntegerField()
    salario = models.DecimalField(max_digits=6, decimal_places=2)
    bio = models.TextField()
    alive = models.Value(value=any)
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self): #Palavra que é mostrada no nome
        return self.first_name


