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
import datetime
#This is the homepage for the User
    
def home(request):

    dvds = DVD.objects.all() #imports dvds from database
    
    query = request.GET.get("query")
    gen = request.GET.get("gen")
    if query: 
        dvds = DVD.objects.filter(Q(Title__icontains=query))#Search Function according to name
        if  not DVD.objects.filter(Q(Title__icontains=query)).exists():
            messages.info(request,'No search results for : '+query)
    elif gen:
        dvds = DVD.objects.filter(Q(genre__icontains=gen))#Search Function according to name


    paginator = Paginator(dvds, 6) # Show 3 dvds per page
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
    users_ID=request.POST['user_ID']
    MovieTitle=request.POST['MovieTitle']
    payment=request.POST['payment']
    bill=int(numOfDays)*int(dvdPrice)
    DVD.objects.filter(id=dvdID).update(NumDaysBooked=numOfDays,InStock=False)
    

    RentDate= datetime.date.today()
    
    DueDate=RentDate+datetime.timedelta(days=int(numOfDays))

    t = datetime.datetime.now().strftime("%H%M%S")
    TransactionNumber=payment+str(RentDate)[0:4]+str(RentDate)[8:10]+t
    
    #Amount
    trans = Transaction(users_ID=users_ID, TransactionNumber=TransactionNumber, RentDate=RentDate, DueDate=DueDate, MovieTitle=MovieTitle, Payment_Method=payment,Amount="R"+str(bill),dvdID=dvdID)
    trans.save()


    return redirect('/clerk')


def checkin(request):
    dvdID= request.POST['dvdID']
    DVD.objects.filter(id=dvdID).update(BookingPickup='None',InStock=True,NumDaysBooked=0)
    return redirect('/clerk')

def deleteMovie(request):
    dvdID= request.POST['dvdID']
    DVD.objects.filter(id=dvdID).delete()
    return redirect('/clerk')

def deleteTransaction(request):
    transID= request.POST['transID']
    Transaction.objects.filter(id=transID).delete()
    return redirect('/transactions')

def deleteUser(request):
    userID= request.POST['userID']
    User.objects.filter(id=userID).delete()
    return redirect('/userstbl')


def user_detail(request):
    id = None
    if request.user.is_authenticated:
        id = request.user.id
    print(id)
    detail2 = Customer.objects.all()
    detail1 = User.objects.filter( id = id )

    detail2 = Customer.objects.filter(id = id ).values()
    if detail2!="":
        phone_number=(str(detail2[0]['phone_number']))
        identification=(str(detail2[0]['identification']))
        address=(str(detail2[0]['address']))
        return render(request, 'user_detail.html',{'detail1':detail1 , phone_number,phone_number:phone_number})

    return render(request, 'user_detail.html',{'detail1':detail1 , 'detail2' : detail2})

def registerCustomer(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        phone_number= request.POST['phone_number']
        address= request.POST['address']
        identification= request.POST['identification']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        username= request.POST['username']

        if password1 == password2 :
            if Customer.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register.html')
            elif Customer.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register.html')
            user = Customer.objects.create_user(phone_number=phone_number, address=address,identification=identification,username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            # customer = Customer.objects.create_user(phone_number=phone_number,identification=identification,address=address)
            user.save()
            # customer.save()
            messages.info(request, 'User Created')
            # messages.info(request, 'Customer Created')
            return redirect('login.html')
        else:
            print('password does not match')
            messages.info(request, 'Password does not match')
            return redirect('register.html')

        return redirect('login.html')

    else:
        return render(request, 'register.html')

def updateCustomer(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        phone_number= request.POST['phone_number']
        address= request.POST['address']
        identification= request.POST['identification']
        email= request.POST['email']
        username= request.POST['username']
        userID=request.POST['userID']
        
        user = Customer.objects.filter(id=userID).update(phone_number=phone_number, address=address,identification=identification,username=username, email=email, first_name=first_name, last_name=last_name)
        # customer = Customer.objects.create_user(phone_number=phone_number,identification=identification,address=address)
        return redirect('home')

def updateUser(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        email= request.POST['email']
        username= request.POST['username']
        userID=request.POST['userID']
        
        user = User.objects.filter(id=userID).update(username=username, email=email, first_name=first_name, last_name=last_name)
        # customer = Customer.objects.create_user(phone_number=phone_number,identification=identification,address=address)
        return redirect('home')

