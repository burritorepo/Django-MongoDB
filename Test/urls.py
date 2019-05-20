from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from Test.views import DriverViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'mongo', DriverViewSet)

urlpatterns = [

]
 
urlpatterns += merouter.urls