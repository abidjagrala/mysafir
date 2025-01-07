from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from django.contrib.admin import register

from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
from .models import  State, Year, Institution, InstitutionDetails

admin.site.unregister(User)
admin.site.unregister(Group)

@register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass

@admin.register(State)
class StateAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    import_form_class = ImportForm
    export_form_class = ExportForm


@admin.register(Year)
class YearAdmin(ModelAdmin,  ImportExportModelAdmin):
    list_display = ('id', 'hijri', 'english', 'is_current_year')
    list_filter = ('is_current_year',)
    import_form_class = ImportForm
    export_form_class = ExportForm


@admin.register(Institution)
class InstitutionAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'address',
        'state',
        'pincode',
        'created',
        'updated',
    )
    list_filter = ('state', 'created', 'updated')
    search_fields = ('name',)
    import_form_class = ImportForm
    export_form_class = ExportForm

@admin.register(InstitutionDetails)
class InstitutionDetailsAdmin(ModelAdmin):
    list_display = (
        'id',
        'institution',
        'year',
        'taalim',
        'moh_name',
        'moh_phone',
        'safir_name',
        'safir_phone',
        'safir_aadhar',
        'res_students',
        'total_students',
        'total_teachers',
        'donation_day',
        'serial_no',
        'halka_code',
        'ijazat_status',
        'next_donation_year',
        'comments',
        'safir_photo',
        'created',
        'updated',
    )
    list_filter = (
        'institution',
        'year',
        'next_donation_year',
        'created',
        'updated',
    )