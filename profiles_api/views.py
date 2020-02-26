from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloViewSet(viewsets.ViewSet):
    """Test Api View Set """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses actions (list, create, retrieve, update , partial_update)',
            'Automatically maps to URLs using Router',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrivee(self, request, pk=None):
        """ handle getting an object by its id """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ handle updating an object """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ handle updating part of object """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ handle removing an object by its id """
        return Response({'http_method': 'DELETE'})


class HelloApiView(APIView):
    """ Test APIView """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put, delete)',
            'is similar to a traditional django view',
            'gives you the method control over your applicatio logic',
            'is mapped manualy to URLs',

        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ create a hello message with our name """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handle updating an objects """
        return Response({'method': 'PUT'})

    def patch(self, request):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object"""
        return Response({'method': 'DELETE'})
