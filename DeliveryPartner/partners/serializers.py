from rest_framework import serializers

from .models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    coverageArea = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    def get_coverageArea(self, partner):
        return {
            "type": "MultiPolygon",
            "coordinates": partner.coverageArea.coords
        }

    def get_address(self, partner):
        return {
            "type": "Point",
            "coordinates": [partner.address.x, partner.address.y]
        }

    class Meta:
        model = Partner
        fields = ('id', 'tradingName', 'ownerName', 'document', 'coverageArea', 'address')
