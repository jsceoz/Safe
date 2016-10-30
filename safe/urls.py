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
        fields = ()


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





urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
