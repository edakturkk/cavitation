# Python PATH Manuel Düzeltme Rehberi

## Sorun
Command Prompt'ta "Python bulunamadı" hatası alıyorsunuz.

## Çözüm Yöntemleri

### Yöntem 1: Sistem Ortam Değişkenlerini Manuel Düzenleme

1. **Windows + R** tuşlarına basın
2. **sysdm.cpl** yazıp Enter'a basın
3. **Gelişmiş** sekmesine tıklayın
4. **Ortam Değişkenleri** butonuna tıklayın
5. **Sistem değişkenleri** bölümünde **Path**'i seçin
6. **Düzenle** butonuna tıklayın
7. **Yeni** butonuna tıklayın
8. Aşağıdaki yolları ekleyin:
   ```
   C:\Users\PC\AppData\Local\Programs\Python\Python311\
   C:\Users\PC\AppData\Local\Programs\Python\Python311\Scripts\
   ```
9. **Tamam** ile tüm pencereleri kapatın
10. Yeni bir Command Prompt açın

### Yöntem 2: Batch Dosyası Çalıştırma

1. `fix_cmd_python.bat` dosyasını **YÖNETİCİ OLARAK** çalıştırın
2. Yeni bir Command Prompt açın
3. `python --version` komutunu test edin

### Yöntem 3: PowerShell Script Çalıştırma

1. PowerShell'i **YÖNETİCİ OLARAK** açın
2. `fix_system_path.ps1` scriptini çalıştırın
3. Yeni bir Command Prompt açın
4. `python --version` komutunu test edin

## Test

Düzeltme sonrası test edin:
```cmd
python --version
pip --version
```

## Not

- Sistem PATH değişiklikleri tüm kullanıcılar için geçerlidir
- Değişikliklerin etkili olması için yeni bir Command Prompt açmanız gerekir 