from django.urls import path
from .views import LoginView, AuthRoot, LogoutView, LoggedInView


urlpatterns = [ 
    path('login', LoginView.as_view(), name='api-login'),
    path('', AuthRoot.as_view(), name='api-auth-root'),
    path('logout', LogoutView.as_view(), name='api-logout'),
    path('logged-in', LoggedInView.as_view(), name='api-logged-in')
]

