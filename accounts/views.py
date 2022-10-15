from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        a={'first_name': serializer.data['first_name'], 'email': serializer.data['email']}
        b = serializer.data
        return Response(a)