from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.routers import APIRootView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer, LogoutSerializer, LoggedInSerializer
from django.contrib.auth.models import User
from django.contrib.auth import logout


class AuthRoot(APIRootView):

    def get(self, request, *args, **kwargs):
        return Response({
            'login': reverse('api-login', request=request),
            'logout': reverse('api-logout', request=request),
            'logged-in': reverse('api-logged-in', request=request)
        })


class LoginView(CreateAPIView):
    schema = AutoSchema(
        tags=['Auth'],
        component_name='login',
        operation_id_base='Login'
    )
    serializer_class = LoginSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class LoggedInView(RetrieveAPIView):
    schema = AutoSchema(
        tags=['Auth'],
        component_name='logged-in',
        operation_id_base='LoggedIn'
    )
    serializer_class = LoggedInSerializer

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({
                'detail': True
            })
        return Response({'detail': False})


class LogoutView(RetrieveAPIView):
    schema = AutoSchema(
        tags=['Auth'],
        component_name='logout',
        operation_id_base='Logout'
    )
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request):
        user = request.user
        logout(request)
        return Response({
            'details': f'Successfully logged out {user}.'
        })

