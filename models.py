from django.db import models

class Card(models.Model):
    number = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    shading = models.CharField(max_length=10)
    shape = models.CharField(max_length=10)

    def __str__(self):
        return (self.number+'_'+self.color+'_'+self.shading+'_'+self.shape)
