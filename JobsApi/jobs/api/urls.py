from django.urls import path
from jobs.api.views import JobsCreateAPIView, JobsDetailAPIView

urlpatterns  = [
    #path("articles/", article_create_list_api_view, name="articles-list"),
    #path("articles/<int:pk>/", article_detail_api_view, name="article-detail")

    path("jobs/", JobsCreateAPIView.as_view(), name="jobs-list"),
    path("jobs/<int:pk>/", JobsDetailAPIView.as_view(), name="job-detail")
]