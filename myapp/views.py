from django.http import HttpResponse
from django.views import View
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.serializers import *


class sample(View):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        return HttpResponse("sample text")

class Welcome(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response('dd')


class Register(ListCreateAPIView):
    # serializer_class = RegisterSerializer
    queryset = MyUser.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return RegisterSerializer
        return RegisterSerializer

class Login(APIView):
    def post(self,request,*args,**kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)









