from django.contrib.gis.db import models


class Partner(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    tradingName = models.CharField(max_length=255)
    ownerName = models.CharField(max_length=255)
    document = models.CharField(max_length=255, unique=True)
    coverageArea = models.MultiPolygonField()
    address = models.PointField()

    def __str__(self):
        return self.tradingName

    def get_full_address(self):
        """
        Get the full address of the partner.

            Returns:
                str: The full address of the partner.
        """
        return f"{self.address.x}, {self.address.y}"

    def is_document_valid(self):
        """
        Check if the document number is valid.

            Returns:
                bool: True if the document is valid, False otherwise.
        """
        # Add your logic to validate the document number here

    class Meta:
        verbose_name_plural = 'Partners'
