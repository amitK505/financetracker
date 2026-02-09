from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.urls import path
from .models import dailyadd
from .models import Monthlyadd
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def home(request):
    a=""
    
        

        
    a={
        'name':request.session.get('name'),
        'gmail':request.session.get('gmail'),
            
    }
    
    return render(request,'index.html',a)
def sign(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('gmail')
        c=request.POST.get('password')
        
        
        
        
        myuser=User.objects.create_user(username=a,email =b,password=c )
        myuser.save()
        return redirect('/')
        

        
        
    return render(request,'signup.html') 
def loginnn(request):
    if request.method=="POST":
        d=request.POST.get('name')
        e=request.POST.get('password')
        user=authenticate(request,username=d,password=e)
        
        
        if user is not None:
            login(request,user)
            request.session['gmail']=d
            return redirect("home")
            
        else:
            return render(request,'login.html',{"error":True})
        
        
        
    return render(request,'login.html')
@login_required(login_url='login')
def daily(request):
    showdata=dailyadd.objects.filter(user=request.user).all()

    data={
        'grocery': request.session.get('grocery'),
        'onlinepayment':request.session.get('onlinepayment'),
        'datetime':request.session.get('datetime'),
        'total':request.session.get('total'),
        'showdata':showdata,
        'name':request.session.get('gmail'),
    }
    return render(request,'daily.html',data)
def updatedaily(request, id):
    expense=get_object_or_404(dailyadd ,id=id)
    if request.method=="POST":
        expense.grocery=int(request.POST.get('grocery') or 0)
        expense.onlinepayment=int(request.POST.get('onlinepayment') or 0)
        expense.total= expense.grocery + expense.onlinepayment

        expense.save()
        return redirect('daily')

    return render(request,'updatedaily.html',{'expense':expense})
def updatemonthly(request,id):
    updatemonthly=get_object_or_404(Monthlyadd,id=id)
    if request.method=="POST":
        updatemonthly.rent=int(request.POST.get('rent') or 0)
        updatemonthly.Utilities=int(request.POST.get('Utilities') or 0)
        updatemonthly.Subscriptions=int(request.POST.get('Subscriptions') or 0)
        updatemonthly.food=int(request.POST.get('food') or 0)
        updatemonthly.transport=int(request.POST.get('transport') or 0)
        updatemonthly.shopping=int(request.POST.get('shopping') or 0)
        updatemonthly.bank=int(request.POST.get('bank') or 0)
        updatemonthly.SIP=int(request.POST.get('SIP') or 0)
        updatemonthly.Festival=int(request.POST.get('Festival') or 0)
        updatemonthly.Medical=int(request.POST.get('Medical') or 0)
        updatemonthly.income=int(request.POST.get('income') or 0)
        updatemonthly.fixed_expenses =updatemonthly.rent+updatemonthly.Utilities+updatemonthly.Subscriptions
        updatemonthly.varaiable_expenses=updatemonthly.food+updatemonthly.transport+updatemonthly.shopping
        updatemonthly.saving=updatemonthly.bank+updatemonthly.SIP
        updatemonthly.sessional =updatemonthly.Festival+updatemonthly.Medical
        updatemonthly.totalspent=updatemonthly.rent+ updatemonthly.Utilities+updatemonthly.Subscriptions+updatemonthly.food+updatemonthly.transport+updatemonthly.shopping+updatemonthly.bank+updatemonthly.SIP+updatemonthly.Festival+updatemonthly.Medical
        updatemonthly.save()
        return redirect('monthly')
    return render(request,'updatemonthly.html')
def deletedaily(request,id):
    expense=get_object_or_404(dailyadd,id=id)
    expense.delete()
    return redirect('daily')
def deletemonthly(request,id):
    de=get_object_or_404(Monthlyadd,id=id)
    de.delete()
    return redirect('monthly')
@login_required(login_url='login')
def monthly(request):
    showdata2= Monthlyadd.objects.filter(user=request.user).all()   #to show data of all record for every unique person
    
        
        
    
    result={
        'month': request.session.get('month'),
        'income':request.session.get('income'),
        'totalspent':request.session.get('totalspent'),
        'fixed_expenses':request.session.get('fixed_expenses'),
        'varaiable_expenses':request.session.get('varaiable_expenses'), 
        'saving':request.session.get('saving'),
        'sessional':request.session.get('sessional'),
        'showdata2':showdata2,
        'name':request.session.get('gmail'),



    }
    return render(request,'monthly.html',result)
def add(request):
    ax=""
    ax={
        'name':request.session.get('gmail'),
        
    }
    
    if request.method =='POST':
        a=int(request.POST.get('grocery') or 0)
        b=int(request.POST.get('onlinepayment') or 0)
        c=request.POST.get('datetime')
        k=a+b
        data=dailyadd.objects.create( grocery= a,onlinepayment=b,datetime=c,total=k)
        
        data.user=request.user
        data.save()
       
    

        request.session['grocery']= a          #to show name ,email or other detail on another html page
        request.session['onlinepayment']= b
        request.session['datetime']= c
        request.session['total']=k
        return redirect('daily')

    return render(request,'add.html',ax)
def monthlyadd(request):
    if request.method=="POST":
        a=int(request.POST.get('rent') or 0)
        b=int(request.POST.get('Utilities') or 0)
        c=int(request.POST.get('Subscriptions') or 0)
        d=int(request.POST.get('food') or 0)
        e=int(request.POST.get('transport') or 0)
        f=int(request.POST.get('shopping') or 0)
        g=int(request.POST.get('bank') or 0)
        h=int(request.POST.get('SIP') or 0)
        i=int(request.POST.get('Festival') or 0)
        j=int(request.POST.get('Medical') or 0)
        k=int(request.POST.get('income') or 0)
        l=request.POST.get("month")
        totalspent = a+b+c+d+e+f+g+h+i+j
         
        fixed_expenses =a+b+c
        varaiable_expenses=d+e+f
        saving=g+h
        sessional =i+j
        monthlycreate = Monthlyadd.objects.create( rent=a,Utilities=b,Subscriptions=c,food=d,transport=e,shopping=f,bank=g,SIP=h,Festival=i,Medical=j,income=k,month=l,totalspent=totalspent,fixed_expenses=fixed_expenses,varaiable_expenses=varaiable_expenses,saving=saving,sessional=sessional)
        monthlycreate.user=request.user
        monthlycreate.save()
        

        request.session['month']=l
        request.session['income']=k
        request.session['totalspent']=totalspent
        request.session['fixed_expenses']=fixed_expenses
        request.session['varaiable_expenses']=varaiable_expenses
        request.session['saving']=saving
        request.session['sessional']=sessional
        return redirect('monthly')
        

    return render(request,"monthlyadd.html")
