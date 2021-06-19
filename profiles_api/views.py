from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class HelloAPIView(APIView):
    """Test API View"""


    def get(self, request, format=None):
        """Returns a list of APIVIew features"""
        an_apiview = [
            'Uses HTTp methods as functions (get, post, patch, put , delete)'
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})


