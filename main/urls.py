from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("job-adverts/", views.JobPosting.as_view(), name="job-posting"),
    path("job-adverts/published/", views.published_adverts, name="published-posting"),
    path("job-adverts/<int:advert_id>/unpublish-advert/", views.unpublish_advert, name="unpublish-posting"),
    path("job-adverts/<int:advert_id>/republish-advert/", views.republish_advert, name="republish-posting"),
    path("job-adverts/<int:advert_id>/", views.JobAdvertDetail.as_view(), name="job-advert-detail"),
    path("applications/", views.job_application, name="job-application"),
    path("applications/<int:application_id>/", views.JobApplicationDetail.as_view(), name="job-application-detail"),
]
