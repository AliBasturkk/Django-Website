# Django Website

Bu proje bir Django web sitesidir. Kafeler için menü, iletişim ve diğer sayfaları içerir.

## Klasörler
- `home/` : Ana sayfa ve genel içerikler
- `menu/` : Menü ve yemek listeleri
- `media/` : Dosya ve görseller
- `static/` : Statik dosyalar (CSS, JS, resimler)
- `templates/` : HTML şablonları

## Kurulum
1. Python ve Django kurulu olmalı.
2. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
3. Veritabanı migrasyonlarını çalıştırın:
   ```bash
   python manage.py migrate
   ```
4. Sunucuyu başlatın:
   ```bash
   python manage.py runserver
   ```

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına bakınız.
