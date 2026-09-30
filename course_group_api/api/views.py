from rest_framework import viewsets
from .models import ResearchArea, Member, Publication, Partner
from .serializers import (
    ResearchAreaSerializer, MemberSerializer,
    PublicationSerializer, PartnerSerializer
)


class ResearchAreaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ResearchArea.objects.all()
    serializer_class = ResearchAreaSerializer


class MemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class PublicationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
