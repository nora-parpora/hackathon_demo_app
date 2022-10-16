from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from django.http import HttpResponse, Http404
from rest_framework import permissions, status

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Employer, HouseOwner
from posts.models import JobAdvert
from posts.serializers import JobAdvertSerializer, RentAdvertSerializer
from posts.utils import CustomPagination


class JobsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if not user or isinstance(user, AnonymousUser) :
            return HttpResponse(status=401)

        try:
            e = Employer.objects.get(pk=user.id)
        except Exception as ex:
            return HttpResponse(status=403, content=ex.args)

        serializer = JobAdvertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.set_employer(e)
        serializer.save()

        return Response(serializer.data)


class JobSearchView(ListAPIView):
    serializer_class = JobAdvertSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        sector = self.request.GET.get('sector')
        city = self.request.GET.get('city')
        empl_type = self.request.GET.get('empl_type')

        qs = None
        if keyword:
            if qs:
                qs &= Q(description__icontains=keyword.lower())
            else:
                qs = Q(description__icontains=keyword.lower())
        if sector:
            if qs:
                qs &= Q(sector__name=sector.lower())
            else:
                qs = Q(sector__name=sector.lower())
        if city:
            if qs:
                qs &= Q(city__icontains=city.lower())
            else:
                qs = Q(city__icontains=city.lower())
        if empl_type:
            if qs:
                qs &= Q(empl_type__icontains=empl_type.lower())
            else:
                qs = Q(empl_type__icontains=empl_type.lower())
        if qs:
            return JobAdvert.objects.filter(qs).order_by("-pk")

        return JobAdvert.objects.all().order_by("-pk")


class JobView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JobAdvertSerializer
    queryset = JobAdvert.objects.all()


class RentsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if not user or isinstance(user, AnonymousUser) :
            return HttpResponse(status=401)

        try:
            o = HouseOwner.objects.get(pk=user.id)
        except Exception as ex:
            return HttpResponse(status=403, content=ex.args)

        serializer = RentAdvertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.set_owner(o)
        serializer.save()

        return Response(serializer.data)
