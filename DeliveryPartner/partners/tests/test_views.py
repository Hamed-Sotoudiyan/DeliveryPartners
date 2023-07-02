import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from partners.models import Partner
from partners.serializers import PartnerSerializer

client = Client()


class PartnerDetailViewTestCase(TestCase):
    """
        Test cases for the PartnerDetailView class.

    This class contains unit tests to verify the behavior of the PartnerDetailView class,
    which is responsible for retrieving a specific partner instance.

    Example:
        To run the tests, you can use a test runner command such as:

        ```shell
        python manage.py test
        ```
    """
    def setUp(self):
        self.partner = Partner.objects.create(
            id='1',
            tradingName='Test Partner',
            ownerName='Test Owner',
            document='12345678901234',
            coverageArea='MULTIPOLYGON (((-46.76379 -23.55767, -46.76557 -23.55867, -46.76557 -23.56014, -46.76379 -23.56114, -46.76202 -23.56014, -46.76202 -23.55867, -46.76379 -23.55767)))',
            address='POINT (-46.76413 -23.55962)'
        )

    def test_get_valid_partner(self):
        response = client.get(reverse('partner-detail', kwargs={'id': '1'}))
        partner = Partner.objects.get(id='1')
        serializer = PartnerSerializer(partner)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_partner(self):
        response = client.get(reverse('partner-detail', kwargs={'id': '2'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class NearestPartnerViewTestCase(TestCase):
    """
        Test cases for the NearestPartnerView class.

    This class contains unit tests to verify the behavior of the NearestPartnerView class,
    which is responsible for retrieving the nearest partner based on longitude and latitude coordinates.

    Example:
        To run the tests, you can use a test runner command such as:

        ```shell
        python manage.py test
        ```
    """
    def setUp(self):
        self.partner1 = Partner.objects.create(
            id='1',
            tradingName='Test Partner 1',
            ownerName='Test Owner 1',
            document='12345678901234',
            coverageArea='MULTIPOLYGON (((-46.76379 -23.55767, -46.76557 -23.55867, -46.76557 -23.56014, -46.76379 -23.56114, -46.76202 -23.56014, -46.76202 -23.55867, -46.76379 -23.55767)))',
            address='POINT (-46.76413 -23.55962)'
        )
        self.partner2 = Partner.objects.create(
            id='2',
            tradingName='Test Partner 2',
            ownerName='Test Owner 2',
            document='123456789',
            coverageArea='MULTIPOLYGON (((-46.76657 -23.55967, -46.76835 -23.56067, -46.76835 -23.56214, -46.76657 -23.56314, -46.76480 -23.56214, -46.76480 -23.56067, -46.76657 -23.55967)))',
            address='POINT (-46.76701 -23.56162)'
        )

    def test_get_nearest_partner(self):
        response = client.get('/partners/nearest/?latitude=-23.55962&longitude=-46.76413')
        nearest_partner = Partner.objects.get(id='1')
        serializer = PartnerSerializer(nearest_partner)

        self.assertEqual(response.data[0], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_no_nearest_partner(self):
        response = client.get('/partners/nearest/?longitude=-46.76513&latitude=-23.55962')
        self.assertNotContains(response,'data')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
