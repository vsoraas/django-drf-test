from rest_framework import routers, serializers, viewsets
from drf.models import HelloWorld

class HelloSerializer(serializers.HyperlinkedModelSerializer):
    print         = serializers.ReadOnlyField()
    from_api      = serializers.ReadOnlyField()
    creation_date = serializers.ReadOnlyField()

    class Meta:
        model = HelloWorld
        fields = ['extra', 'sender', 'print', 'from_api', 'creation_date']