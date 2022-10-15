from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.serializers import JobAdvertSerializer


class JobView(APIView):
    def post(self, request):

        user = request.user
        serializer = JobAdvertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_employer(user.id)
        serializer.save()

        return Response(serializer.data)