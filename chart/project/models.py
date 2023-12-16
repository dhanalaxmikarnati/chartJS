from django.db import models
from django.utils import timezone

# Create your models here.
class Dashboard(models.Model):
    intensity = models.IntegerField()
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.CharField(max_length=100)
    url = models.URLField()
    region = models.CharField(max_length=100)
    impact = models.CharField(max_length=100, blank=True, null=True)
    # added = models.DateTimeField()
    added = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField()
    country = models.CharField(max_length=100)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    likelihood = models.IntegerField()
    start_year = models.IntegerField(null=True)  # New field for start_year
    end_year = models.IntegerField(null=True)  # New field for end_year

    city= models.CharField(max_length=100, null=True)


    def __str__(self):
        return f"Model {self.id}: {self.country}, {self.title}"
    
    
   