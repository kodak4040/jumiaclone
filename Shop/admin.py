from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(myuser)
admin.site.register(Customer)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Order)
admin.site.register(OrderProduct)