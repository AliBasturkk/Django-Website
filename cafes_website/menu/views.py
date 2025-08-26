from django.shortcuts import render
from .models import FoodPrice, MonthlyMenu

def menu_list(request):
    """Menü ana sayfası"""
    current_monthly_menu = MonthlyMenu.objects.filter(is_active=True).first()
    food_prices = FoodPrice.objects.filter(is_available=True).order_by('name')
    
    meta_title = "Menülerimiz | Lezzet Catering"
    meta_description = "Lezzet Catering güncel menülerini inceleyin. İstanbul'da ev yemekleri tadında catering menüleri, aylık menü seçenekleri ve fiyatları."
    meta_keywords = "istanbul menü, catering yemekleri, aylık menü, yemek fiyatları, lezzet catering menü, kurumsal yemek menüsü"

    context = {
        'current_monthly_menu': current_monthly_menu,
        'food_prices': food_prices,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'meta_keywords': meta_keywords,
    }
    
    return render(request, 'menu/menu_list.html', context)

def monthly_menu(request):
    """Aylık menü sayfası"""
    current_menu = MonthlyMenu.objects.filter(is_active=True).first()
    # Aktif olmayan menüleri veya güncel aydan önceki tüm menüleri göster
    previous_menus = MonthlyMenu.objects.exclude(id=current_menu.id if current_menu else None).order_by('-year', '-month')[:6]

    meta_title = "Aylık Menü | Lezzet Catering"
    meta_description = "Lezzet Catering aylık menü seçenekleri. Güncel menülerimizi inceleyin, PDF olarak indirin. Kurumsal catering aylık abonelik menüleri."
    meta_keywords = "aylık menü, lezzet catering menü, kurumsal aylık menü, istanbul aylık catering, menü pdf indirme"

    context = {
        'current_menu': current_menu,
        'previous_menus': previous_menus,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'meta_keywords': meta_keywords,
    }
    
    return render(request, 'menu/monthly_menu.html', context)
