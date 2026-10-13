from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from spending.serializers import UserSerializers,ExpenseSerializer
from spending.models import Expense

from django.contrib.auth.models import User

from spending.permission import IsOwner




class SignUpViews(APIView):
    def post(self,request):
        form_data = request.data
        serializer_instance = UserSerializers(data=form_data)

        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data
            instance = User.objects.create_user(**cleaned_data)

            serializer_instance = UserSerializers(instance)
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)


class GetMeView(APIView):
    
    # authentication_classes = [authentication.BasicAuthentication]
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        auth_user = request.user   # gets the user who sends the request

        instance = User.objects.get(username = auth_user)

        serializer_instance = UserSerializers(instance)

        return Response(data=serializer_instance.data)


class ExpenseListCreateView(APIView):
    # authentication_classes = [authentication.BasicAuthentication]
    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        instance = Expense.objects.filter(owner = request.user)
        serializer_instance = ExpenseSerializer(instance,many=True)
        return Response(data=serializer_instance.data)


    def post(self,request):
        form_data = request.data
        serializer_instance = ExpenseSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save(owner=request.user)
            # cleaned_data = serializer_instance.validated_data
            # instance = Expense.objects.create(**cleaned_data,owner = request.user)

            # serializer_instance = ExpenseSerializer(instance)
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)


class ExpenseRetriveUpdateDeleteView(APIView):
    # authentication_classes = [authentication.BasicAuthentication]
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwner]

    def get(self,request,pk):
        instance = Expense.objects.get(id=pk)  # also can use "get_object_or_404" 

        self.check_object_permissions(request,instance)    #To check if the user have permission

        serializer_instance = ExpenseSerializer(instance)
        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):
        
        instance = get_object_or_404(Expense,id=pk) # helps to run without error
        form_data = request.data

        self.check_object_permissions(request,instance)    #To check if the user have permission
                
        serializer_instance = ExpenseSerializer(data=form_data,instance=instance)  # instance given so that program understands its instance is updated
        
        if serializer_instance.is_valid():
            serializer_instance.save()
            # cleaned_data = serializer_instance.validated_data
            # Expense.objects.filter(id=pk).update(**cleaned_data)
            # serializer_instance = ExpenseSerializer(instance,many=True)
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)


    def delete(self,request,pk=None):
        instance = get_object_or_404(Expense,id=pk)
        instance.delete()
        return Response(data={"Message":"Deleted"})


