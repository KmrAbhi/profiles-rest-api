from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import permissions

from profiles_api import models
from profiles_api import serializers

# Create your views here.


class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer



    def get(self, request, format=None):
        """Returns a list of APIVIew features"""
        an_apiview = [
            'Uses HTTp methods as functions (get, post, patch, put , delete)'
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello message with your name"""
        serializer = self.serializer_class(data=request.data)
        

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )


    def put(self, request, pk=None):
        """Handle updating an object"""
        #pk stands for primary key
        serialzer = self.serializer_class(data=request.data)
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        serializer = self.serializer_class(data=request.data)
        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):
        """Handle delete of an object"""
        serializer = self.serializer_class(data=request.data)
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API View Set"""
    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """Return a hello message"""


        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code',

        ]

        return Response({'message':'Hello', 'a_viewset':a_viewset})


    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message':message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        """handle getting an object by it's Id"""
        return Response({'HTTTP_Method':'Get'})


    def update(self, request, pk=None):
        """handle updating an object by its Id"""
        return Response({'HTTP_Method':'Put'})


    def partial_update(self, request, pk=None):
        """Handle partially updating an object"""
        return Response({'HTTP_Method':'Patch'})


    def destroy(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'HTTP_Method':'Delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
     








        



    




