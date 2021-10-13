from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from employee.models import Employee, Department
from employee.serializers import EmployeeSerializer, DepartmentSerializer

# Create your views here.
@csrf_exempt
def department_list(request):
    if request.method == 'GET':
        department = Department.objects.all()
        serializer = DepartmentSerializer( department, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Added Sucessfully', safe = False)
        return JsonResponse('Failed to Add Data', safe = False) 

    elif request.method == 'DELETE':
        department=Department.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse('Deleted Sucessfully', safe = False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)  
        department = Department.objects.get(DepartmentId = department_data['DepartmentId'])  
        serializer = DepartmentSerializer(department, data=department_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Updated Sucessfully', safe = False)
        return JsonResponse('Failed to Update Data', safe = False)

@csrf_exempt
def employee_list(request):
    if request.method == 'GET':
        employees = Department.objects.all()
        serializer = DepartmentSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        employees = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=employees)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Added Sucessfully', safe = False)
        return JsonResponse('Failed to Add Data', safe = False) 

    elif request.method == 'DELETE':
        employee=Department.objects.get(EmployeeId = id)
        employee.delete()
        return JsonResponse('Deleted Sucessfully', safe = False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)  
        employee = Department.objects.get(DepartmentId = employee_data['EmployeeId'])  
        serializer = DepartmentSerializer(employee, data=employee_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Updated Sucessfully', safe = False)
        return JsonResponse('Failed to Update Data', safe = False)


def department_detail(request):
    pass
