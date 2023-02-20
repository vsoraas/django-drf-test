from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, serializers
from drf.models import HelloWorld
from drf.views import HelloViewSet


### DRF ###

router = routers.DefaultRouter()
router.register(r'helloworld', HelloViewSet)

### DRF ###


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]