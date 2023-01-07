from django.urls import path, include
from api.user.views import UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]