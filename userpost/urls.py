from rest_framework.routers import DefaultRouter
from django.urls import include, path
from userpost import views

router = DefaultRouter()
router.register('', views.UserPostViewSet)

urlpatterns = [
    path('', include(router.urls))
]

