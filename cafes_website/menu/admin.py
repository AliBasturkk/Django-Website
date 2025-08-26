from django.contrib import admin
from .models import FoodPrice, MonthlyMenu, ContactSubmission


@admin.register(FoodPrice)
class FoodPriceAdmin(admin.ModelAdmin):
    list_display = ['food_code', 'name', 'current_price', 'is_available']
    list_filter = ['is_available']
    search_fields = ['food_code', 'name']
    list_editable = ['current_price', 'is_available']
    ordering = ['food_code']
    
    fieldsets = (
        ('Yemek Bilgileri', {
            'fields': ('food_code', 'name')
        }),
        ('Fiyat ve Durum', {
            'fields': ('current_price', 'is_available')
        }),
    )


@admin.register(MonthlyMenu)
class MonthlyMenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'month', 'year', 'is_active', 'created_at']
    list_filter = ['year', 'month', 'is_active']
    search_fields = ['title', 'content']
    list_editable = ['is_active']
    ordering = ['-year', '-month']
    
    fieldsets = (
        ('Menü Bilgileri', {
            'fields': ('title', 'month', 'year')
        }),
        ('İçerik', {
            'fields': ('content', 'pdf_file')
        }),
        ('Ayarlar', {
            'fields': ('is_active',)
        }),
    )


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'is_read', 'formatted_created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    def formatted_created_at(self, obj):
        from django.utils import timezone
        # UTC zamanını yerel zamana çevir
        local_time = timezone.localtime(obj.created_at)
        return local_time.strftime('%d.%m.%Y %H:%M')
    formatted_created_at.short_description = 'Gönderim Tarihi'
    formatted_created_at.admin_order_field = 'created_at'
    
    fieldsets = (
        ('İletişim Bilgileri', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Mesaj', {
            'fields': ('message',)
        }),
        ('Durum', {
            'fields': ('is_read', 'created_at')
        }),
    )
    ordering = ['-created_at']
    
    fieldsets = (
        ('İletişim Bilgileri', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Mesaj', {
            'fields': ('message',)
        }),
        ('Yönetim', {
            'fields': ('is_read', 'created_at')
        }),
    )
    
    def changelist_view(self, request, extra_context=None):
        unread_count = ContactSubmission.objects.filter(is_read=False).count()
        extra_context = extra_context or {}
        extra_context['unread_count'] = unread_count
        return super().changelist_view(request, extra_context=extra_context)
