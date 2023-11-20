from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/accounts/", include("accounts.urls")),
    path("api/v1/mall_test/", include("mall_test.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path("", TemplateView.as_view(template_name="root.html"), name="root"),
    ]
