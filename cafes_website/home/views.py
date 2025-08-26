from django.shortcuts import render, redirect
from django.contrib import messages
from menu.models import ContactSubmission

def home(request):
    """Ana sayfa"""
    meta_title = "Ana Sayfa | Lezzet Catering"
    meta_description = "İstanbul'da kaliteli catering hizmetleri. Ev yemekleri tadında lezzetler, kurumsal yemek servisleri ve aylık menü seçenekleri."
    meta_keywords = "istanbul catering, yemek servisi, kurumsal yemek, ev yemekleri, lezzet catering, istanbul yemek, fabrika yemek, aylık menü, yemek siparişi, sağlıklı yemekler"

    context = {
        'meta_title': meta_title,
        'meta_description': meta_description,
        'meta_keywords': meta_keywords,
    }
    
    return render(request, 'home/home.html', context)

def about(request):
    """Hakkımızda sayfası"""
    meta_title = "Hakkımızda | Lezzet Catering"
    meta_description = "Lezzet Catering'in hikayesi, misyonu ve vizyonu. İstanbul'da kaliteli yemek hizmeti sunan deneyimli ekibimizi tanıyın."
    meta_keywords = "lezzet catering hakkında, istanbul catering şirketi, yemek hizmeti deneyim, kurumsal catering geçmiş"

    context = {
        'meta_title': meta_title,
        'meta_description': meta_description,
        'meta_keywords': meta_keywords,
    }
    
    return render(request, 'home/about.html', context)

def services(request):
    """Hizmetlerimiz sayfası"""
    meta_title = "Hizmetlerimiz | Lezzet Catering"
    meta_description = "Lezzet Catering hizmetleri: Kurumsal catering, özel etkinlik yemekleri, aylık abonelik menüleri ve daha fazlası."
    meta_keywords = "catering hizmetleri, kurumsal yemek servisi, özel etkinlik catering, aylık menü, fabrika yemek hizmeti"
    
    context = {
        'meta_title': meta_title,
        'meta_description': meta_description,
        'meta_keywords': meta_keywords,
    }
    
    return render(request, 'home/services.html', context)

def contact(request):
    """İletişim sayfası"""
    print(f"Contact view called with method: {request.method}")
    
    if request.method == 'POST':
        print("POST request received!")
        print(f"All POST data: {dict(request.POST)}")
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        company = request.POST.get('company', '')
        subject = request.POST.get('subject', '')
        
        if name and email and phone and message and subject:
            try:
                full_message = message
                if company:
                    full_message = f"Şirket: {company}\n\n{message}"
                if subject:
                    full_message = f"Hizmet Türü: {subject}\n\n{full_message}"
                
                contact_submission = ContactSubmission.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    message=full_message
                )
                print(f"Contact submission created with ID: {contact_submission.id}")
                messages.success(request, 'Mesajınız başarıyla gönderildi. En kısa sürede size dönüş yapacağız.')
                return redirect('contact')
            except Exception as e:
                print(f"Error creating contact submission: {e}")
                messages.error(request, 'Mesaj gönderilirken bir hata oluştu. Lütfen tekrar deneyin.')
        else:
            missing_fields = []
            if not name:
                missing_fields.append('Ad Soyad')
            if not email:
                missing_fields.append('E-posta')
            if not phone:
                missing_fields.append('Telefon')
            if not message:
                missing_fields.append('Mesaj')
            if not subject:
                missing_fields.append('Hizmet Türü')
            
            error_msg = f"Lütfen şu alanları doldurun: {', '.join(missing_fields)}"
            print(f"Validation error: {error_msg}")
            messages.error(request, error_msg)
    else:
        print("GET request - showing form")
    
    meta_title = "İletişim | Lezzet Catering"
    meta_description = "Lezzet Catering ile iletişime geçin. İstanbul'da kaliteli catering hizmetleri için bizimle iletişime geçin."
    meta_keywords = "lezzet catering iletişim, istanbul catering telefon, yemek servisi iletişim, catering teklif al"

    context = {
        'meta_title': meta_title,
        'meta_description': meta_description,
        'meta_keywords': meta_keywords,
    }
    
    return render(request, 'home/contact.html', context)

def company_policy(request):
    """Şirket politikası sayfası"""
    meta_title = "Şirket Politikamız | Lezzet Catering"
    meta_description = "Lezzet Catering kalite, müşteri memnuniyeti, çevre ve gizlilik politikaları. HACCP ve ISO standartlarımız."
    meta_keywords = "lezzet catering politika, haccp sertifika, gıda güvenliği, kalite standartları, müşteri memnuniyeti"

    context = {
        'meta_title': meta_title,
        'meta_description': meta_description,
        'meta_keywords': meta_keywords,
    }
    
    return render(request, 'home/company_policy.html', context)
