from django.contrib import admin

# Register your models here.
from .models import Beer, Entry

admin.site.register(Entry)

@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    fields = ('name', 'owner', 'status')
    search_fields = ('name',)
    ordering = ['name']
    
    # Django admin actions: See docs.
    @admin.action(description="Mark selected as not tasty")
    def mark_as_not_tasty(modeladmin, request, queryset):
        queryset.update(status="Not tasty")

    actions = [mark_as_not_tasty]    