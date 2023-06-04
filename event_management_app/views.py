# import functions to render html page and redirect user
from django.shortcuts import render, redirect
# importing the forms
from .forms import Create_Event_Form, RegisterUserForm, Login_form, Profile_form
#import the models(tables)
from .models import Events, Event_User

import datetime
#import function to support login, logout and signup functionablity
from django.contrib.auth import login, authenticate, logout
#importing the decorator to check that the user is logged in or not
from django.contrib.auth.decorators import login_required
#import the django user
from django.contrib.auth.models import User

#function used as key to sort the Event object according to date first then time
def sub_list(data1, data2):
    data3 = []
    for i in data1:
        if i not in data2:
            data3.append(i)
    return data3



#Function returns the homepage
def home(request):
    today_date = datetime.date.today()
    current = datetime.datetime.now()
    current_time = current.time()
    data = list(Events.objects.values('id','name', 'date', 'start_time', 'end_time').filter(date__gt=today_date))
    # data contain the list of event that who's date is greater than today's date
    current_date_data = list(Events.objects.values('name', 'date', 'start_time', 'end_time').filter(end_time__gt=current_time).filter(date=today_date))
    # data contain the list of event that who's date is equal to today's date but the event end time is greater than current time
    for i in current_date_data:
        data.append(i)
    #sorting the data in descending order
    data.sort(key= lambda ele: (ele['date'], ele['start_time']))
    # fetching all the records present in Events table to get the past data for that we are subtracting current data from past
    all_data = list(Events.objects.values('id','name', 'date', 'start_time', 'end_time').all())
    past_data = sub_list(all_data.copy(), data.copy())
    past_data.sort(key= lambda ele: (ele['date'], ele['start_time']),reverse=True)
    return render(request, 'home.html', context={'data':data,'past_data': past_data})

#allow users to create a event
#if user if not logged in then he/she will not be able to see the create_event page he/she needs to login first
@login_required(login_url="/signin")
def create_event(request):
    if request.method== "POST": # check wheather the request is post or not
        form = Create_Event_Form(request.POST) # populate the form with the data sent by user
        if form.is_valid(): # check that form is valid or not(wheather the user have provided proper data or not)
            form.save() # create a new record in the Events table
    form = Create_Event_Form()
    return render(request, "Create_Event.html", context={
        'form':form,
    })

#allow users to get the details of the event
#if user if not logged in then he/she will not be able to see the create_event page he/she needs to login first
@login_required(login_url="/signin")
def get_event_details(request, id):
    data = Events.objects.filter(id=id) # try yo filter the Events by id
    if len(data) != 1: # will check wheather the record exists or not
        return render(request, 'error.html',context={'error':"Event Doesn't exists"}) # return ths error page if the event doesn't exists
    data = data[0]
    is_event_active = True
    if data.date < datetime.date.today(): # check wheater the the events occured in past or not
        is_event_active = False
    elif data.date == datetime.date.today(): # check wheater the the events occured in past or not
        current = datetime.datetime.now()
        current_time = current.time()
        if data.end_time < current_time: # if the event occured today the it check that is event going on or not
            is_event_active = False
    return render(request, "event_details.html", context={'data':data, 'is_event_active':is_event_active})

#user signup/register function
def create_user(request):
    if request.method == "POST": # check wheather the request is post or not
        form = RegisterUserForm(request.POST)
        if form.is_valid(): # check that form is valid or not(wheather the user have provided proper data or not)
            user = form.save()
            login(request, user) # function used to login the user 
            return redirect('Homepage') # will redirect user to homepage
        field = None
        for i in form.errors: # if form contains error is it contains error will append those error in our error list and will pass these details to template
            field = i
        errors = form.errors[field]
        return render(request, "user_register.html", context={'form': form, 'errors':errors})
    form = RegisterUserForm()
    return render(request, "user_register.html", context={'form': form})


#login user code
def login_user(request):
    if request.method == "POST": # check wheather the request is post or not
        form = Login_form(data=request.POST)
        redirect_uri = request.GET.get('next') # check if we have next in url parameter the after login it will be redirect to that page else it will be redirect tto homepage
        if form.is_valid(): # check that form is valid or not(wheather the user have provided proper data or not)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) # authenticate the user 
            if user is not None:
                login(request, user) 
                if redirect_uri != None:
                    return redirect(redirect_uri) # will redirect user to the previous page
                return redirect('Homepage') # will redirect user to home page
        errors = ["Invalid username or password."]
        return render(request,"user_login.html",context={'form': form,'errors':errors})
    form = Login_form()
    return render(request, "user_login.html", context={'form': form})

#allow users to logout
#if user if not logged in then he/she will not be able to see the create_event page he/she needs to login first
@login_required(login_url="/signin")
def logout_user(request):
    logout(request)
    return redirect("Homepage")

#allow users to see and edit there profile
#if user if not logged in then he/she will not be able to see the create_event page he/she needs to login first
@login_required(login_url="/signin")
def profile(request):
    if request.method == "POST": # check wheather the request is post or not
        user_form = Profile_form(request.POST, instance=request.user) # passes user data to Profile_form form with user data who is currently logged in
        if user_form.is_valid(): # check that form is valid or not(wheather the user have provided proper data or not)
            user_form.save()
            message = ['User Details Updated']
            return render(request,'profile.html', context={'form':user_form,'message':message})
        errors = ['User Details Not Updated(Please try again)']
        field = None
        for i in user_form.errors: # check that the error of form data which is further passed to template
            field = i
            errors = user_form.errors[field]
        return render(request,'profile.html', context={ 'form':user_form,'errors':errors})
    user_id = request.user.id # get id of details currently logged in user
    user_details = User.objects.filter(id=user_id) # fetch details of currently logged in user
    if len(user_details) != 1:
        errors = ["User Not Found"]
        return render(request,"error.html",context={'errors':errors})
    user_details = user_details[0]
    user_form_dict = {'username': user_details.username,'first_name':user_details.first_name,'last_name':user_details.last_name,'email':user_details.email}
    form = Profile_form(user_form_dict)
    return render(request,'profile.html', context={'user_details':user_details, 'form':form})

#allow users to create a event
#allow user to register for an event
@login_required(login_url="/signin")
def event_register(request, event_id):
    user = request.user # ge the user instance(details to currently logged in user)
    event = Events.objects.filter(id=event_id) # get the event details
    if len(event) == 1: # check event exists or not
        event = event[0]
        if len(Event_User.objects.filter(user=user).filter(event = event)) > 0: # cehck record exists or not( is it exists the error will be displayed)
            return render(request, 'error.html',context={'error':'You have already register for this event'})
        register = Event_User(user= user, event = event)
        register.save()
        return render(request,'event_register.html', context={'event_name':event.name})
    return render(request, 'error.html',context={'error':"Event Doesn't exists"})
