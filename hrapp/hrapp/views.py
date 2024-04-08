from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from .models import Employee_skills,Leave_Application,Employees,Next_of_kin
from .serializer import All_Employees,UserSkills,Next_Of_Kin, Leave_applications

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError



@api_view(['POST'])
def login(request):
    user = get_object_or_404(Employees, email=request.data['email'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = All_Employees(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def employees_list(request):
    if request.method == 'GET':
        #GET ALL DATA
        #SERIALIZE
        #RETURN JSON
        employees = Employees.objects.all()
        serializer = All_Employees(employees , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    


    if request.method == 'POST':
        serializer = All_Employees(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = Employees.objects.get(email=request.data['email'])
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Handle invalid serializer
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def employee_detail(request, id):

    # CHECK EXISTANCE OF EMPLOYEE
    try:
       employee = Employees.objects.get(pk=id)
    except Employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = All_Employees(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        serializer  = All_Employees(employee)
        return Response(serializer.data , status=status.HTTP_302_FOUND)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def next_of_kin(request, id):
    if request.method == 'GET':
        try:
            nextOfKin = Next_of_kin.objects.filter(employee= id).all()
            serializer = Next_Of_Kin(nextOfKin, many=True)
            return Response(serializer.data, status=status.HTTP_302_FOUND)        
        except Next_of_kin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
    elif request.method == 'POST':
        try:
            user = Employees.objects.get(pk = id)
            userSerializer = All_Employees(user)
            received_data = request.data
            serializer = Next_of_kin(
                first_name = received_data.get('first_name'),
                last_name = received_data.get('last_name'),
                relationship = received_data.get('relationship'),
                phone_number = received_data.get('phone_number'),
                email = received_data.get('email'),
                employee= user
            )
            print(serializer)
            if userSerializer.data.get('id') == id :
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)  
            return Response(status=status.HTTP_403_FORBIDDEN)        
                     
        except Employees.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        
@api_view(['GET','POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def employee_skills(request, id):
    if request.method == 'GET':
        try:
            skills = Employee_skills.objects.filter(employee = id).all()
            serielizer = UserSkills(skills, many=True)
            return  Response(serielizer.data,status=status.HTTP_200_OK)
        except Employee_skills.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        try:
            employee = Employees.objects.get(pk=id)
            new_skill = Employee_skills(
                skill_title = request.data.get('skill_title'),
                level_of_education = request.data.get('education'),
                school_name = request.data.get('school'),
                attain_year = request.data.get('end_date'),
                more_information = request.data('more_description'),
                employee = employee
            )
            new_skill.save()
            return Response({'message': 'added successfully'}, status = status.HTTP_201_CREATED)
        except Employees.DoesNotExist:
            return Response({'message':'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT','DELETE', 'GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def skill_update_delete(request, id):
    try:
        skill = Employee_skills.objects.get(pk=id)
    except Employee_skills.DoesNotExist:
        return Response({'message':'Skill not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSkills(skill)
        return Response(serializer, status=status.HTTP_302_FOUND)
    elif request.method == 'PUT':
        serializer = UserSkills(skill, data=request.data)
        return Response(serializer, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        skill.delete()
        return Response({'message':'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def employee_leaves(request, id):
    if request.method == 'GET':
        try:
            leaves = Leave_Application.objects.filter(employee = id).all()
            serializer = Leave_applications(leaves, many=True)
            return Response(serializer, status=status.HTTP_200_OK)
        
        except Leave_Application.DoesNotExist:
            return Response({'message':'No leaves found'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        employee = Employees.objects.get(pk=id)
        new_leave = Leave_Application(
            reason = request.data.get('reason'),
            status='pending',
            start_date = request.data.get('date'),
            number_of_days = request.data.get('days'),
            end_date = request.data.get('end_date'),
            employee = employee,
            approved_by = 'Waiting'           
        )
        new_leave.save()
        return Response({'message':'Applied for leave successfully. Wait for approval'}, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def leave_approval_rejection(request,id):
    try:
        leave = Leave_Application.objects.get(pk=id)
    except Leave_Application.DoesNotExist:
        return Response({'message':'leave not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Leave_applications(leave)
        return Response(serializer, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        new_change = Leave_applications(leave, data=request.data)
        if new_change.is_valid():
            new_change.save()

    
            