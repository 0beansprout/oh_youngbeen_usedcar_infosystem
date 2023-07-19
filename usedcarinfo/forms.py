from django import forms

from usedcarinfo.models import Technician, Maintenance, Inventory, Auto_part, Maintenance_schedule, Dealer, Customer, Invoice


class TechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'

    def clean_maintenance_name(self):
        return self.cleaned_data['maintenance_name'].strip()


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

    def clean_inventory_name(self):
        return self.cleaned_data['car_name'].strip()


class Auto_partForm(forms.ModelForm):
    class Meta:
        model = Auto_part
        fields = '__all__'

    def clean_auto_part_number(self):
        return self.cleaned_data['auto_part_number'].strip()

    def clean_auto_part_name(self):
        return self.cleaned_data['auto_part_name'].strip()


class Maintenance_scheduleForm(forms.ModelForm):
    class Meta:
        model = Maintenance_schedule
        fields = '__all__'


class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
