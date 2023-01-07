from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User 
from api.user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    schema = AutoSchema(
        tags=['User'],
        component_name='user',
        operation_id_base='User'
    )
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]