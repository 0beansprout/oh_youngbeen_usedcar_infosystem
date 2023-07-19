from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    technician_permissions = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                             content_type__model='technician')

    dealer_permissions = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                          content_type__model='dealer')

    customer_permissions = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                         content_type__model='customer')

    month_permissions = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                                  content_type__model='month')

    year_permissions = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                                  content_type__model='year')

    date_permissions = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                                  content_type__model='date')

    maintenance_schedule_permissions = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                           content_type__model='maintenance_schedule')

    auto_part_permissions = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                         content_type__model='auto_part')

    maintenance_permissions = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                          content_type__model='maintenance')

    inventory_permissions = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                              content_type__model='inventory')

    invoice_permissions = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                               content_type__model='invoice')

    perm_view_technician = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                           content_type__model='technician',
                                                           codename='view_technician')

    perm_view_dealer = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                        content_type__model='dealer',
                                                        codename='view_dealer')

    perm_view_customer = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                       content_type__model='customer',
                                                       codename='view_customer')

    perm_view_month = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                               content_type__model='month',
                                                               codename='view_month')

    perm_view_year = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                               content_type__model='year',
                                                               codename='view_year')

    perm_view_date = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                               content_type__model='date',
                                                               codename='view_date')

    perm_view_maintenance_schedule = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                         content_type__model='maintenance_schedule',
                                                         codename='view_maintenance_schedule')

    perm_view_auto_part = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                       content_type__model='auto_part',
                                                       codename='view_auto_part')

    perm_view_maintenance = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                        content_type__model='maintenance',
                                                        codename='view_maintenance')

    perm_view_inventory = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                        content_type__model='inventory',
                                                        codename='view_inventory')

    perm_view_invoice = permission_class.objects.filter(content_type__app_label='usedcarinfo',
                                                             content_type__model='invoice',
                                                             codename='view_invoice')

    ci_user_permissions = chain(perm_view_technician,
                                perm_view_month,
                                perm_view_year,
                                perm_view_date,
                                perm_view_dealer,
                                perm_view_customer,
                                perm_view_maintenance_schedule,
                                perm_view_auto_part,
                                perm_view_maintenance,
                                perm_view_inventory,
                                perm_view_invoice)

    ci_scheduler_permissions = chain(technician_permissions,
                                     month_permissions,
                                     year_permissions,
                                     date_permissions,
                                     maintenance_schedule_permissions,
                                     auto_part_permissions,
                                     maintenance_permissions,
                                     inventory_permissions,
                                     perm_view_dealer,
                                     perm_view_customer,
                                     perm_view_invoice)

    ci_registrar_permissions = chain(dealer_permissions,
                                     customer_permissions,
                                     invoice_permissions,
                                     perm_view_technician,
                                     perm_view_month,
                                     perm_view_year,
                                     perm_view_date,
                                     perm_view_auto_part,
                                     perm_view_maintenance_schedule,
                                     perm_view_maintenance,
                                     perm_view_inventory)

    my_groups_initialization_list = [
        {
            "name": "ci_user",
            "permissions_list": ci_user_permissions,
        },
        {
            "name": "ci_scheduler",
            "permissions_list": ci_scheduler_permissions,
        },
        {
            "name": "ci_registrar",
            "permissions_list": ci_registrar_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('usedcarinfo', '0009_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
