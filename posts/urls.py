from django.urls import path

from posts.views import JobView, JobSearchView

urlpatterns = [

    path('jobs/', JobView.as_view(), name="jobs_view"),
    path('jobs/search/', JobSearchView.as_view(), name="job_search"),

    ]
