from django.urls import path

from posts.views import JobsView, JobSearchView, JobView

urlpatterns = [
    path('jobs/', JobsView.as_view(), name="jobs_view"),
    path('jobs/search/', JobSearchView.as_view(), name="job_search"),
    path('jobs/<int:pk>/', JobView.as_view(), name="job"),

    ]
