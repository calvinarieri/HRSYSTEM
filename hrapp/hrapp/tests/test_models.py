from django.test import TestCase
from hrapp.models import Employees, Next_of_kin, Employee_skills, Leave_Application
from datetime import date

class ModelsTestCase(TestCase):
    def setUp(self):
        # Create test data for Employees model
        self.employee = Employees.objects.create(
            first_name='John',
            last_name='Doe',
            phone_number='1234567',
            email='john@example.com',
            password='password',
            role='Developer',
            age=30,
            date_of_birth=date(1994, 5, 12),
            home_adress='123 Main St'
        )

        # Create test data for Next_of_kin model
        self.next_of_kin = Next_of_kin.objects.create(
            first_name='Jane',
            last_name='Doe',
            relationship='Spouse',
            phone_number='9876543',
            email='jane@example.com',
            employee=self.employee
        )

        # Create test data for Employee_skills model
        self.employee_skill = Employee_skills.objects.create(
            skill_title='Python',
            level_of_education='Bachelor',
            school_name='University of ABC',
            attain_year=date(2016, 5, 12),
            more_information='Some additional information',
            employee=self.employee
        )

        # Create test data for Leave_Application model
        self.leave_application = Leave_Application.objects.create(
            reason='Vacation',
            status='Pending',
            start_date=date(2024, 4, 10),
            number_of_days=5,
            end_date=date(2024, 4, 15),
            employee=self.employee,
            approved_by='Manager'
        )

    def test_employees_model(self):
        employee = Employees.objects.get(id=self.employee.id)
        self.assertEqual(employee.first_name, 'John')
        self.assertEqual(employee.last_name, 'Doe')
        self.assertEqual(employee.phone_number, '1234567')
        self.assertEqual(employee.email, 'john@example.com')
        self.assertEqual(employee.role, 'Developer')
        self.assertEqual(employee.age, 30)
        self.assertEqual(employee.date_of_birth, date(1994, 5, 12))
        self.assertEqual(employee.home_adress, '123 Main St')

    def test_next_of_kin_model(self):
        next_of_kin = Next_of_kin.objects.get(id=self.next_of_kin.id)
        self.assertEqual(next_of_kin.first_name, 'Jane')
        self.assertEqual(next_of_kin.last_name, 'Doe')
        self.assertEqual(next_of_kin.relationship, 'Spouse')
        self.assertEqual(next_of_kin.phone_number, '9876543')
        self.assertEqual(next_of_kin.email, 'jane@example.com')
        self.assertEqual(next_of_kin.employee, self.employee)

    def test_employee_skills_model(self):
        employee_skill = Employee_skills.objects.get(id=self.employee_skill.id)
        self.assertEqual(employee_skill.skill_title, 'Python')
        self.assertEqual(employee_skill.level_of_education, 'Bachelor')
        self.assertEqual(employee_skill.school_name, 'University of ABC')
        self.assertEqual(employee_skill.attain_year, date(2016, 5, 12))
        self.assertEqual(employee_skill.more_information, 'Some additional information')
        self.assertEqual(employee_skill.employee, self.employee)

    def test_leave_application_model(self):
        leave_application = Leave_Application.objects.get(id=self.leave_application.id)
        self.assertEqual(leave_application.reason, 'Vacation')
        self.assertEqual(leave_application.status, 'Pending')
        self.assertEqual(leave_application.start_date, date(2024, 4, 10))
        self.assertEqual(leave_application.number_of_days, 5)
        self.assertEqual(leave_application.end_date, date(2024, 4, 15))
        self.assertEqual(leave_application.employee, self.employee)
        self.assertEqual(leave_application.approved_by, 'Manager')
