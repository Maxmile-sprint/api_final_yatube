from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowAPIView, GroupViewSet, PostViewSet


router_version_1 = DefaultRouter()

router_version_1.register('posts', PostViewSet)
router_version_1.register('groups', GroupViewSet)
router_version_1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/follow/', FollowAPIView.as_view(), name='follow'),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_version_1.urls)),
]
