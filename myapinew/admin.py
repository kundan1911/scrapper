from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here
all_models=[res_rent_model,res_pg_model,res_sale_model,comm_lease_model,comm_sale_model,no_broker_rent_model,no_broker_sale_model]
admin.site.register(all_models)