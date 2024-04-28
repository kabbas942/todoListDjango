from django.shortcuts import render,HttpResponse
from list.models import todoList
from RestApi.serializer import listSerialize
from rest_framework.renderers import JSONRenderer
# Create your views here.

def allRecord(request):
    allList = todoList.objects.all()
    serializer = listSerialize(allList,many=True)
    jsonre= JSONRenderer().render(serializer.data)
    return HttpResponse(jsonre,content_type='application/json')




