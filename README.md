# EmployeeManagement
The Employee Management System is a web-based application built using Django, JavaScript, HTML, CSS, and MySQL. This project manages their employee data efficiently. It consists of two main applications: empapp1 for employee-related operations and empapp2 for administrative functions.

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
