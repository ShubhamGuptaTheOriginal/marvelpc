from django.conf.urls import url,include
from products import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
]