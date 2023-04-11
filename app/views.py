from django.shortcuts import render,HttpResponse, redirect
from .models import student


# Create your views 
def singuppage(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        passwordagain=request.POST['passwordagain']
        if password==passwordagain:
            try:
                a=student.objects.get(email=email)
                return render(request,'singup.html',{'error':'already exist'})
            #after login we send home page
                
            except student.DoesNotExist:
                stu=student.objects.create(name=name,email=email,password=password,passwordagain=passwordagain)
                stu.save()
                return redirect('login')
        else:
            return render(request,'singup.html',{'error':'password does not match'})
        
    return render(request,'singup.html')



def loginpage(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)
        # a=student.objects.get(email=email)
        # print(a.email)
        # print(a.name)
        # print(a.password)
        try:
            
            a=student.objects.get(email=email)
            if (email==a.email) and (password==a.password):
                return render(request,'singup.html',{'error':'you are login'}) 
            else:
                return render(request,'login.html',{'error':'your password is wrong'}) 
        except student.DoesNotExist:
            return render(request,'login.html',{'error':'your email does not match'}) 
    return render(request,'login.html')


