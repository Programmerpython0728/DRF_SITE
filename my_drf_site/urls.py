from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet,BookViewSet

router=routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'books',BookViewSet)

urlpatterns = [
    path('', include(router.urls)),

]

