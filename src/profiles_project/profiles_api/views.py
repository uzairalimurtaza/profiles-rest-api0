from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.views import Response
from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test Api View."""

    serializer_class = serializers.HelloSerializers

    def get(self,request,format=None):
        """Return a list of Api View features."""

        an_apiview = [
            'user http methods as functions'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})


    def post(self,request):
        """create a hello message with our name"""

        # serializer = None

        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})

        else:
            return Response(serializer.errors)

    def put(self,request,pk=None):
        """Handles updating an Object"""

        return Response({'method':'put'})


    def patch(self,request,pk=None):
        """Patch request, only update fields provided in the request"""

        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """Delete an Object"""

        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.HelloSerializers

    def list(self, request):
        """Return a Hello Message."""

        a_viewset = [
        'user actions'
        ]

        return Response({'message':'Hello!','a_viewset': a_viewset})

    def create(self,request):
        """create a hello message with our name"""

            # serializer = None

        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})

        else:
            return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method':'update'})

    def partial_update(self,request,pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method':'PARTIAL_UPDATE'})

    def destroy(self,request,pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method':'DESTROY'})
