from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import BasicAuthentication

schema_view = get_schema_view(
   openapi.Info(
      title="Job Posting",
      default_version='v1',
      description="API backend of a simple job posting application. The application contains three entities; Job Advert, Job Application, and User. A job advert can optionally have a job application.",
      terms_of_service="",
      contact=openapi.Contact(email="desmond.nnebue@torilo.co.uk"),
      license=openapi.License(name=""),
   ),
   public=True,
#    authentication_classes=[BasicAuthentication],
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("v1/", include("main.urls", namespace="main")),
    path("v1/", include("accounts.urls")),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
