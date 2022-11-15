from django.db import models

# Create your models here.

class login(models.Model):
    mobile = models.IntegerField()
    otp = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return ("Mobile Number = {}, OTP = {}, Time = {}". format(self.mobile, self.otp, self.time))
