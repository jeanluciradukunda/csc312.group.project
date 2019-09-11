from django.shortcuts import render
from .models import DVD
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
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
def clerk(request):
    dvds = DVD.objects.all() #imports dvds from database

    query = request.GET.get("query")
    if query:
        dvds = DVD.objects.filter(Q(Title__icontains=query)) #Search Function according to name

    paginator = Paginator(dvds, 6) # Show 3 dvds per page
    page = request.GET.get('page')
    dvds = paginator.get_page(page)  
    form=DocumentForm()
    context_dict = { 'dvds':dvds ,'form': form}
    return render(request, 'clerk.html',context_dict)

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
    numOfDays=request.POST['numDaysBooked']
    if(str(dvdID)!="" and str(numOfDays)!=""):
        DVD.objects.filter(id=dvdID).update(BookingPickup=username,NumDaysBooked=numOfDays,InStock=False)

    return redirect('home')