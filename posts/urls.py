from django.urls import path

from posts.views import JobView

urlpatterns = [

    path('jobs/', JobView.as_view(), name="profile_view"),
    ]
