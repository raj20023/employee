from rest_framework import serializers
from .models import Employee
from .models import Company

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    company = EmployeeSerializer(many=True)

    class Meta:
        model = Company
        fields = ('company_id','company_name','company')    