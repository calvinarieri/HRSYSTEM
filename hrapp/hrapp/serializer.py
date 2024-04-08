from rest_framework import serializers
from .models import Employee_skills, Employees, Leave_Application, Next_of_kin

class All_Employees(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'first_name', 'last_name', 'phone_number','email', 'password' , 'date', 'role', 'age', 'date_of_birth', 'home_adress']

class UserSkills(serializers.ModelSerializer):
    class Meta:
        model = Employee_skills
        fields = ['id', 'skill_title', 'level_of_education', 'school_name', "attain_year" , 'more_information', 'employee']

class Next_Of_Kin(serializers.ModelSerializer):
    class Meta:
        model = Next_of_kin
        fields = ['id' , 'first_name', 'last_name', 'relationship' , 'phone_number', 'email', 'employee']

class Leave_applications(serializers.ModelSerializer):
    class Meta:
        model=Leave_Application
        fields = ['id', 'reason', 'status','date', 'start_date', 'number_of_days', 'end_date', 'employee' ,'aproved_by']