from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from django.http import HttpResponse

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Employer
from posts.models import JobAdvert
from posts.serializers import JobAdvertSerializer
from posts.utils import CustomPagination


class JobView(APIView):
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

        serializer.set_employer(user.id)
        serializer.save()


        return Response(serializer.data)

# from rest_framework import permissions
#
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of an object to edit it.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         # Write permissions are only allowed to the owner of the snippet.
#         return obj.owner == request.user
#
# Now we can add that custom permission to our snippet instance endpoint,
# by editing the permission_classes property on the SnippetDetail view class:
#
# permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly]


class JobSearchView(ListAPIView):
    serializer_class = JobAdvertSerializer
    pagination_class = CustomPagination

    #metadata_class = JobAdvert

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
            return JobAdvert.objects.filter(qs)
        # ToDo to implement search for the city as well
        return JobAdvert.objects.all()

