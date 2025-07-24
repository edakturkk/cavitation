# Sistem PATH'ini düzeltme scripti
# Bu scripti YÖNETİCİ olarak çalıştırın!

Write-Host "Sistem PATH'i ayarlaniyor..." -ForegroundColor Yellow

# Python dizinlerini tanımla
$pythonPath = "C:\Users\PC\AppData\Local\Programs\Python\Python311\"
$pythonScriptsPath = "C:\Users\PC\AppData\Local\Programs\Python\Python311\Scripts\"

# Mevcut sistem PATH'ini al
$currentSystemPath = [Environment]::GetEnvironmentVariable("Path", "Machine")

# Python dizinlerini kontrol et
if (Test-Path $pythonPath) {
    Write-Host "✓ Python dizini bulundu" -ForegroundColor Green
} else {
    Write-Host "✗ Python dizini bulunamadi!" -ForegroundColor Red
    exit 1
}

if (Test-Path $pythonScriptsPath) {
    Write-Host "✓ Python Scripts dizini bulundu" -ForegroundColor Green
} else {
    Write-Host "✗ Python Scripts dizini bulunamadi!" -ForegroundColor Red
    exit 1
}

# PATH'e ekle (eğer zaten yoksa)
$newSystemPath = $currentSystemPath
if ($currentSystemPath -notlike "*$pythonPath*") {
    $newSystemPath = $currentSystemPath + ";" + $pythonPath
    Write-Host "Python dizini sistem PATH'ine ekleniyor..." -ForegroundColor Cyan
}

if ($currentSystemPath -notlike "*$pythonScriptsPath*") {
    $newSystemPath = $newSystemPath + ";" + $pythonScriptsPath
    Write-Host "Python Scripts dizini sistem PATH'ine ekleniyor..." -ForegroundColor Cyan
}

# Sistem PATH'ini güncelle
[Environment]::SetEnvironmentVariable("Path", $newSystemPath, "Machine")

Write-Host "`n✅ Sistem PATH'i basariyla ayarlandi!" -ForegroundColor Green
Write-Host "Yeni bir Command Prompt veya PowerShell acarak test edebilirsiniz." -ForegroundColor Yellow
Write-Host "Test komutu: python --version" -ForegroundColor Cyan

Write-Host "`nİşlem tamamlandi!" -ForegroundColor Green 