from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('blogger', views.BloggerViewSet)

urlpatterns = [
    path("", views.index),
    path("mydetails/", views.mydetails),
    path("api/", include(router.urls)),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework'))
]