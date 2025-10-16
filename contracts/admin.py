from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'conclusion_date', 'amount')
    search_fields = ('name',)
    list_filter = ('conclusion_date',)
