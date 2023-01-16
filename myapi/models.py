from django.db import models

# Create your models here.
class Entries(models.Model):
    id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField()
    Link=models.TextField()
    Owner=models.TextField()
    bHK=models.TextField()
    Locality=models.TextField()
    city=models.TextField()
    Price=models.TextField()
    Carpet_Area=models.TextField()
    Furnishing=models.TextField()
    Bathrooms=models.TextField()
    Facing=models.TextField()
    Status=models.TextField()
    Transaction=models.TextField()
    Price_Sqft=models.TextField()
    Floor=models.TextField()
    Description=models.TextField()

    def __str__(self):
        return self.Owner