"""safe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from map.models import BufferArea, DangerousArea, Location, User, Message


class BufferAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BufferArea
        fields = ('latitude', 'longitude', 'radius', 'info')


class DangerousAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DangerousArea
        fields = ('latitude', 'longitude', 'radius', 'info')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('user', 'time', 'latitude', 'longitude')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'password')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('sender', 'content', 'time')


class BufferAreaViewSet(viewsets.ModelViewSet):
    queryset = BufferArea.objects.all()
    serializer_class = BufferAreaSerializer


class DangerousAreaViewSet(viewsets.ModelViewSet):
    queryset = DangerousArea.objects.all()
    serializer_class = DangerousAreaSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


router = routers.DefaultRouter()
router.register(r'bufferarea', BufferAreaViewSet)
router.register(r'dangerousarea', DangerousAreaViewSet)
router.register(r'location', LocationViewSet)
router.register(r'user', UserViewSet)
router.register(r'message', MessageViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
