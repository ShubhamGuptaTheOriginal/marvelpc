from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^register$',views.register),
    url(r'^login$',views.login),
]