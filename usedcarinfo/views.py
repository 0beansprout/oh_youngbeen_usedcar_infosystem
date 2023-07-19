from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import (
    TechnicianForm, MaintenanceForm, InventoryForm, Auto_partForm, Maintenance_scheduleForm, DealerForm, CustomerForm, InvoiceForm,
)
from .models import (
    Technician, Maintenance, Inventory, Auto_part, Maintenance_schedule, Dealer, Customer, Invoice,
)
from .utils import PageLinksMixin


class TechnicianList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Technician
    permission_required = 'usedcarinfo.view_technician'


class TechnicianDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Technician
    permission_required = 'usedcarinfo.view_technician'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        technician = self.get_object()
        maintenance_list = technician.maintenance.all()
        context['maintenance_list'] = maintenance_list
        return context


class TechnicianCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = TechnicianForm
    model = Technician
    permission_required = 'usedcarinfo.add_technician'


class TechnicianUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = TechnicianForm
    model = Technician
    template_name = 'usedcarinfo/technician_form_update.html'
    permission_required = 'usedcarinfo.change_technician'



class TechnicianDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Technician
    success_url = reverse_lazy('usedcarinfo_technician_list_urlpattern')
    permission_required = 'usedcarinfo.delete_technician'


    def get(self, request, pk):
        technician = get_object_or_404(Technician, pk=pk)
        maintenance = technician.maintenance.all()
        if maintenance.count() > 0:
            return render(
                request,
                'usedcarinfo/technician_refuse_delete.html',
                {'technician': technician,
                 'maintenance': maintenance,
                 }
            )
        else:
            return render(
                request,
                'usedcarinfo/technician_confirm_delete.html',
                {'technician': technician}
            )


class MaintenanceList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Maintenance
    permission_required = 'usedcarinfo.view_maintenance'


class MaintenanceDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Maintenance
    permission_required = 'usedcarinfo.view_maintenance'


    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        maintenance = self.get_object()
        maintenance_schedule = maintenance.maintenance_schedule
        auto_part = maintenance.auto_part
        technician = maintenance.technician
        inventory_list = maintenance.inventory.all()
        context['maintenance_schedule'] = maintenance_schedule
        context['auto_part'] = auto_part
        context['technician'] = technician
        context['inventory_list'] = inventory_list
        return context


class MaintenanceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = MaintenanceForm
    model = Maintenance
    permission_required = 'usedcarinfo.add_maintenance'



class MaintenanceUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = MaintenanceForm
    model = Maintenance
    template_name = 'usedcarinfo/maintenance_form_update.html'
    permission_required = 'usedcarinfo.change_maintenance'



class MaintenanceDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Maintenance
    success_url = reverse_lazy('usedcarinfo_maintenance_list_urlpattern')
    permission_required = 'usedcarinfo.delete_maintenance'


    def get(self, request, pk):
        maintenance = get_object_or_404(Maintenance, pk=pk)
        inventory = maintenance.inventory.all()
        if inventory.count() > 0:
            return render(
                request,
                'usedcarinfo/maintenance_refuse_delete.html',
                {'maintenance': maintenance,
                 'inventory': inventory,
                 }
            )
        else:
            return render(
                request,
                'usedcarinfo/maintenance_confirm_delete.html',
                {'maintenance': maintenance}
            )


class InventoryList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Inventory
    permission_required = 'usedcarinfo.view_inventory'



class InventoryDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Inventory
    permission_required = 'usedcarinfo.view_inventory'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        inventory = self.get_object()
        maintenance = inventory.maintenance
        dealer = inventory.dealer
        invoice_list = inventory.invoice.all()
        context['maintenance'] = maintenance
        context['dealer'] = dealer
        context['invoice_list'] = invoice_list
        return context


class InventoryCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = InventoryForm
    model = Inventory
    permission_required = 'usedcarinfo.add_inventory'


class InventoryUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = InventoryForm
    model = Inventory
    template_name = 'usedcarinfo/inventory_form_update.html'
    permission_required = 'usedcarinfo.change_inventory'


class InventoryDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Inventory
    success_url = reverse_lazy('usedcarinfo_inventory_list_urlpattern')
    permission_required = 'usedcarinfo.delete_inventory'

    def get(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        invoice = inventory.invoice.all()
        if invoice.count() > 0:
            return render(
                request,
                'usedcarinfo/inventory_refuse_delete.html',
                {'inventory': inventory,
                 'invoice': invoice,
                 }
            )
        else:
            return render(
                request,
                'usedcarinfo/inventory_confirm_delete.html',
                {'inventory': inventory}
            )


class Auto_partList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Auto_part
    permission_required = 'usedcarinfo.view_auto_part'


class Auto_partDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Auto_part
    permission_required = 'usedcarinfo.view_auto_part'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        auto_part = self.get_object()
        maintenance_list = auto_part.maintenance.all()
        context['maintenance_list'] = maintenance_list
        return context


class Auto_partCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = Auto_partForm
    model = Auto_part
    permission_required = 'usedcarinfo.add_auto_part'


class Auto_partUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = Auto_partForm
    model = Auto_part
    template_name = 'usedcarinfo/auto_part_form_update.html'
    permission_required = 'usedcarinfo.change_auto_part'


class Auto_partDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Auto_part
    success_url = reverse_lazy('usedcarinfo_auto_part_list_urlpattern')
    permission_required = 'usedcarinfo.delete_auto_part'

    def get(self, request, pk):
        auto_part = get_object_or_404(Auto_part, pk=pk)
        maintenance = auto_part.maintenance.all()
        if maintenance.count() > 0:
            return render(
                request,
                'usedcarinfo/auto_part_refuse_delete.html',
                {'auto_part': auto_part,
                 'maintenance': maintenance,
                 }
            )
        else:
            return render(
                request,
                'usedcarinfo/auto_part_confirm_delete.html',
                {'auto_part': auto_part}
            )


class Maintenance_scheduleList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Maintenance_schedule
    permission_required = 'usedcarinfo.view_maintenance_schedule'


class Maintenance_scheduleDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Maintenance_schedule
    permission_required = 'usedcarinfo.view_maintenance_schedule'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        maintenance_schedule = self.get_object()
        maintenance_list = maintenance_schedule.maintenance.all()
        context['maintenance_list'] = maintenance_list
        return context


class Maintenance_scheduleCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = Maintenance_scheduleForm
    model = Maintenance_schedule
    permission_required = 'usedcarinfo.add_maintenance_schedule'


class Maintenance_scheduleUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = Maintenance_scheduleForm
    model = Maintenance_schedule
    template_name = 'usedcarinfo/maintenance_schedule_form_update.html'
    permission_required = 'usedcarinfo.change_maintenance_schedule'


class Maintenance_scheduleDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Maintenance_schedule
    success_url = reverse_lazy('usedcarinfo_maintenance_list_urlpattern')
    permission_required = 'usedcarinfo.delete_maintenance_schedule'

    def get(self, request, pk):
        maintenance_schedule = get_object_or_404(Maintenance_schedule, pk=pk)
        maintenance = maintenance_schedule.maintenance.all()
        if maintenance.count() > 0:
            return render(
                request,
                'usedcarinfo/maintenance_schedule_refuse_delete.html',
                {'maintenance_schedule': maintenance_schedule,
                 'maintenance': maintenance,
                 }
            )
        else:
            return render(
                request,
                'usedcarinfo/maintenance_schedule_confirm_delete.html',
                {'maintenance_schedule': maintenance_schedule}
            )


class DealerList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Dealer
    permission_required = 'usedcarinfo.view_dealer'


class DealerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Dealer
    permission_required = 'usedcarinfo.view_dealer'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dealer = self.get_object()
        inventory_list = dealer.inventory.all()
        context['inventory_list'] = inventory_list
        return context


class DealerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = DealerForm
    model = Dealer
    permission_required = 'usedcarinfo.add_dealer'


class DealerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = DealerForm
    model = Dealer
    template_name = 'usedcarinfo/dealer_form_update.html'
    permission_required = 'usedcarinfo.change_dealer'


class DealerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Dealer
    success_url = reverse_lazy('usedcarinfo_dealer_list_urlpattern')
    permission_required = 'usedcarinfo.delete_dealer'

    def get(self, request, pk):
        dealer = get_object_or_404(Dealer, pk=pk)
        inventory = dealer.inventory.all()
        if inventory.count() > 0:
            return render(
                request,
                'usedcarinfo/dealer_refuse_delete.html',
                {'dealer': dealer,
                 'inventory': inventory,
                 }
            )
        else:
            return render(
                request,
                'usedcarinfo/dealer_confirm_delete.html',
                {'dealer': dealer}
            )


class CustomerList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Customer
    permission_required = 'usedcarinfo.view_customer'


class CustomerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Customer
    permission_required = 'usedcarinfo.view_customer'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        customer = self.get_object()
        invoice_list = customer.invoice.all()
        context['invoice_list'] = invoice_list
        return context


class CustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CustomerForm
    model = Customer
    permission_required = 'usedcarinfo.add_customer'


class CustomerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CustomerForm
    model = Customer
    template_name = 'usedcarinfo/customer_form_update.html'
    permission_required = 'usedcarinfo.change_customer'


class CustomerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('usedcarinfo_customer_list_urlpattern')
    permission_required = 'usedcarinfo.delete_customer'

    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        invoice = customer.invoice.all()
        if invoice.count() > 0:
            return render(
                request,
                'usedcarinfo/customer_refuse_delete.html',
                {'customer': customer,
                 'invoice': invoice,
                 }
            )
        else:
            return render(
                request,
                'usedcarinfo/customer_confirm_delete.html',
                {'customer': customer}
            )


class InvoiceList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Invoice
    permission_required = 'usedcarinfo.view_invoice'


class InvoiceDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Invoice
    permission_required = 'usedcarinfo.view_invoice'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        invoice = self.get_object()
        customer = invoice.customer
        inventory = invoice.inventory
        context['customer'] = customer
        context['inventory'] = inventory
        return context


class InvoiceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = InvoiceForm
    model = Invoice
    permission_required = 'usedcarinfo.add_invoice'


class InvoiceUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = InvoiceForm
    model = Invoice
    template_name = 'usedcarinfo/invoice_form_update.html'
    permission_required = 'usedcarinfo.change_invoice'


class InvoiceDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Invoice
    success_url = reverse_lazy('usedcarinfo_invoice_list_urlpattern')
    permission_required = 'usedcarinfo.delete_invoice'
