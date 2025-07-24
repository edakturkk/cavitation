from docx import Document
import os

def read_docx_file(file_path):
    """Word dosyasını oku ve içeriğini döndür"""
    try:
        doc = Document(file_path)
        full_text = []
        
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():  # Boş paragrafları atla
                full_text.append(paragraph.text)
        
        return '\n'.join(full_text)
    
    except Exception as e:
        return f"Dosya okuma hatası: {str(e)}"

# Dosya yolunu belirt
file_path = "dosyalar/EDA EN SON HALİ FORM-31_TEZ KONUSU ve PLANI (2) (3).docx"

# Dosyanın var olup olmadığını kontrol et
if os.path.exists(file_path):
    print("Dosya bulundu, okunuyor...")
    content = read_docx_file(file_path)
    print("\n" + "="*50)
    print("DOSYA İÇERİĞİ:")
    print("="*50)
    print(content)
else:
    print(f"Dosya bulunamadı: {file_path}") 