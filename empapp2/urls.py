from django.urls import path
from . import views

urlpatterns = [
    path("admin_home/",views.admin_home,name="admin_home"),
    path("admin_login/",views.admin_login,name="admin_login"),
    path("logout_admin/",views.logout_admin,name="logout_admin"),
    path("admin_chnagepassword/",views.admin_changepassword,name="admin_changepassword"),
    path("all_employee/",views.all_employee,name="all_employee"),
    path("delete_employee/<int:pid>",views.delete_employee,name='delete_employee'),
    path("edit_admin_profile/<int:pid>",views.edit_admin_profile,name="edit_admin_profile"),
    path("edit_admin_education/<int:pid>",views.edit_admin_education,name="edit_admin_education"),
]
