from django.urls import path, include
from alpine.regionconfig import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =[
	path('v1/kvstore/<key>', views.kvstore),
	path('v1/kvstore/<key>/<value>', views.kvstore),
]
urlpatterns = format_suffix_patterns(urlpatterns)