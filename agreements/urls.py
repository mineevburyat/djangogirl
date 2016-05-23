from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^/$', views.agreement_list, name='agreement_list'),

]