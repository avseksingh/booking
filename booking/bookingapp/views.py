from django.shortcuts import render, HttpResponse
from . import utilities as ut
from .models import Registration
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, "index.html")

def reg(request):
    if request.GET:
        otp = ut.getOtp()
        user = request.GET['user']
        mobile = request.GET['mobile']
        address = request.GET['address']
        now = datetime.now() #now = 2021-06-25 07:58:56.550604
        # dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
        data = Registration(name=user, mobile=mobile, address=address, otp=otp, time=now)
        data.save()
        rawdata = Registration.objects.filter(mobile = mobile)
        return render(request, 'verify.html', {"otp": otp, "user": user, 'mobile': mobile, "rawdata": rawdata})
        # if request.GET:
        #     # userotp = request.GET['userotp']
        #     userotp = otp
        #     if userotp == otp:
        #         data = registration(name=user, mobile=mobile, address=address)
        #         data.save()
        #         return HttpResponse("OTP Verified Successfully")
        #     else:
        #         return HttpResponse("Invalid OTP")
                
        # return render(request, 'verifyuser.html', {"otp": otp, "user": user})
    return render(request, "registration.html")

def verify(request):
    rawdata = Registration.objects.all()
    if request.GET:
        # userotp=request.GET['userotpv']

        otp = request.GET['otp']
        userotp = otp
        if userotp == otp:
            return HttpResponse("OTP Verified Successfully")
        else:
            return HttpResponse("Invalid OTP")
        
    return render(request, 'verifyuser.html', {'rawdata': rawdata})

def rand(request):
    rnumber = ut.getOtp()
    return HttpResponse(rnumber)
