from rest_framework import serializers
from .models import Customer, Customer_Clinical_Info, Equation, Equation_Source, User, Subuser, User_Activity, User_Goal, User_Feedback, User_Score

class CustomerSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Customer
		fields = ('name', 'department_name', 'address', 'city',
				  'state', 'zipcode', 'admin', 'created',
				  'last_update')

class Customer_Clinical_InfoSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Customer_Clinical_Info
		fields = ('')

class EquationSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Equation
		fields = ('customer', 'is_active', 'is_master', 'is_starred',
				  'param_count', 'default_priority', 'equation', 'get_param_sql',
				  'get_param', 'recommendation', 'updated_by', 'created_by',
				  'short_text', 'med_text', 'large_text', 'created',
				  'last_update')

class Equation_SourceSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Equation_Source
		fields = ('customer', 'is_active', 'source_type', 'link',
				  'directive')

class UserSerializer(serializers.ModelSerializer):	
	class Meta:
		model = User
		fields = ('customer', 'email', 'first_name', 'middle_name', 
				  'last_name', 'title', 'suffix', 'display_name',
				  'user_type', 'is_admin', 'last_login', 'last_update',
				  'last_password_update')

class SubuserSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Subuser
		fields = ('parent_user_id',)

class User_ActivitySerializer(serializers.ModelSerializer):	
	class Meta:
		model = User_Activity
		fields = ('')

class User_GoalSerializer(serializers.ModelSerializer):	
	class Meta:
		model = User_Goal
		fields = ('user', 'equation', 'target', 'description',
				  'user_priority', 'created', 'last_update')

class User_FeedbackSerializer(serializers.ModelSerializer):	
	class Meta:
		model = User_Feedback
		fields = ('user', 'equation', 'feedback_type', 'sub_type',
				  'comment', 'copied', 'created')

class User_ScoreSerializer(serializers.ModelSerializer):	
	class Meta:
		model = User_Score
		fields = ('user', 'equation', 'value', 'created',
				  'last_update')