from django.shortcuts import render
from .models import DVD
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from django.db.models import Q


#This is the homepage for the User
def home(request):

    dvds = DVD.objects.all() #imports dvds from database
    
    query = request.GET.get("query")
    if query:
        dvds = DVD.objects.filter(Q(name__icontains=query))#Search Function according to name

    paginator = Paginator(dvds, 3) # Show 3 dvds per page
    page = request.GET.get('page')
    dvds = paginator.get_page(page)  

    return render(request, 'home.html', {'dvds':dvds}) #renders the page

#This is the page for clerks
def clerk(request):
    dvds = DVD.objects.all() #imports dvds from database

    query = request.GET.get("query")
    if query:
        dvds = DVD.objects.filter(Q(name__icontains=query)) #Search Function according to name

    paginator = Paginator(dvds, 3) # Show 3 dvds per page
    page = request.GET.get('page')
    dvds = paginator.get_page(page)  
    
    return render(request, 'clerk.html', {'dvds':dvds})

