from mysite.views import SnippedViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('list', SnippedViewSet, base_name='person')