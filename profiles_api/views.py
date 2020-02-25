from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test APIView """

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put, delete)',
            'is similar to a traditional django view',
            'gives you the method control over your applicatio logic',
            'is mapped manualy to URLs',

        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
