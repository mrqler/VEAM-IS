from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^helloVEAM$', views.helloVEAM, name='helloVEAM'),
    url(r'^helpVeam$', views.helpVeam, name='helpVeam'),
]
