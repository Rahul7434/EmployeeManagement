from django.shortcuts import render,redirect ,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import check_password ,make_password
# Create your views here.
from .form import *
from .models import *

#/*****************// INDEX VIEW //***********************/
def index(request):
    return render(request,"empapp1/index.html")


#/*****************// Registration Signup VIEW //***********************/
def registration(request):
    error=""
    if request.method == "POST":
        fn=request.POST['first_name']
        ln=request.POST['last_name']
        ec=request.POST['empcode']
        em=request.POST['email']
        pwd=request.POST['password']
        try:
            user= User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            EmployeeDetail.objects.create(user=user,empcode=ec)
            EmployeeExperience.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)
            error="no"
        except:
            error="yes"
    #print("Error",error)
    context={'error':error}
    return render(request,"empapp1/registration.html",context)


#/*****************// Profile Update VIEW //***********************/
def profile(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    error=""
    user=request.user
    try:
        employee = EmployeeDetail.objects.get(user=user)
        # Process the retrieved employee object
        if request.method == "POST":
            fn=request.POST['first_name']
            ln=request.POST['last_name']
            ec=request.POST['empcode']
            em=request.POST['email']
            dm=request.POST['department']
            ds=request.POST['designation']
            co=request.POST['contact']
            jd=request.POST['joiningdate']
            gn=request.POST['gender']
            
            employee.user.first_name=fn
            employee.user.last_name=ln
            employee.user.username=em
            employee.empcode=ec
            employee.empdept=dm
            employee.designation=ds
            employee.contact=co
            employee.gender=gn
            if jd:
                employee.joiningdate=jd
            try:
                employee.save()
                employee.user.save()
                error="no"
            except:
                error="yes"
        context={'error':error,'employee':employee}
        return render(request,"empapp1/profile.html",context)
    except EmployeeDetail.DoesNotExist:
        return HttpResponse("Employee profile not found.")



#/*****************// Employee Login VIEW //***********************/
def emplogin(request):
    error=""
    if request.method == "POST":
        u=request.POST['email_id']
        p=request.POST['password']
        user= authenticate(username=u,password=p)
        if user:
            login(request, user)
            error="no"
        else:
            error="yes"
    context={'error':error}
    return render(request,"empapp1/emplogin.html",context)


#/*****************// Employee Profile detaol  VIEW //***********************/
def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    return render(request,"empapp1/emp_home.html")


#/*****************// Logout VIEW //***********************/
def logout_user(request):
    logout(request)
    return redirect('index')


#/*****************// Employee Experience Detail VIEW //***********************/
def experience_view(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    
    user=request.user
    try:
        experience = EmployeeExperience.objects.get(user=user)
    except EmployeeExperience.DoesNotExist:
        experience=None
    return render(request,"empapp1/experience.html",{'experience':experience})



#/*****************// Employee Experience Update  VIEW //***********************/

def edit_experience_view(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    user=request.user
    try:
        experience = EmployeeExperience.objects.get(user=user)
    except EmployeeExperience.DoesNotExist:
        experience = None
    error=""
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            form.save()
            error="yes"
            #return redirect('experience')  # Redirect to the desired URL after successful save
        else:
            error="no"
    else:
        form = ExperienceForm(instance=experience)
    context={'error':error,'form':form}
    return render(request,"empapp1/edit_experience.html",context)

#********************// Edication View //*****************
def education(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    user=request.user
    try:
        education = EmployeeEducation.objects.get(user=user)
    except:
        education = None
    return render(request,"empapp1/education.html",{'education':education})

#*********************// Edit Education View //****************

def edit_education(request):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    user=request.user
    
    try:
        education =EmployeeEducation.objects.get(user=user)
    except EmployeeEducation.DoesNotExist:
        education=None
    error=""
    if request.method == "POST":
        form = EmployeeEducationForm(request.POST, instance=education)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.user=user
            form.save()
            error="no"
        else:
            error="yes"
    else:
        form = EmployeeEducationForm(instance=education)
    context={'error':error,'form':form}
    return render(request,"empapp1/edit_education.html",context)

        
def change_password(request):
    if not request.user.is_authenticated:
        return redirect("emplogin")
    error=""
    user=request.user
    if request.method == "POST":
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
        cn=request.POST['confirmpassword']
        try:
            if user.check_password(c):
                if n==cn:
                    user.set_password(n)
                    user.save()
                    error="no"
                else:
                    error="cp"
            else:
                error="not"
        except:
            error="yes"
    return render(request,"empapp1/changepassword.html",{'error':error})

