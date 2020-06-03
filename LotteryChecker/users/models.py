from django.db import models
from django.contrib.auth.models import User

#Model to store User Tickets
class Ticket(models.Model):
    WB1 = models.IntegerField()
    WB2 = models.IntegerField()
    WB3 = models.IntegerField()
    WB4 = models.IntegerField()
    WB5 = models.IntegerField()
    RB = models.IntegerField()
    DD = models.DateField()
    status = models.CharField(max_length=50,default="Pending")
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)