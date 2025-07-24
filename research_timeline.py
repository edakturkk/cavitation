"""
Araştırma Zaman Çizelgesi - Dipsavak Hava Giriş Verimi
"""

from datetime import datetime, timedelta

def create_research_timeline():
    """Araştırma zaman çizelgesi oluştur"""
    
    print("="*70)
    print("ARAŞTIRMA ZAMAN ÇİZELGESİ")
    print("="*70)
    
    # 24 aylık plan
    timeline = [
        {
            "Aşama": "1. HAZIRLIK VE LİTERATÜR",
            "Süre": "1-3 ay",
            "Aktiviteler": [
                "Detaylı literatür taraması",
                "Araştırma sorularının netleştirilmesi",
                "Hipotezlerin oluşturulması",
                "Ön çalışma raporu hazırlama",
                "Laboratuvar erişim izinleri"
            ],
            "Çıktılar": [
                "Literatür özeti raporu",
                "Araştırma metodolojisi",
                "Ön çalışma sonuçları"
            ]
        },
        {
            "Aşama": "2. DENEYSEL KURULUM",
            "Süre": "4-6 ay", 
            "Aktiviteler": [
                "Laboratuvar ekipmanlarının hazırlanması",
                "Model tasarımı ve imalatı",
                "Ölçüm sistemlerinin kurulumu",
                "Kalibrasyon işlemleri",
                "Pilot deneyler"
            ],
            "Çıktılar": [
                "Çalışır durumda deney düzeneği",
                "Kalibrasyon raporları",
                "Pilot deney sonuçları"
            ]
        },
        {
            "Aşama": "3. VERİ TOPLAMA",
            "Süre": "7-13 ay",
            "Aktiviteler": [
                "Sistematik deneyler",
                "Parametrik çalışmalar",
                "Veri kayıt ve depolama",
                "Kalite kontrol",
                "Ön analizler"
            ],
            "Çıktılar": [
                "Ham veri setleri",
                "Deney protokolleri",
                "Ön analiz raporları"
            ]
        },
        {
            "Aşama": "4. VERİ ANALİZİ",
            "Süre": "14-18 ay",
            "Aktiviteler": [
                "İstatistiksel analizler",
                "Matematiksel modelleme",
                "Korelasyon çalışmaları",
                "Optimizasyon analizleri",
                "Karşılaştırmalı değerlendirmeler"
            ],
            "Çıktılar": [
                "Analiz sonuçları",
                "Matematiksel modeller",
                "Optimizasyon önerileri"
            ]
        },
        {
            "Aşama": "5. DOĞRULAMA",
            "Süre": "19-20 ay",
            "Aktiviteler": [
                "Sonuçların doğrulanması",
                "Hata analizleri",
                "Belirsizlik hesaplamaları",
                "Literatür ile karşılaştırma",
                "Sonuçların değerlendirilmesi"
            ],
            "Çıktılar": [
                "Doğrulama raporu",
                "Hata analizi",
                "Karşılaştırmalı değerlendirme"
            ]
        },
        {
            "Aşama": "6. TEZ YAZIMI",
            "Süre": "21-24 ay",
            "Aktiviteler": [
                "Tez yazımı",
                "Grafik ve tabloların hazırlanması",
                "Literatür listesinin güncellenmesi",
                "Tez kontrolü ve düzeltmeler",
                "Sunum hazırlığı"
            ],
            "Çıktılar": [
                "Tamamlanmış tez",
                "Sunum dosyaları",
                "Yayın hazırlıkları"
            ]
        }
    ]
    
    # Zaman çizelgesini yazdır
    for i, stage in enumerate(timeline, 1):
        print(f"\n📅 AŞAMA {i}: {stage['Aşama']}")
        print(f"⏰ Süre: {stage['Süre']}")
        
        print("\n🔧 Aktiviteler:")
        for activity in stage['Aktiviteler']:
            print(f"  • {activity}")
        
        print("\n📄 Çıktılar:")
        for output in stage['Çıktılar']:
            print(f"  ✓ {output}")
        
        print("-" * 50)
    
    return timeline

def create_milestone_checklist():
    """Kilometre taşları kontrol listesi"""
    
    print("\n🎯 KİLOMETRE TAŞLARI KONTROL LİSTESİ")
    print("="*50)
    
    milestones = [
        ("3. ay", "Literatür taraması tamamlandı"),
        ("6. ay", "Deney düzeneği hazır"),
        ("13. ay", "Tüm deneyler tamamlandı"),
        ("18. ay", "Veri analizi tamamlandı"),
        ("20. ay", "Doğrulama işlemleri bitti"),
        ("24. ay", "Tez tamamlandı")
    ]
    
    for month, milestone in milestones:
        print(f"📌 {month}: {milestone}")
    
    return milestones

def create_risk_analysis():
    """Risk analizi"""
    
    print("\n⚠️ RİSK ANALİZİ VE ÖNLEMLER")
    print("="*50)
    
    risks = [
        {
            "Risk": "Laboratuvar ekipmanı arızası",
            "Olasılık": "Orta",
            "Etki": "Yüksek",
            "Önlem": "Yedek ekipman, bakım planı"
        },
        {
            "Risk": "Veri kaybı",
            "Olasılık": "Düşük", 
            "Etki": "Çok Yüksek",
            "Önlem": "Yedekleme, bulut depolama"
        },
        {
            "Risk": "Zaman aşımı",
            "Olasılık": "Orta",
            "Etki": "Orta",
            "Önlem": "Esnek planlama, öncelik belirleme"
        },
        {
            "Risk": "Bütçe yetersizliği",
            "Olasılık": "Düşük",
            "Etki": "Yüksek", 
            "Önlem": "Alternatif kaynaklar, maliyet optimizasyonu"
        },
        {
            "Risk": "Teknik zorluklar",
            "Olasılık": "Orta",
            "Etki": "Orta",
            "Önlem": "Uzman danışmanlığı, pilot çalışmalar"
        }
    ]
    
    for risk in risks:
        print(f"\n🚨 {risk['Risk']}")
        print(f"   Olasılık: {risk['Olasılık']}")
        print(f"   Etki: {risk['Etki']}")
        print(f"   Önlem: {risk['Önlem']}")
    
    return risks

if __name__ == "__main__":
    create_research_timeline()
    create_milestone_checklist()
    create_risk_analysis()
    
    print("\n" + "="*70)
    print("ARAŞTIRMA PLANI TAMAMLANDI!")
    print("="*70) 