from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmployeeDetail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    empcode=models.CharField(max_length=50)
    empdept=models.CharField(max_length=50,null=True)
    designation=models.CharField(max_length=50,null=True)
    contact=models.CharField(max_length=60,null=True)
    gender=models.CharField(max_length=50,null=True)
    joiningdate=models.DateField(null=True)
    def __str__(self):
        return self.user.username
    

class EmployeeEducation(models.Model):
    # Post Graducation Fields
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course_pg=models.CharField(max_length=200)
    clg_name_pg=models.CharField(max_length=200,null=True)
    year_of_passing_pg=models.CharField(max_length=50,null=True)
    persentage_pg=models.CharField(max_length=60,null=True)
    
    # Graducation FIelds
    course_g=models.CharField(max_length=200)
    clg_name_g=models.CharField(max_length=200,null=True)
    year_of_passing_g=models.CharField(max_length=50,null=True)
    persentage_g=models.CharField(max_length=60,null=True)
    
    # SSC Fields
    course_ssc=models.CharField(max_length=200)
    school_name_ssc=models.CharField(max_length=200,null=True)
    year_of_passing_ssc=models.CharField(max_length=50,null=True)
    persentage_ssc=models.CharField(max_length=60,null=True)
    
    # HSC Fields
    course_hsc=models.CharField(max_length=200)
    school_name_hsc=models.CharField(max_length=200,null=True)
    year_of_passing_hsc=models.CharField(max_length=50,null=True)
    persentage_hsc=models.CharField(max_length=60,null=True)
    def __str__(self):
        return self.user.username
    

class EmployeeExperience(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company1_name=models.CharField(max_length=50)
    company1_desig=models.CharField(max_length=50,null=True)
    company1_duration=models.CharField(max_length=50,null=True)
    company1_salary=models.CharField(max_length=60,null=True)
    
    company2_name=models.CharField(max_length=50)
    company2_desig=models.CharField(max_length=50,null=True)
    company2_duration=models.CharField(max_length=50,null=True)
    company2_salary=models.CharField(max_length=60,null=True)
    
    company3_name=models.CharField(max_length=50)
    company3_desig=models.CharField(max_length=50,null=True)
    company3_duration=models.CharField(max_length=50,null=True)
    company3_salary=models.CharField(max_length=60,null=True)
    def __str__(self):
        return self.user.username

