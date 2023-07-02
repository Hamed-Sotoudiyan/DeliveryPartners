from django.contrib.gis.geos import Point
from rest_framework import generics
from rest_framework.generics import ListAPIView

from .models import Partner
from .serializers import PartnerSerializer


class PartnerDetailView(generics.RetrieveAPIView):
    """
        A view for retrieving a specific partner instance,
    which corresponds to item 1.2. in the Task document.

    This view extends the `generics.RetrieveAPIView` class provided by Django REST framework
    to retrieve a specific partner object from the database based on the specified lookup field.
    """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    lookup_field = 'id'


class NearestPartnerView(ListAPIView):
    """
        A view for retrieving the nearest partner based on longitude and latitude coordinates.
    which corresponds to item 1.3. in the Task document.

    This view extends the `ListAPIView` class provided by Django REST framework to retrieve
    the nearest partner object from the database based on the specified longitude and latitude
    coordinates.
    The partners are filtered based on the coverage area that contains the given location.
    """
    serializer_class = PartnerSerializer

    def get_queryset(self):
        longitude = self.request.query_params.get('longitude')
        latitude = self.request.query_params.get('latitude')

        location = Point(float(longitude), float(latitude))

        partners = Partner.objects.filter(coverageArea__contains=location)
        partners_distances = {}
        for partner in partners:
            distance = partner.address.distance(location)
            partners_distances[partner.id] = distance

        if not partners_distances:
            return []

        min_distnace = min(partners_distances.items(), key=lambda x: x[1])
        nearest_partner = partners.filter(id=int(min_distnace[0]))
        return nearest_partner if nearest_partner else []
