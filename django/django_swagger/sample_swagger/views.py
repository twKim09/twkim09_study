from django.http import JsonResponse
from django.shortcuts import render
from .mysql import mysql_query, mysql_query2
import json
from .kafka_producer_test import kafka_producer
from .kafka_consumer_test import kafka_consumer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def mysql(request):
    body = mysql_query()
    return JsonResponse(body,safe=False)
@csrf_exempt
def producer(request):
    value = request.body.decode('utf-8')
    value = json.loads(value)
    msg = value['kafka-prod']
    res = kafka_producer(msg)

    return JsonResponse(res,safe=False)

def consumer(request):
    res = kafka_consumer()
    
    return JsonResponse(res,safe = False)

@csrf_exempt
def dbinput(request):
    value=request.body.decode('utf-8')
    value = json.loads(value)
    name = value["name"]
    password = value["password"]
    
    res = mysql_query2(name,password)


    status = json.dumps({"status":200})
    return JsonResponse(status,safe=False)