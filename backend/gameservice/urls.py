from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url, include

from gameservice import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'contests', views.ContestViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'submissions', views.SubmissionViewSet)
# router.register(r'contests/(?P<id>\d+)/history', views.ContestHistoryViewSet)

schema_view = get_swagger_view(title='GameServer ISOLA')

nested_router = routers.NestedSimpleRouter(router, r'contests', lookup='contest')
nested_router.register(r'history', views.NestedContestHistoryViewSet, base_name='contests')

urlpatterns = [
    url(r'api/v1/swagger', schema_view),
    url(r'api/v1/', include(nested_router.urls)),
    url(r'api/v1/', include(router.urls))
]

