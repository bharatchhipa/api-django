from functools import partial
from apipost.models import student
import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .serializers import studentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.


@csrf_exempt
def add(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            emp = student.objects.get(id=id)
            serializer = studentSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        emp = student.objects.all()
        serializer = studentSerializer(emp, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = studentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data inserted Succesfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        emp = student.objects.get(id=id)
        serializer = studentSerializer(emp, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        emp = student.objects.get(id=id)
        emp.delete()
        res = {'msg': 'data Updated'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
