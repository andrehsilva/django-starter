from django.contrib import admin
from .models import Tenant, Domain

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    # Alterado de 'created_on' para 'created'
    list_display = ('schema_name', 'name', 'created')  
    search_fields = ('schema_name', 'name')

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
    search_fields = ('domain',)