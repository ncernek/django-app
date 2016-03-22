from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
	#customers
	url(r'^customers/$', views.CustomerList.as_view()),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
    #customer_clinical_info
    url(r'^customer_clinical_info/$', views.Customer_Clinical_InfoList.as_view()),
    url(r'^customer_clinical_info/(?P<pk>[0-9]+)/$', views.Customer_Clinical_InfoDetail.as_view()),
    #equations
    url(r'^equations/$', views.EquationList.as_view()),
    url(r'^equations/(?P<pk>[0-9]+)/$', views.EquationDetail.as_view()),
    #equation_source
    url(r'^equation_sources/$', views.Equation_SourceList.as_view()),
    url(r'^equation_sources/(?P<pk>[0-9]+)/$', views.Equation_SourceDetail.as_view()),
    #user
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    #subuser
    url(r'^subusers/$', views.SubuserList.as_view()),
    url(r'^subusers/(?P<pk>[0-9]+)/$', views.SubuserDetail.as_view()),
    #user_activity
    url(r'^user_activity/$', views.User_ActivityList.as_view()),
    url(r'^user_activity/(?P<pk>[0-9]+)/$', views.User_ActivityDetail.as_view()), 
    #user_goal
    url(r'^user_goals/$', views.User_GoalList.as_view()),
    url(r'^user_goals/(?P<pk>[0-9]+)/$', views.User_GoalDetail.as_view()),
    #user_feedback
    url(r'^user_feedback/$', views.User_FeedbackList.as_view()),
    url(r'^user_feedback/(?P<pk>[0-9]+)/$', views.User_FeedbackDetail.as_view()),
    #user_score
    url(r'^user_scores/$', views.User_ScoreList.as_view()),
    url(r'^user_scores/(?P<pk>[0-9]+)/$', views.User_ScoreDetail.as_view()),   
]

#urlpatterns = format_suffix_patterns(urlpatterns)