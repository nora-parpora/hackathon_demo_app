from http.client import HTTPResponse

from rest_framework.views import APIView
from .serializers import ProfileSerializer
from rest_framework.response import Response


class RegisterView(APIView):

    def post(self, request):
        user = {'email': request.data['email'], 'password': request.data['password']}
        serializer = ProfileSerializer(data={'user':user, 'first_name':request.data['first_name'], 'last_name':request.data['last_name'], 'phone':request.data['phone']})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return_value = serializer.data['first_name'], serializer.data['last_name']
        # return Response(serializer.data)
        return Response(return_value)