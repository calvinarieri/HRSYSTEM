from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import AbstractUser,PermissionsMixin

class Employees(AbstractUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=7)
    last_name = models.CharField(max_length=7)
    phone_number = models.CharField(max_length=7)
    email =models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=18)
    date = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=10)
    age = models.IntegerField(null=False)
    date_of_birth = models.DateField()
    home_adress = models.CharField(max_length=70)  
    username = models.CharField(max_length=60 ,unique=False) 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    
    def __str__(self) -> str:
        return  f"{self.first_name} {self.last_name}"
    def set_password(self, raw_password):
        """
        Sets the employee's password to the given raw string, hashing it for security.
        """
        self.password = make_password(raw_password)
    def check_password(self, raw_password):
        """
        Checks if the given raw password matches the hashed password of the employee.
        """
        return check_password(raw_password, self.password)    
    
class Next_of_kin(models.Model):
    id =models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=7)
    last_name= models.CharField(max_length=7)
    relationship= models.CharField(max_length=5)
    phone_number= models.CharField(max_length=7)
    email    = models.EmailField(max_length=40)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Employee_skills(models.Model):
    id = models.AutoField(primary_key=True)
    skill_title = models.CharField(max_length=20)
    level_of_education = models.CharField(max_length=60)
    school_name = models.CharField(max_length=40)
    attain_year = models.DateField()
    more_information =models.TextField()
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE , null=True) 

    def __str__(self):
        return f"{self.id}{self.skill_title} "
    
class Leave_Application(models.Model):
    id = models.AutoField(primary_key=True)
    reason = models.TextField()
    status =models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    number_of_days = models.IntegerField()
    end_date = models.DateField()
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE , null=True) 
    approved_by = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.id} {self.date}"


