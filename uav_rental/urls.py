
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("rental/", include("rental.urls")),
    path("api/rental/", include("rental.api.urls")),

]
