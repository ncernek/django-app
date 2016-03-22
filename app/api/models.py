from django.db import models
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=2048)
    department_name = models.CharField(max_length=2048, null=True)
    address = models.CharField(max_length=2048, null=True)
    city = models.CharField(max_length=2048, null=True)
    state = models.CharField(max_length=2048, null=True)
    zipcode = models.IntegerField(null=True)
    admin = models.CharField(max_length=2048)
    created = models.DateTimeField(default=datetime.now, blank=True)
    last_update = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

#To be updated according to pilot data & use cases:
class Customer_Clinical_Info(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)	
    def __str__(self):
        return self.customer

class Equation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_active = models.IntegerField(default=0)
    is_master = models.IntegerField(default=0)
    is_starred = models.IntegerField(default=0)
    param_count = models.IntegerField(default=0)
    default_priority = models.IntegerField(default=0)
    equation = models.CharField(max_length=2048)
    get_param_sql = models.CharField(max_length=2048, null=True, blank=True)
    get_param = models.CharField(max_length=2048, null=True, blank=True)
    recommendation = models.CharField(max_length=2048, null=True, blank=True)
    updated_by = models.CharField(max_length=2048, null=True, blank=True)
    created_by = models.CharField(max_length=2048, null=True, blank=True)
    short_text = models.CharField(max_length=2048, null=True, blank=True)
    med_text = models.CharField(max_length=2048, null=True, blank=True)
    large_text = models.CharField(max_length=2048, null=True, blank=True)
    created = models.DateTimeField(default=datetime.now, blank=True)
    last_update = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.large_text

class Equation_Source(models.Model):
    customer = models.ForeignKey(Equation, on_delete=models.CASCADE)
    is_active = models.IntegerField(default=0, blank=True, null=True)
    source_type = models.CharField(max_length=2048, blank=True, null=True)
    link = models.CharField(max_length=2048, blank=True, null=True)
    directive = models.CharField(max_length=2048, blank=True, null=True)
    def __str__(self):
        return self.source_type

class User(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)	
    email = models.CharField(max_length=2048)
    password = models.CharField(max_length=2048)
    first_name = models.CharField(max_length=2048)
    middle_name = models.CharField(max_length=2048, null=True, blank=True)
    last_name = models.CharField(max_length=2048)
    title = models.CharField(max_length=2048, null=True, blank=True)
    suffix = models.CharField(max_length=2048, null=True, blank=True)
    display_name = models.CharField(max_length=2048)
    user_type = models.CharField(max_length=2048, null=True, blank=True)
    update_user = models.IntegerField(blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    is_admin = models.IntegerField(default=0)
    last_login = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(default=datetime.now, blank=True, null=True)
    last_password_update = models.DateTimeField(default=datetime.now, blank=True, null=True)
#    highlighted = models.TextField()
    def __str__(self):
        return self.display_name  

class Subuser(models.Model):
    parent_user_id = models.ForeignKey(User, on_delete=models.CASCADE)	
 # Django doesn't like this (having two foreign keys that are the same)
 #   child_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)	
    relationship = models.CharField(max_length=2048, null=True, blank=True)
    def __str__(self):
        return self.parent_user_id

#To be defined when tools are implemented to track user activity:
class User_Activity(models.Model):
    parent_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.customer

class User_Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)	
    equation = models.ForeignKey(Equation, on_delete=models.CASCADE)
    target = models.FloatField(default=0)
    description = models.CharField(max_length=2048, null=True, blank=True)
    user_priority = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(default=datetime.now, blank=True, null=True) 
    last_update = models.DateTimeField(default=datetime.now, blank=True, null=True)
    def __str__(self):
        return self.description

class User_Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)	
    equation = models.ForeignKey(Equation, on_delete=models.CASCADE)
    feedback_type = models.IntegerField(blank=True, null=True)
    sub_type = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=2048, blank=True, null=True)
    copied = models.CharField(max_length=2048, blank=True, null=True)
    created = models.DateTimeField(default=datetime.now, blank=True, null=True)
    def __str__(self):
        return self.comment

class User_Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)	
    equation = models.ForeignKey(Equation, on_delete=models.CASCADE)
    value = models.FloatField(default=0)
    created = models.DateTimeField(default=datetime.now, blank=True, null=True) 
    last_update = models.DateTimeField(default=datetime.now, blank=True, null=True)
    def __str__(self):
        return self.value

