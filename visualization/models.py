from django.db import models
class DataPoint(models.Model):
    intensity = models.FloatField()
    likelihood = models.FloatField()
    relevance = models.FloatField()
    year = models.IntegerField()
    country = models.CharField(max_length=100, null=True, blank=True)
    topic = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    pestle = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.year} - {self.country}"
