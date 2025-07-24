"""
Deneysel Kurulum Planı - Dipsavak Hava Giriş Verimi
"""

def create_experimental_plan():
    """Deneysel kurulum planı oluştur"""
    
    print("="*60)
    print("DENEYSEL KURULUM PLANI")
    print("="*60)
    
    # 1. Laboratuvar Hazırlığı
    print("\n🏗️ 1. LABORATUVAR HAZIRLIĞI")
    lab_requirements = [
        "Fırat Üniversitesi Hidrolik Laboratuvarı erişimi",
        "Yüksek basınçlı pompa sistemi (50+ m/s kapasite)",
        "Elektromanyetik akış ölçer (kalibre edilmiş)",
        "Akış kontrol vanası sistemi",
        "Basınç ölçüm sensörleri",
        "Hava hızı ölçüm cihazları",
        "Veri toplama sistemi (DAQ)",
        "Güvenlik ekipmanları"
    ]
    
    for i, req in enumerate(lab_requirements, 1):
        print(f"{i:2d}. {req}")
    
    # 2. Model Tasarımı
    print("\n🔧 2. MODEL TASARIMI")
    model_components = [
        "Ana su tankı (rezervuar simülasyonu)",
        "Dipsavak modeli (ölçekli)",
        "Kapak sistemi (farklı tipler)",
        "Havalandırma bacası",
        "Farklı enkesit şekilleri",
        "Batıklık ayar sistemi",
        "Çıkış havuzu",
        "Ölçüm noktaları"
    ]
    
    for i, comp in enumerate(model_components, 1):
        print(f"{i:2d}. {comp}")
    
    # 3. Parametre Matrisi
    print("\n📊 3. PARAMETRE MATRİSİ")
    parameters = {
        "Enkesit Şekilleri": ["Dairesel", "Dikdörtgen", "Elips", "Kare"],
        "Kapak Tipleri": ["Radial", "Düz", "Eğimli", "Kombinasyon"],
        "Batıklık Oranları": ["0%", "25%", "50%", "75%", "100%"],
        "Kapak Açıklıkları": ["10%", "25%", "50%", "75%", "100%"],
        "Debi Değerleri": ["Q1", "Q2", "Q3", "Q4", "Q5"],
        "Dipsavak Uzunlukları": ["L1", "L2", "L3"]
    }
    
    for param, values in parameters.items():
        print(f"\n{param}:")
        for value in values:
            print(f"  • {value}")
    
    return lab_requirements, model_components, parameters

def create_measurement_plan():
    """Ölçüm planı oluştur"""
    
    print("\n📏 4. ÖLÇÜM PLANI")
    
    measurements = [
        ("Su Debisi", "L/s", "Elektromanyetik akış ölçer"),
        ("Su Hızı", "m/s", "Pitot tüpü veya Doppler"),
        ("Basınç", "Pa", "Basınç sensörleri"),
        ("Hava Debisi", "L/s", "Hava akış ölçer"),
        ("Hava Hızı", "m/s", "Anemometre"),
        ("Su Seviyesi", "m", "Seviye ölçer"),
        ("Sıcaklık", "°C", "Sıcaklık sensörü"),
        ("Türbülans", "-", "Türbülans ölçer")
    ]
    
    print("Ölçüm Parametreleri:")
    for param, unit, method in measurements:
        print(f"• {param}: {unit} ({method})")
    
    # Ölçüm noktaları
    print("\n📍 ÖLÇÜM NOKTALARI:")
    locations = [
        "Kapak öncesi (giriş)",
        "Kapak altı (vena contracta)",
        "Havalandırma bacası girişi",
        "Dipsavak ortası",
        "Dipsavak sonu",
        "Çıkış havuzu"
    ]
    
    for i, loc in enumerate(locations, 1):
        print(f"{i}. {loc}")
    
    return measurements, locations

def create_data_analysis_plan():
    """Veri analiz planı oluştur"""
    
    print("\n📈 5. VERİ ANALİZ PLANI")
    
    analysis_methods = [
        "İstatistiksel analiz (ortalama, standart sapma)",
        "Korelasyon analizi (parametreler arası)",
        "Regresyon analizi (matematiksel model)",
        "Boyut analizi (Froude, Reynolds sayıları)",
        "Grafik analizi (trendler, dağılımlar)",
        "Karşılaştırmalı analiz (literatür ile)",
        "Optimizasyon analizi (en iyi parametreler)",
        "Belirsizlik analizi (hata hesaplamaları)"
    ]
    
    print("Analiz Yöntemleri:")
    for i, method in enumerate(analysis_methods, 1):
        print(f"{i:2d}. {method}")
    
    # Yazılım araçları
    print("\n💻 ÖNERİLEN YAZILIM ARAÇLARI:")
    software = [
        "Python (NumPy, Pandas, Matplotlib)",
        "MATLAB (veri analizi)",
        "Excel (temel hesaplamalar)",
        "Origin (grafik çizimi)",
        "SPSS (istatistiksel analiz)",
        "CFD yazılımları (ANSYS, OpenFOAM)"
    ]
    
    for sw in software:
        print(f"• {sw}")
    
    return analysis_methods, software

if __name__ == "__main__":
    create_experimental_plan()
    create_measurement_plan()
    create_data_analysis_plan()
    
    print("\n" + "="*60)
    print("DENEYSEL KURULUM PLANI HAZIR!")
    print("="*60) 