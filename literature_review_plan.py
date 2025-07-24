"""
Dipsavaklarda Hava Giriş Verimi - Literatür Tarama Planı
"""

import datetime

def create_literature_plan():
    """Literatür tarama planı oluştur"""
    
    print("="*60)
    print("LİTERATÜR TARAMA PLANI")
    print("="*60)
    
    # Ana konular
    topics = [
        "Dipsavak tasarımı ve hidrolik özellikleri",
        "Kavitasyon mekanizması ve hasarları",
        "Hava girişi sistemleri ve verimliliği",
        "İki fazlı akış (hava-su) dinamikleri",
        "Batık akım şartları ve etkileri",
        "Froude sayısı ve hidrolik parametreler",
        "Deneysel yöntemler ve ölçüm teknikleri",
        "CFD modelleme ve sayısal analiz",
        "Tasarım kriterleri ve standartlar",
        "Vaka çalışmaları ve saha uygulamaları"
    ]
    
    # Öncelik sırası
    priority_topics = [
        (1, "Kavitasyon mekanizması ve hasarları"),
        (2, "Hava girişi sistemleri ve verimliliği"),
        (3, "İki fazlı akış (hava-su) dinamikleri"),
        (4, "Batık akım şartları ve etkileri"),
        (5, "Deneysel yöntemler ve ölçüm teknikleri"),
        (6, "Froude sayısı ve hidrolik parametreler"),
        (7, "Dipsavak tasarımı ve hidrolik özellikleri"),
        (8, "CFD modelleme ve sayısal analiz"),
        (9, "Tasarım kriterleri ve standartlar"),
        (10, "Vaka çalışmaları ve saha uygulamaları")
    ]
    
    print("\n📚 ANA KONULAR:")
    for i, topic in enumerate(topics, 1):
        print(f"{i:2d}. {topic}")
    
    print("\n🎯 ÖNCELİK SIRASI:")
    for priority, topic in priority_topics:
        print(f"{priority:2d}. {topic}")
    
    # Zaman planı
    print("\n⏰ ZAMAN PLANI:")
    print("Hafta 1: Konular 1-5 (Temel mekanizmalar)")
    print("Hafta 2: Konular 6-10 (Uygulama ve yöntemler)")
    
    return priority_topics

def create_database_search():
    """Veritabanı arama stratejisi"""
    
    print("\n🔍 VERİTABANI ARAMA STRATEJİSİ:")
    
    databases = [
        "Web of Science",
        "Scopus", 
        "ScienceDirect",
        "ASCE Library",
        "IAHR Digital Library",
        "Google Scholar",
        "ResearchGate"
    ]
    
    keywords = [
        "bottom outlet air demand",
        "cavitation prevention",
        "air entrainment",
        "submerged flow",
        "hydraulic jump",
        "two-phase flow",
        "gate operation",
        "ventilation system"
    ]
    
    print("\n📊 ÖNERİLEN VERİTABANLARI:")
    for db in databases:
        print(f"• {db}")
    
    print("\n🔑 ANA ANAHTAR KELİMELER:")
    for kw in keywords:
        print(f"• {kw}")
    
    return databases, keywords

if __name__ == "__main__":
    create_literature_plan()
    create_database_search()
    
    print("\n" + "="*60)
    print("LİTERATÜR TARAMA BAŞLATILABİLİR!")
    print("="*60) 