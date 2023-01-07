from django.urls import include, re_path
from .views import ApiRoot, schema_view, swagger_view


urlpatterns = [
    # Auto-generated: a keyword used by the createapi command to know where to add new urls
    re_path('$', ApiRoot.as_view(), name='api-root'),
    re_path('', include('api.user.urls')),
    re_path('openapi', schema_view, name='openapi-schema'),
    re_path('swagger-ui', swagger_view, name='swagger-ui'),
    re_path('openapi', schema_view, name='openapi-schema'),
    re_path('swagger-ui', swagger_view, name='swagger-ui'),
    re_path('auth/', include('api.auth.urls')),
]