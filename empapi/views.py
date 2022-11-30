from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, Company
from .serializers import EmployeeSerializer, CompanySerializer

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Emp List':'/employee-list/',
		'Emp Detail View':'/employee-detail/<str:pk>/',
		'Emp Create':'/emp-create/',
		'Emp Update':'/emp-update/<str:pk>/',
		'Emp Delete':'/emp-delete/<str:pk>/',
        'Cmp List':'/cmp-list/',
		'Cmp Detail View':'/cmp-detail/<str:pk>/',
		'Cmp Create':'/cmp-create/',
		'Cmp Update':'/cmp-update/<str:pk>/',
		'Cmp Delete':'/cmp-delete/<str:pk>/',
		}

	return Response(api_urls)
    
#views for employee table
@api_view(['GET'])
def employeelist(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def employeedetail(request,pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def employeecreate(request):
	serializer = EmployeeSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def employeeupdate(request, pk):
	employee = Employee.objects.get(id=pk)
	serializer = EmployeeSerializer(instance=employee, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def employeedelete(request, pk):
	task = Employee.objects.get(id=pk)
	task.delete()

	return Response('Employee details succsesfully delete!')







# views for company table

@api_view(['GET'])
def companylist(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def companydetail(request,pk):
    company = Company.objects.get(company_id=pk)
    serializer = CompanySerializer(company,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def companycreate(request):
	serializer = CompanySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def companyupdate(request, pk):
	company = Company.objects.get(company_id=pk)
	serializer = CompanySerializer(instance=company, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def companydelete(request, pk):
	task = Company.objects.get(company_id=pk)
	task.delete()

	return Response('Company details succsesfully delete!')