from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from empapp1.models import *
from empapp1.form import *
from .form import *
from django.contrib.auth.models import User
#/*****************// Admin Login VIEW //***********************/
def admin_login(request):
    error=""
    user=request.user
    if request.method == "POST":
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(username=u,password=p)
        if not request.user.is_staff or  request.user.is_superuser:
            login(request,user)
            error='no'
        else:
            error="yes"
    return render(request,"empapp2/admin_login.html",{'error':error})

def admin_home(request):
    if not request.user.is_staff or request.user.is_superuser:
        return redirect("admin_login")
    return render(request,"empapp2/admin_home.html")

#/*****************// Logout VIEW //***********************/
def logout_admin(request):
    if not request.user.is_staff or request.user.is_superuser:
        logout(request)
    return redirect('index')

def admin_changepassword(request):
    if not request.user.is_staff or request.user.is_superuser:
        return redirect("admin_login")
    error=""
    user=request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        cn = request.POST['confirmpassword']
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
    return render(request,"empapp2/admin_changepassword.html",{'error':error})


def all_employee(request):
    if not request.user.is_staff or request.user.is_superuser:
        return redirect("admin_login")
    employee= EmployeeDetail.objects.all()
    return render(request,"empapp2/all_employee.html",{'employee':employee})



def delete_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    user=User.objects.get(id=pid)
    user.delete()
    return redirect('all_employee')



def edit_admin_education(request,pid):
    if not request.user.is_authenticated:
        return redirect('emplogin')

    error=""
    user=User.objects.get(id=pid)
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
    return render(request,"empapp2/edit_admin_education.html",context)


def edit_admin_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('emplogin')
    error=""
    user=User.objects.get(id=pid)
    try:
        employee = EmployeeDetail.objects.get(user=user)
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
        return render(request,"empapp2/edit_admin_profile.html",context)
    except EmployeeDetail.DoesNotExist:
        return HttpResponse("Employee profile not found.")