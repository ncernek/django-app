from api.models import Customer, Customer_Clinical_Info, Equation, Equation_Source, User, Subuser, User_Activity, User_Goal, User_Feedback, User_Score
from api.serializers import CustomerSerializer, Customer_Clinical_InfoSerializer, EquationSerializer, Equation_SourceSerializer, UserSerializer, SubuserSerializer, User_ActivitySerializer, User_GoalSerializer, User_FeedbackSerializer, User_ScoreSerializer
from rest_framework import generics

#Customers:
class CustomerList(generics.ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

#Customer_Clinical_Info
class Customer_Clinical_InfoList(generics.ListCreateAPIView):
	queryset = Customer_Clinical_Info.objects.all()
	serializer_class = Customer_Clinical_InfoSerializer

class Customer_Clinical_InfoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Customer_Clinical_Info.objects.all()
	serializer_class = Customer_Clinical_InfoSerializer

#Equation:
class EquationList(generics.ListCreateAPIView):
	queryset = Equation.objects.all()
	serializer_class = EquationSerializer

class EquationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Equation.objects.all()
	serializer_class = EquationSerializer

#Equation_Source:
class Equation_SourceList(generics.ListCreateAPIView):
	queryset = Equation_Source.objects.all()
	serializer_class = Equation_SourceSerializer

class Equation_SourceDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Equation_Source.objects.all()
	serializer_class = Equation_SourceSerializer

#User:
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

#Subuser:
class SubuserList(generics.ListCreateAPIView):
	queryset = Subuser.objects.all()
	serializer_class = SubuserSerializer

class SubuserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Subuser.objects.all()
	serializer_class = SubuserSerializer

#User_Activity
class User_ActivityList(generics.ListCreateAPIView):
	queryset = User_Activity.objects.all()
	serializer_class = User_ActivitySerializer

class User_ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User_Activity.objects.all()
	serializer_class = User_ActivitySerializer
	
#User_Goal
class User_GoalList(generics.ListCreateAPIView):
	queryset = User_Goal.objects.all()
	serializer_class = User_GoalSerializer

class User_GoalDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User_Goal.objects.all()
	serializer_class = User_GoalSerializer

#User_Feedback
class User_FeedbackList(generics.ListCreateAPIView):
	queryset = User_Feedback.objects.all()
	serializer_class = User_FeedbackSerializer

class User_FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User_Feedback.objects.all()
	serializer_class = User_FeedbackSerializer

#User_Score
class User_ScoreList(generics.ListCreateAPIView):
	queryset = User_Score.objects.all()
	serializer_class = User_ScoreSerializer

class User_ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User_Score.objects.all()
	serializer_class = User_ScoreSerializer