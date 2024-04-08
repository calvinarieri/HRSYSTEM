from django.test import TestCase, Client
from rest_framework import status
from hrapp.models import Employees, Employee_skills, Next_of_kin, Leave_Application
from hrapp.serializer import All_Employees
import json


class EmployeesViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.employee_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'email': 'john@example.com',
            'password': 'password',
            'date': '2022-04-08',
            'role': 'Developer',
            'age': 30,
            'date_of_birth': '1992-04-08',
            'home_adress': '123 Main St'
        }
        # self.employee = Employees.objects.create(**self.employee_data)
        self.employee = All_Employees(data=json.dumps(self.employee_data))
        if self.employee.is_valid():
            self.employee.save()

    def test_employees_list(self):
        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_employee(self):
        response = self.client.post('/employees/', data=self.employee_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employees.objects.count(), 2)

    def test_get_employee_detail(self):
        response = self.client.get(f'/employee/{self.employee.data.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.employee_data['first_name'])

    def test_update_employee(self):
        updated_data = {
            'first_name': 'Updated Name',
            'age': 35
        }
        response = self.client.put(f'/employee/{self.employee.data.id}/', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.data.refresh_from_db()
        self.assertEqual(self.employee.data.first_name, 'Updated Name')
        self.assertEqual(self.employee.data.age, 35)

    def test_delete_employee(self):
        response = self.client.delete(f'/employee/{self.employee.data.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employees.objects.count(), 0)

# class EmployeeSkillsViewsTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.employee = Employees.objects.create(
#             first_name='John',
#             last_name='Doe',
#             phone_number='1234567890',
#             email='john@example.com',
#             password='password',
#             date='2022-04-08',
#             role='Developer',
#             age=30,
#             date_of_birth='1992-04-08',
#             home_adress='123 Main St'
#         )
#         self.skill_data = {
#             'skill_title': 'Python',
#             'level_of_education': 'Bachelor',
#             'school_name': 'University of ABC',
#             'attain_year': '2016-05-12',
#             'more_information': 'Some additional information',
#             'employee': self.employee.id
#         }
#         self.skill = Employee_skills.objects.create(**self.skill_data)

#     def test_skills_list(self):
#         response = self.client.get('/employee_skills/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_create_skill(self):
#         response = self.client.post('/employee_skills/', data=self.skill_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Employee_skills.objects.count(), 2)

#     def test_get_skill_detail(self):
#         response = self.client.get(f'/employee_skills/{self.skill.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['skill_title'], self.skill_data['skill_title'])

#     def test_update_skill(self):
#         updated_data = {
#             'skill_title': 'Updated Skill',
#             'level_of_education': 'Master'
#         }
#         response = self.client.put(f'/employee_skills/{self.skill.id}/', data=json.dumps(updated_data), content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.skill.refresh_from_db()
#         self.assertEqual(self.skill.skill_title, 'Updated Skill')
#         self.assertEqual(self.skill.level_of_education, 'Master')

#     def test_delete_skill(self):
#         response = self.client.delete(f'/employee_skills/{self.skill.id}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Employee_skills.objects.count(), 0)


# class NextOfKinViewsTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.employee = Employees.objects.create(
#             first_name='John',
#             last_name='Doe',
#             phone_number='1234567890',
#             email='john@example.com',
#             password='password',
#             date='2022-04-08',
#             role='Developer',
#             age=30,
#             date_of_birth='1992-04-08',
#             home_adress='123 Main St'
#         )
#         self.next_of_kin_data = {
#             'first_name': 'Jane',
#             'last_name': 'Doe',
#             'relationship': 'Spouse',
#             'phone_number': '0987654321',
#             'email': 'jane@example.com',
#             'employee': self.employee.id
#         }
#         self.next_of_kin = Next_of_kin.objects.create(**self.next_of_kin_data)

#     def test_next_of_kin_list(self):
#         response = self.client.get('/next_of_kin/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_create_next_of_kin(self):
#         response = self.client.post('/next_of_kin/', data=self.next_of_kin_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Next_of_kin.objects.count(), 2)

#     def test_get_next_of_kin_detail(self):
#         response = self.client.get(f'/next_of_kin/{self.next_of_kin.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['first_name'], self.next_of_kin_data['first_name'])

#     def test_update_next_of_kin(self):
#         updated_data = {
#             'first_name': 'Updated Name',
#             'relationship': 'Sibling'
#         }
#         response = self.client.put(f'/next_of_kin/{self.next_of_kin.id}/', data=json.dumps(updated_data), content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.next_of_kin.refresh_from_db()
#         self.assertEqual(self.next_of_kin.first_name, 'Updated Name')
#         self.assertEqual(self.next_of_kin.relationship, 'Sibling')

#     def test_delete_next_of_kin(self):
#         response = self.client.delete(f'/next_of_kin/{self.next_of_kin.id}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Next_of_kin.objects.count(), 0)

# class LeaveApplicationViewsTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.employee = Employees.objects.create(
#             first_name='John',
#             last_name='Doe',
#             phone_number='1234567890',
#             email='john@example.com',
#             password='password',
#             date='2022-04-08',
#             role='Developer',
#             age=30,
#             date_of_birth='1992-04-08',
#             home_adress='123 Main St'
#         )
#         self.leave_application_data = {
#             'reason': 'Vacation',
#             'status': 'Pending',
#             'date': '2024-04-10',
#             'start_date': '2024-04-12',
#             'number_of_days': 5,
#             'end_date': '2024-04-16',
#             'employee': self.employee.id,
#             'approved_by': 'Manager'
#         }
#         self.leave_application = Leave_Application.objects.create(**self.leave_application_data)

#     def test_leave_application_list(self):
#         response = self.client.get('/leave_application/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_create_leave_application(self):
#         response = self.client.post('/leave_application/', data=self.leave_application_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Leave_Application.objects.count(), 2)

#     def test_get_leave_application_detail(self):
#         response = self.client.get(f'/leave_application/{self.leave_application.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['reason'], self.leave_application_data['reason'])

#     def test_update_leave_application(self):
#         updated_data = {
#             'reason': 'Updated Reason',
#             'status': 'Approved'
#         }
#         response = self.client.put(f'/leave_application/{self.leave_application.id}/', data=json.dumps(updated_data), content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.leave_application.refresh_from_db()
#         self.assertEqual(self.leave_application.reason, 'Updated Reason')
#         self.assertEqual(self.leave_application.status, 'Approved')

#     def test_delete_leave_application(self):
#         response = self.client.delete(f'/leave_application/{self.leave_application.id}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Leave_Application.objects.count(), 0)


