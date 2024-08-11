from django.contrib import admin
from .models import MoistureLevel

@admin.register(MoistureLevel)
class MoistureLevelAdmin(admin.ModelAdmin):
    list_display = ('saturated', 'created_at')
    list_filter = ('saturated', 'created_at')
    search_fields = ('created_at',)
