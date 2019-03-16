from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView)
from rest_framework.views import APIView
from rest_framework.decorators import action
from mysite.models import Person
from django.contrib.auth.models import User

from mysite.serializers import UserSerializer
from mysite.serializers import (
    PersonSerializer,
    ResgisterSerializer,
    FileSerializer
)
from rest_framework.response import Response
from rest_framework import status
import logging
import traceback
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authtoken.models import Token


logger = logging.getLogger(__name__)


class EmployeeSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PersonList(ListAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonSet(RetrieveAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonAdd(CreateAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class Test(RetrieveAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # lookup_field = 'fname'


class SnippedViewSet(viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('first_name').first()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class RegisterUser(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = ResgisterSerializer



class RegisterUser(APIView):

    @action(methods=['post'], detail=False)
    def post(self, request, *args, **kwargs):
        print('tesing ...')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_user(username, user_email, password)

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        #Generate Token
        token = Token.objects.create(user=user)
        return Response({'User Registed', 'token'})
