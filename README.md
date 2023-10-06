# EmployeeManagement
The Employee Management System is a web-based application built using Django, JavaScript, HTML, CSS, and MySQL. This project manages their employee data efficiently. It consists of two main applications: empapp1 for employee-related operations and empapp2 for administrative functions.


## Project Structure

- Employee_Management_System
     - Employee_Management_System
          - __init__.py
          - asgi.py
          - settings.py
          - urls.py
          - wsgi.py
     - empapp1
          - __init__.py
          - admin.py
          - apps.py
          - forms.py
          - models.py
          - tests.py
          - urls.py 
          - views.py
     - empapp2
          - __init__.py
          - admin.py
          - apps.py
          - forms.py
          - models.py
          - tests.py
          - urls.py 
          - views.py
     - static
          - empapp1
               - css
               - images
               - js
          - empapp1
               - css
               - images
               - js
     - templates
          - empapp1
               - all templates files
          - empapp2
               - all twmplates files
     - manage.py

## Features
1. User registration and login system
2. Employee profile management
3. Employee education details management
4. Employee experience details management
5. Admin login for staff or superusers
6. Admin can view, edit, and delete employee data
7. Admin can change their password
8. User-friendly interface


## Installation
To run this project on your local machine, follow these steps:

1. Clone the repository:
     ```git clone https://github.com/your-username/employee-management-system.git```
   
2. Navigate to the project directory:
    ```cd employee-management-system```
   
3. Create a virtual environment (recommended):
    ```python -m venv venv```
   
4. Activate the virtual environment:
    - On Windows:
          - ```venv\Scripts\activate```
      
5. Install the project dependencies:
      ```pip install -r requirements.txt```
   
6. Create and configure the MySQL database:
   - Create a MySQL database named "Employee_Management_System".
   - Update the database settings in Employee_Management_System/settings.py with your MySQL credentials.

7. Apply migrations to create database tables:
      ```python manage.py migrate```
   
8. Create a superuser account:
  ```python manage.py createsuperuser```
  
9. Run the development server:
    ```python manage.py runserver```
Access the web application in your browser at http://localhost:8000.

## Usage
  - Visit the application in your browser and create a user account or log in as an admin.
  - Users can manage their employee profiles, education, and experience details.
  - Admins can log in to access administrative functions such as viewing, editing, and deleting employee data.
  - Admins can also change their password.


### Access the web application in your browser at http://localhost:8000. it will gives this interface. 

![Screenshot 2023-10-06 181055](https://github.com/Rahul7434/EmployeeManagement/assets/138716867/28fda4c3-ecf6-4b23-91da-649966323abe)

### Note:- You have to log in to access all programs If you are not logged in then sign up, After logging in you will go to the profile page.

![Screenshot 2023-10-06 182127](https://github.com/Rahul7434/EmployeeManagement/assets/138716867/96a535ea-00dc-49bd-ba58-0f9babe0d3f5)
