from django.contrib import admin

from .models import Maintenance_schedule, Auto_part, Technician, Dealer, Customer, Maintenance, Inventory, Invoice, Month, Year, Date

admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Date)
admin.site.register(Maintenance_schedule)
admin.site.register(Auto_part)
admin.site.register(Technician)
admin.site.register(Dealer)
admin.site.register(Customer)
admin.site.register(Maintenance)
admin.site.register(Inventory)
admin.site.register(Invoice)
