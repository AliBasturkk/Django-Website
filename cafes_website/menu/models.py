from django.db import models
from datetime import date

# Sadece Fiyat Kontrolü İçin Basit Yemek Modeli
class FoodPrice(models.Model):
    food_code = models.CharField(max_length=50, unique=True, verbose_name="Yemek Kodu")
    name = models.CharField(max_length=200, verbose_name="Yemek Adı")
    current_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Güncel Fiyat")
    is_available = models.BooleanField(default=True, verbose_name="Mevcut")
    
    class Meta:
        verbose_name = "Yemek Fiyatı"
        verbose_name_plural = "Yemek Fiyatları"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.current_price}₺"


# Aylık Menü Modeli
class MonthlyMenu(models.Model):
    """Aylık güncel menü"""
    title = models.CharField(max_length=200, verbose_name="Menü Başlığı")
    month = models.IntegerField(verbose_name="Ay (1-12)", help_text="1=Ocak, 2=Şubat, ..., 12=Aralık")
    year = models.IntegerField(verbose_name="Yıl")
    content = models.TextField(verbose_name="Menü İçeriği")
    pdf_file = models.FileField(upload_to='monthly_menus/', blank=True, verbose_name="PDF Dosyası")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Aylık Menü"
        verbose_name_plural = "Aylık Menüler"
        ordering = ['-year', '-month']
        unique_together = ['month', 'year']
    
    def get_month_display(self):
        months = {1: 'Ocak', 2: 'Şubat', 3: 'Mart', 4: 'Nisan', 5: 'Mayıs', 6: 'Haziran',
                 7: 'Temmuz', 8: 'Ağustos', 9: 'Eylül', 10: 'Ekim', 11: 'Kasım', 12: 'Aralık'}
        return months.get(self.month, str(self.month))
    
    def __str__(self):
        return f"{self.get_month_display()} {self.year} - {self.title}"


# İletişim Formu Gönderileri
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ad Soyad")
    email = models.EmailField(verbose_name="E-posta")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    message = models.TextField(verbose_name="Mesaj")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Gönderim Tarihi")
    is_read = models.BooleanField(default=False, verbose_name="Okundu")
    
    class Meta:
        verbose_name = "İletişim Mesajı"
        verbose_name_plural = "İletişim Mesajları"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d.%m.%Y')}"
