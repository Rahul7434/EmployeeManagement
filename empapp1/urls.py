
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    #path('registration/',views.registration,name='registration'),
    path('emplogin/',views.emplogin,name='emplogin'),
    path('emp_home/',views.emp_home,name="emp_home"),
    path('profile/',views.profile,name="profile"),
    path('registration/',views.registration,name="registration"),
    path('logout_user/',views.logout_user,name='logout'),
    path('exe/',views.experience_view,name="experience"),
    path('editexperience/',views.edit_experience_view,name="edit_experience"),
    path('education/',views.education,name="education"),
    path('edit_education/',views.edit_education,name="edit_education"),
    path('change_password/',views.change_password,name="change_password"),
]


