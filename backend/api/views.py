from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.routers import APIRootView
from rest_framework.reverse import reverse
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Rango API')
swagger_view = TemplateView.as_view(template_name='swagger-ui.html', extra_context={'schema_url': 'openapi-schema'})


# Create your views here.
class ApiRoot(APIRootView):

    def get(self, request, *args, **kwargs):
        return Response({
            # Auto-generated: a keyword used by the createapi command to know where to add new urls
            'user': reverse('user-list', request=request),
            'openapi': reverse('openapi-schema', request=request),
            'swagger-ui': reverse('swagger-ui', request=request),
            'auth': reverse('api-auth-root', request=request),
        })