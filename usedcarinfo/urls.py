from django.urls import path

from usedcarinfo.views import (
    TechnicianList,
    MaintenanceList,
    InventoryList,
    Auto_partList,
    Maintenance_scheduleList,
    DealerList,
    CustomerList,
    InvoiceList,
    TechnicianDetail,
    MaintenanceDetail,
    InventoryDetail,
    Auto_partDetail,
    Maintenance_scheduleDetail,
    DealerDetail,
    CustomerDetail,
    InvoiceDetail,
    TechnicianCreate,
    TechnicianUpdate,
    TechnicianDelete,
    MaintenanceCreate,
    MaintenanceUpdate,
    MaintenanceDelete,
    InventoryCreate,
    InventoryUpdate,
    InventoryDelete,
    Auto_partCreate,
    Auto_partUpdate,
    Auto_partDelete,
    Maintenance_scheduleCreate,
    Maintenance_scheduleUpdate,
    Maintenance_scheduleDelete,
    DealerCreate,
    DealerUpdate,
    DealerDelete,
    CustomerCreate,
    CustomerUpdate,
    CustomerDelete,
    InvoiceCreate,
    InvoiceUpdate,
    InvoiceDelete,
)

urlpatterns = [
    path('technician/',
         TechnicianList.as_view(),
         name='usedcarinfo_technician_list_urlpattern'),

    path('technician/<int:pk>/',
         TechnicianDetail.as_view(),
         name='usedcarinfo_technician_detail_urlpattern'),

    path('technician/create/',
         TechnicianCreate.as_view(),
         name='usedcarinfo_technician_create_urlpattern'),

    path('technician/<int:pk>/update/',
         TechnicianUpdate.as_view(),
         name='usedcarinfo_technician_update_urlpattern'),

    path('technician/<int:pk>/delete/',
         TechnicianDelete.as_view(),
         name='usedcarinfo_technician_delete_urlpattern'),

    path('maintenance/',
         MaintenanceList.as_view(),
         name='usedcarinfo_maintenance_list_urlpattern'),

    path('maintenance/<int:pk>/',
         MaintenanceDetail.as_view(),
         name='usedcarinfo_maintenance_detail_urlpattern'),

    path('maintenance/Create/',
         MaintenanceCreate.as_view(),
         name='usedcarinfo_maintenance_create_urlpattern'),

    path('maintenance/<int:pk>/update/',
         MaintenanceUpdate.as_view(),
         name='usedcarinfo_maintenance_update_urlpattern'),

    path('maintenance/<int:pk>/delete/',
         MaintenanceDelete.as_view(),
         name='usedcarinfo_maintenance_delete_urlpattern'),

    path('inventory/',
         InventoryList.as_view(),
         name='usedcarinfo_inventory_list_urlpattern'),

    path('inventory/<int:pk>/',
         InventoryDetail.as_view(),
         name='usedcarinfo_inventory_detail_urlpattern'),

    path('inventory/Create/',
         InventoryCreate.as_view(),
         name='usedcarinfo_inventory_create_urlpattern'),

    path('inventory/<int:pk>/update/',
         InventoryUpdate.as_view(),
         name='usedcarinfo_inventory_update_urlpattern'),

    path('inventory/<int:pk>/delete/',
         InventoryDelete.as_view(),
         name='usedcarinfo_inventory_delete_urlpattern'),

    path('autopart/',
         Auto_partList.as_view(),
         name='usedcarinfo_auto_part_list_urlpattern'),

    path('autopart/<int:pk>/',
         Auto_partDetail.as_view(),
         name='usedcarinfo_auto_part_detail_urlpattern'),

    path('autopart/create/',
         Auto_partCreate.as_view(),
         name='usedcarinfo_auto_part_create_urlpattern'),

    path('autopart/<int:pk>/update/',
         Auto_partUpdate.as_view(),
         name='usedcarinfo_auto_part_update_urlpattern'),

    path('autopart/<int:pk>/delete/',
         Auto_partDelete.as_view(),
         name='usedcarinfo_auto_part_delete_urlpattern'),

    path('schedule/',
         Maintenance_scheduleList.as_view(),
         name='usedcarinfo_maintenance_schedule_list_urlpattern'),

    path('schedule/<int:pk>/',
         Maintenance_scheduleDetail.as_view(),
         name='usedcarinfo_maintenance_schedule_detail_urlpattern'),

    path('schedule/create/',
         Maintenance_scheduleCreate.as_view(),
         name='usedcarinfo_maintenance_schedule_create_urlpattern'),

    path('schedule/<int:pk>/update/',
         Maintenance_scheduleUpdate.as_view(),
         name='usedcarinfo_maintenance_schedule_update_urlpattern'),

    path('schedule/<int:pk>/delete/',
         Maintenance_scheduleDelete.as_view(),
         name='usedcarinfo_maintenance_schedule_delete_urlpattern'),

    path('dealer/',
         DealerList.as_view(),
         name='usedcarinfo_dealer_list_urlpattern'),

    path('dealer/<int:pk>/',
         DealerDetail.as_view(),
         name='usedcarinfo_dealer_detail_urlpattern'),

    path('dealer/create/',
         DealerCreate.as_view(),
         name='usedcarinfo_dealer_create_urlpattern'),

    path('dealer/<int:pk>/update/',
         DealerUpdate.as_view(),
         name='usedcarinfo_dealer_update_urlpattern'),

    path('dealer/<int:pk>/delete/',
         DealerDelete.as_view(),
         name='usedcarinfo_dealer_delete_urlpattern'),

    path('customer/',
         CustomerList.as_view(),
         name='usedcarinfo_customer_list_urlpattern'),

    path('customer/<int:pk>/',
         CustomerDetail.as_view(),
         name='usedcarinfo_customer_detail_urlpattern'),

    path('customer/create/',
         CustomerCreate.as_view(),
         name='usedcarinfo_customer_create_urlpattern'),

    path('customer/<int:pk>/update/',
         CustomerUpdate.as_view(),
         name='usedcarinfo_customer_update_urlpattern'),

    path('customer/<int:pk>/delete/',
         CustomerDelete.as_view(),
         name='usedcarinfo_customer_delete_urlpattern'),

    path('invoice/',
         InvoiceList.as_view(),
         name='usedcarinfo_invoice_list_urlpattern'),

    path('invoice/<int:pk>/',
         InvoiceDetail.as_view(),
         name='usedcarinfo_invoice_detail_urlpattern'),

    path('invoice/create/',
         InvoiceCreate.as_view(),
         name='usedcarinfo_invoice_create_urlpattern'),

    path('invoice/<int:pk>/update/',
         InvoiceUpdate.as_view(),
         name='usedcarinfo_invoice_update_urlpattern'),

    path('invoice/<int:pk>/delete/',
         InvoiceDelete.as_view(),
         name='usedcarinfo_invoice_delete_urlpattern'),
]
