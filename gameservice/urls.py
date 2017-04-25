from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url, include

from gameservice import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'contests', views.MatchViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'submissions', views.CodeBotViewSet)
router.register(r'gamemoves', views.HistoryViewSet)

schema_view = get_swagger_view(title='GameServer ISOLA')

urlpatterns = [
    url(r'api/v1/swagger', schema_view),
    url(r'api/v1/', include(router.urls))
]
