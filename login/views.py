from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import mobile
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.session.has_key('is-logged'):
        return redirect('home')
    else:
        return render(request,'login.html')

## login and home view
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    ## object for dynamic contents
    mobile1 = mobile()
    mobile1.name = 'OnePlus 9R 5G'
    mobile1.description = 'The OnePlus is a line of smartphones designed and marketed by Apple Inc. that use Apple' 

    mobile2 = mobile()
    mobile2.name = 'iphone 7plus'
    mobile2.description = 'The OnePlus is a line of smartphones designed and marketed by Apple Inc. that use Apple' 


    mobile3 = mobile()
    mobile3.name = 'iphone 8plus'
    mobile3.description = 'The iphone 8plus is a line of smartphones designed and marketed by Apple Inc. that use Apple' 


    mobile4 = mobile()
    mobile4.name = 'iphone 10'
    mobile4.description = 'The iphone 10 is a line of smartphones designed and marketed by Apple Inc. that use Apple' 


    mobile5 = mobile()
    mobile5.name = 'iphone 11pro'
    mobile5.description = 'The iphone 11pro is a line of smartphones designed and marketed by Apple Inc. that use Apple' 


    mobile6 = mobile()
    mobile6.name = 'iphone 12pro'
    mobile6.description = 'The iphone 12pro is a line of smartphones designed and marketed by Apple Inc. that use Apple' 


    mobiles = [mobile1,mobile2,mobile3,mobile4,mobile5,mobile6]

    if request.session.has_key('is-logged'):
        return render(request,'home.html', {'mobiles':mobiles})
    else:
        return redirect(login)

## email and password checking
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
        # print('okfj')
        if request.method == 'POST':
            val1 = request.POST.get("email1")
            val2 = request.POST.get("passwords")
            val3 = "mejokkurian06@gmail.com"
            val4 = "123"
            # print(val1,val2)

            if val1 == val3 and val2 == val4:
                request.session['is-logged'] = True
                messages.success(request,"")   
                return redirect(home)
            else:
                # print("jkih")
                messages.error(request,"Incorrect email or password!!!")
                return redirect(login)
        else:
            return redirect(home)

## logout 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    if request.session.has_key('is-logged'):
        del request.session['is-logged']
    return redirect(login)
      




     

            



    



     

    

    

