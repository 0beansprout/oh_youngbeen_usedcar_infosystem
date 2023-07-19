from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


#Month(period)
class Month(models.Model):
    month_id = models.AutoField(primary_key=True)
    period_sequence = models.IntegerField(unique=True)
    period_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.period_name

    class Meta:
        ordering = ['period_sequence']


#Year
class Year(models.Model):
    year_id = models.AutoField(primary_key=True)
    year = models.IntegerField(unique=True)

    def __str__(self):
        return '%s' % self.year

    class Meta:
        ordering = ['year']


#Date
class Date(models.Model):
    date_id = models.AutoField(primary_key=True)
    date = models.IntegerField(unique=True)

    def __str__(self):
        return '%s' % self.date

    class Meta:
        ordering = ['date']


#Maintenance_schedule(semeseter)
class Maintenance_schedule(models.Model):
    maintenance_schedule_id = models.AutoField(primary_key=True)
    year = models.ForeignKey(Year, related_name='maintenance_schedule', on_delete=models.PROTECT)
    month = models.ForeignKey(Month, related_name='maintenance_schedule', on_delete=models.PROTECT)
    date = models.ForeignKey(Date, related_name='maintenance_schedule', on_delete=models.PROTECT)

    def __str__(self):
        return '%s  %s  %s' % (self.year.year, self.month.period_name, self.date.date)

    def get_absolute_url(self):
        return reverse('usedcarinfo_maintenance_schedule_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('usedcarinfo_maintenance_schedule_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('usedcarinfo_maintenance_schedule_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['year__year', 'month__period_sequence', 'date__date']
        constraints = [
            UniqueConstraint(fields=['year', 'month', 'date'], name='unique_maintenance_schedule')
        ]


#Auto_part(course)
class Auto_part(models.Model):
    auto_part_id = models.AutoField(primary_key=True)
    auto_part_number = models.CharField(max_length=20)
    auto_part_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.auto_part_number, self.auto_part_name)

    def get_absolute_url(self):
        return reverse('usedcarinfo_auto_part_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('usedcarinfo_auto_part_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('usedcarinfo_auto_part_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['auto_part_number', 'auto_part_name']
        constraints = [
            UniqueConstraint(fields=['auto_part_number', 'auto_part_name'], name='unique_auto_part')
        ]


#Technician(instructor)
class Technician(models.Model):
    technician_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('usedcarinfo_technician_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('usedcarinfo_technician_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse(
            'usedcarinfo_technician_delete_urlpattern',
            kwargs={'pk': self.pk}
        )

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'],
                             name='unique_technician')
        ]


#Dealer
class Dealer(models.Model):
    dealer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('usedcarinfo_dealer_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('usedcarinfo_dealer_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('usedcarinfo_dealer_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'],
                             name='unique_dealer')
        ]


#Customer
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('usedcarinfo_customer_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('usedcarinfo_customer_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('usedcarinfo_customer_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'],
                             name='unique_customer')
        ]


#Maintenance(section)
class Maintenance(models.Model):
    maintenance_id = models.AutoField(primary_key=True)
    maintenance_name = models.CharField(max_length=20)
    maintenance_schedule = models.ForeignKey(Maintenance_schedule, related_name='maintenance', on_delete=models.PROTECT)
    auto_part = models.ForeignKey(Auto_part, related_name='maintenance', on_delete=models.PROTECT)
    technician = models.ForeignKey(Technician, related_name='maintenance', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s (%s)' % (self.maintenance_name, self.auto_part.auto_part_number,  self.maintenance_schedule.__str__())

    def get_absolute_url(self):
        return reverse('usedcarinfo_maintenance_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('usedcarinfo_maintenance_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse(
            'usedcarinfo_maintenance_delete_urlpattern',
            kwargs={'pk': self.pk}
        )

    class Meta:
        ordering = ['auto_part', 'maintenance_name', 'maintenance_schedule']
        constraints = [
            UniqueConstraint(fields=['maintenance_schedule', 'auto_part', 'maintenance_name'],
                             name='unique_maintenance')
        ]


#Inventory(section)
class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=20)
    maintenance = models.ForeignKey(Maintenance, related_name='inventory', on_delete=models.PROTECT)
    dealer = models.ForeignKey(Dealer, related_name='inventory', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s (%s)' % (self.car_name, self.maintenance.maintenance_name, self.dealer.__str__())

    def get_absolute_url(self):
        return reverse('usedcarinfo_inventory_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('usedcarinfo_inventory_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse(
            'usedcarinfo_inventory_delete_urlpattern',
            kwargs={'pk': self.pk}
        )

    class Meta:
        ordering = ['maintenance', 'car_name', 'dealer']
        constraints = [
            UniqueConstraint(fields=['dealer', 'maintenance', 'car_name'],
                             name='unique_inventory')
        ]


#Invoice(registration)
class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name='invoice',  on_delete=models.PROTECT)
    inventory = models.ForeignKey(Inventory, related_name='invoice',  on_delete=models.PROTECT)

    def __str__(self):
        return '%s / %s' % (self.customer, self.inventory)

    def get_absolute_url(self):
        return reverse('usedcarinfo_invoice_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('usedcarinfo_invoice_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('usedcarinfo_invoice_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['inventory', 'customer']
        constraints = [
            UniqueConstraint(fields=['inventory', 'customer'],
                             name='unique_invoices')
        ]