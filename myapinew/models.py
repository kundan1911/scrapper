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
    
class no_broker_rent_model(models.Model):
    Id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField(null=True)
    Link=models.TextField()
    Rent=models.TextField()
    EMI=models.TextField()
    Nearby=models.TextField(null=True)
    SQFT=models.TextField()
    Furnishing=models.TextField()
    Available_from=models.TextField()
    Prop_Type=models.TextField()
    Preferred_Tenants=models.TextField()
    Apt_Type=models.TextField()
    Parking=models.TextField()
    Bedrooms=models.TextField()
    Possesion_By=models.TextField()
    Balcony=models.TextField()
    
    def __str__(self):
        return self.Owner
    
class no_broker_sale_model(models.Model):
    Id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField(null=True)
    Link=models.TextField()
    Price=models.TextField()
    EMI=models.TextField()
    Nearby=models.TextField(null=True)
    SQFT=models.TextField()
    Facing=models.TextField()
    Bathrooms=models.TextField()
    Apt_Type=models.TextField()
    Apt_Name=models.TextField()
    Parking=models.TextField()
    Bedrooms=models.TextField()
    Possesion_By=models.TextField()
    Balcony=models.TextField()
    Power_Backup=models.TextField()
    
    def __str__(self):
        return self.Owner
    

class no_broker_comm_rent_model(models.Model):
    Id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField(null=True)
    Link=models.TextField()
    Rent=models.TextField()
    Deposit=models.TextField()
    Nearby=models.TextField(null=True)
    SQFT=models.TextField()
    Floor=models.TextField()
    Prop_Type=models.TextField()
    Furnishing=models.TextField()
    Availability=models.TextField()
    Parking=models.TextField()
 
    def __str__(self):
        return self.Owner

class no_broker_comm_sale_model(models.Model):
    Id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField(null=True)
    Link=models.TextField()
    Price=models.TextField()
    EMI=models.TextField()
    Nearby=models.TextField(null=True)
    SQFT=models.TextField()
    Facing=models.TextField()
    Bathrooms=models.TextField()
    Apt_Type=models.TextField()
    Parking=models.TextField()
 
    def __str__(self):
        return self.Owner

class no_broker_pg_model(models.Model):
    Id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField(null=True)
    Link=models.TextField()
    Rent=models.TextField()
    Deposit=models.TextField()
    Nearby=models.TextField(null=True)
    Room_Type=models.TextField()
    Preferred_Tenants=models.TextField()
    Food=models.TextField()
    Parking=models.TextField()
    Possesion_By=models.TextField()
    def __str__(self):
        return self.Owner
