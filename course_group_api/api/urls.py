from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# 创建路由器并注册视图集
router = DefaultRouter()
router.register(r'research-areas', views.ResearchAreaViewSet, basename='research-area')
router.register(r'members', views.MemberViewSet, basename='member')
router.register(r'publications', views.PublicationViewSet, basename='publication')
router.register(r'partners', views.PartnerViewSet, basename='partner')

urlpatterns = [
    # 包含路由器生成的URL
    path('', include(router.urls)),
]
