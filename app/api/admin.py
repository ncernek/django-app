from django.contrib import admin

from .models import Equation, Equation_Source, User, Subuser, User_Goal, User_Feedback, User_Score, Customer

sites = [Equation, Equation_Source, User, Subuser, User_Goal, User_Feedback, User_Score, Customer]

for x in sites:
	admin.site.register(x)