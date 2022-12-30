from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length= 20)
    mobile = models.CharField(max_length= 10, unique=True)
    address = models.CharField(max_length=50)
    otp = models.CharField(max_length=10)
    time = models.DateTimeField()
    
    def __str__(self):
        return ("Name = {}, Mobile = {}, Address = {}".format(self.name, self.mobile, self.address))

class login(models.Model):
    mobile = models.CharField(max_length= 10)
    otp = models.CharField(max_length = 4)
    time = models.DateTimeField()

    def __str__(self):
        return ("Mobile Number = {}, OTP = {}, Time = {}". format(self.mobile, self.otp, self.time))
