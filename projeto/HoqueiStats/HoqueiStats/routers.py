from rest_framework import routers
from StatsApp.viewsets import ClubeViewSet
router = routers.DefaultRouter()
router.register(r'clube', ClubeViewSet)