from django.contrib import admin
from django.urls import path, include
from microbiome_api.api.viewsets import EntryViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'entry', EntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('entries-table/', include('microbiome_api.urls')),
]
