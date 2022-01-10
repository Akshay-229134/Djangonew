from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee,Student
from rest_framework.views import APIView

# Create your views here.
# JsonResponse for serialization
def employeeView(request):
    emp={
        'id':1,
        'name':'John',
        'sal':1000000
    }

    data =Employee.objects.all()
    response={'employees':list(data.values('name','sal'))}

    return  JsonResponse(response)


def studentView(request):
    student=Student.objects.all()
    print("new api")
    # print(student.name)
    response={'student':list(student.values('name'))}

    return  JsonResponse(response)
    