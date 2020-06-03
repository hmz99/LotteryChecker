from django.db import models

# Create your models here.

# Model to store all winning tickets
class WinningNumbers(models.Model):
    WB1 = models.IntegerField()
    WB2 = models.IntegerField()
    WB3 = models.IntegerField()
    WB4 = models.IntegerField()
    WB5 = models.IntegerField()
    RB = models.IntegerField()
    DD = models.DateField()

