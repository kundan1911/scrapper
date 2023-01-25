from django.db import models

# Create your models here.
class res_sale_model(models.Model):
    Id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField()
    Proptype=models.TextField(null=True)
    Link=models.TextField()
    Owner=models.TextField()
    BHK=models.TextField()
    Locality=models.TextField()
    City=models.TextField()
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

    
class res_rent_model(models.Model):
    Id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField()
    Proptype=models.TextField(null=True)
    Link=models.TextField()
    Owner=models.TextField()
    BHK=models.TextField()
    Locality=models.TextField()
    City=models.TextField()
    Rent=models.TextField()
    Carpet_Area=models.TextField()
    Furnishing=models.TextField()
    Facing=models.TextField()
    Tenant=models.TextField()
    Floor=models.TextField()
    Description=models.TextField()
    def __str__(self):
        return self.Owner


class res_pg_model(models.Model):
    Id=models.IntegerField(primary_key=True)
    Posted_by=models.TextField()
    Proptype=models.TextField()
    Link=models.TextField()
    Owner=models.TextField()
    Locality=models.TextField()
    City=models.TextField()
    Charges=models.TextField()
    PG_for=models.TextField()
    Description=models.TextField()
    def __str__(self):
        return self.Owner

class comm_sale_model(models.Model):
    Id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField()
    Proptype=models.TextField()
    Link=models.TextField()
    Owner=models.TextField()
    Locality=models.TextField()
    City=models.TextField()
    Price=models.TextField()
    Carpet_Area=models.TextField()
    Parking=models.TextField()
    Property_Age=models.TextField()
    Facing=models.TextField()
    Water_Availability=models.TextField()
    Pantry=models.TextField()
    Overlooking=models.TextField()
    Description=models.TextField()

    def __str__(self):
        return self.Owner


class comm_lease_model(models.Model):
    Id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField(null=True)
    Proptype=models.TextField(null=True)
    Link=models.TextField()
    Retailer=models.TextField()
    BHK=models.TextField()
    Locality=models.TextField()
    City=models.TextField()
    Price=models.TextField()
    Carpet_Area=models.TextField()
    Washroom=models.TextField()
    Facing=models.TextField()
    Pantry=models.TextField()
    Parking=models.TextField()
    Water_Availability=models.TextField()
    Price_Sqft=models.TextField()
    Property_Age=models.TextField()
    Description=models.TextField()


    def __str__(self):
        return self.Owner
