from typing import Any
from django import http
from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import User
import json
# Create your views here.
class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            users = list(User.objects.filter(id=id).values())
            if len(users)>0:
                user = users[0]
                data = {"message":"Success" , "user":user}
                #print(data)
            else:
                data = {"message":"User not found..."} 
            return JsonResponse(data)
        else:
            users = list(User.objects.values())

            if len(users)>0:
                data = {"message" : "success" , "users" : users}
            else:
                data = {"message":"Users not found..."}
            return JsonResponse(data)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        User.objects.create(name=jd['name'], lastname=jd['lastname'] , email=jd['email'])
        data = {"message":"Success"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        users = list(User.objects.filter(id=id).values())
        if len(users)>0:
            user = User.objects.get(id=id)
            user.name=jd['name']
            user.lastname=jd['lastname']
            user.email=jd['email']
            user.save()
            data = {"message":"Success"}
        else:
            data = {"message":"User not found..."}
        return JsonResponse(data)

    def delete(self, request , id):
        users = list(User.objects.filter(id=id).values())
        if len(users)>0:
            User.objects.filter(id=id).delete()
            data = {"message":"Success"}
        else:
            data = {"message":"User not found..."}
        return JsonResponse(data)