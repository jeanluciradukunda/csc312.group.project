from django.shortcuts import render
from .models import DVD, Transaction, Customer
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, permission_required
from .form import DocumentForm
#This is the homepage for the User
    
def home(request):

    dvds = DVD.objects.all() #imports dvds from database
    
    query = request.GET.get("query")
    gen = request.GET.get("gen")
    if query: 
        dvds = DVD.objects.filter(Q(Title__icontains=query))#Search Function according to name
    elif gen:
        dvds = DVD.objects.filter(Q(genre__icontains=gen))#Search Function according to name

    paginator = Paginator(dvds, 3) # Show 3 dvds per page
    page = request.GET.get('page')
    dvds = paginator.get_page(page)  
    
    genre = {'Action', 'Comedy', 'Drama', 'Family', 'Romance'}

    return render(request, 'home.html', {'dvds':dvds}, {'genre':genre}) #renders the page

#This is the page for clerks

@login_required

def clerk(request):
    dvds = DVD.objects.all() #imports dvds from database
    trans = Transaction.objects.all() #imports dvds from database
    users = User.objects.all() #imports dvds from database
    customer = Customer.objects.all() #imports dvds from database

    query = request.GET.get("query")
    if query:
        dvds = DVD.objects.filter(Q(Title__icontains=query)) #Search Function according to name

    paginator = Paginator(dvds, 6) # Show 3 dvds per page
    page = request.GET.get('page')
    dvds = paginator.get_page(page)  
    form=DocumentForm()
    context_dict = { 'dvds':dvds ,'form': form, 'trans':trans, 'users':users, 'customer':customer}
    return render(request, 'clerk.html',context_dict)

@login_required
def userstbl(request):
    dvds = DVD.objects.all() #imports dvds from database
    trans = Transaction.objects.all() #imports dvds from database
    users = User.objects.all() #imports dvds from database
    customer = Customer.objects.all() #imports dvds from database

    query = request.GET.get("query")
    if query:
        users = User.objects.filter(Q(username__icontains=query)) #Search Function according to name

    paginator = Paginator(dvds, 6) # Show 3 dvds per page
    page = request.GET.get('page')
    dvds = paginator.get_page(page)  
    form=DocumentForm()
    context_dict = { 'dvds':dvds ,'form': form, 'trans':trans, 'users':users, 'customer':customer}
    return render(request, 'userstbl.html',context_dict)

@login_required
def transactions(request):
    dvds = DVD.objects.all() #imports dvds from database
    trans = Transaction.objects.all() #imports dvds from database
    users = User.objects.all() #imports dvds from database
    customer = Customer.objects.all() #imports dvds from database

    query = request.GET.get("query")
    if query:
        trans = Transaction.objects.filter(Q(TransactionNumber__icontains=query)) #Search Function according to name

    paginator = Paginator(dvds, 6) # Show 3 dvds per page
    page = request.GET.get('page')
    dvds = paginator.get_page(page)  
    form=DocumentForm()
    context_dict = { 'dvds':dvds ,'form': form, 'trans':trans, 'users':users, 'customer':customer}
    return render(request, 'transactions.html',context_dict)

def register2(request):

    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password1= first_name[0]+last_name
        

        if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('clerk')
        elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        messages.info(request, 'User Created')

    return redirect('/clerk')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
    return redirect('/clerk')



def booking(request):

    username= request.POST['username']
    dvdID= request.POST['dvdID']
    DVD.objects.filter(id=dvdID).update(BookingPickup=username)

    return redirect('home')

def checkout(request):
    dvdID= request.POST['dvdID']
    numOfDays=request.POST['numDaysBooked']
    dvdPrice=request.POST['dvdPrice']
    bill=numOfDays*dvdPrice
    DVD.objects.filter(id=dvdID).update(NumDaysBooked=numOfDays,InStock=False)
    trans = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        trans.save()


    return render(request, 'clerk.html',{'bill':bill})

def checkoutProceed(request):
    dvdID= request.POST['dvdID']
    numOfDays=request.POST['numDaysBooked']

    DVD.objects.filter(id=dvdID).update(NumDaysBooked=numOfDays,InStock=False)


    return redirect('/clerk')



def checkin(request):
    dvdID= request.POST['dvdID']
    DVD.objects.filter(id=dvdID).update(BookingPickup='None',InStock=True,NumDaysBooked=0)
    return redirect('home')