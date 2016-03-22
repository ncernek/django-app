from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import TemplateView

from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^api/', include('api.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]

urlpatterns = format_suffix_patterns(urlpatterns)