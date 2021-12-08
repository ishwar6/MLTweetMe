
from django.urls import path, include
from rest_framework import routers
from data.views import PersonView
router = routers.DefaultRouter()
router.register(r'people', PersonView)


urlpatterns = [
    path('p/', include(router.urls)),
]
