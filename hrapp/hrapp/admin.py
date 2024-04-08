from django.contrib import admin
from .models import Employees , Leave_Application,Next_of_kin,Employee_skills

admin.site.register(Employee_skills)
admin.site.register(Employees)
admin.site.register(Leave_Application)
admin.site.register(Next_of_kin)
