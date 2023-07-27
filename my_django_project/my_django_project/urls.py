from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="TTWordServer",
        default_version='0.10.0',
        description="This is TTWord API Documentation.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kimjunghyun696@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('star-wars/', include('my_api.urls')),
   path('admin', admin.site.urls),
   path('api/', include(('sample_swagger.urls', 'api'))),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^api(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^api/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]