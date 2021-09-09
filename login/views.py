from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.session.has_key('is-logged'):
        return redirect('home')
    else:
        return render(request,'login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if request.session.has_key('is-logged'):
        return render(request,'home.html')
    else:
        return redirect('login')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
        print('okfj')
        if request.method == 'POST':
            val1 = request.POST.get("email1")
            val2 = request.POST.get("passwords")
            val3 = "mejokkurian06@gmail.com"
            val4 = "123"
            print(val1,val2)

            if val1 == val3 and val2 == val4:
                request.session['is-logged'] = True
                messages.success(request,"")   
                return redirect('home')
            else:
                print("jkih")
                messages.error(request,"Incorrect email or password!!!")
                return redirect(login)
        else:
            return render(request,'home.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    del request.session['is-logged']
    return redirect('login')




     

            



    



     

    

    

