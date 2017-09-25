from django.conf.urls import url
from api.views import *
urlpatterns = [
    url(r'v1/getsite/', get_site),
]