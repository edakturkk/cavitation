# Python PATH Düzeltme Scripti
Write-Host "Python PATH ayarlaniyor..." -ForegroundColor Yellow

# Python dizinlerini PATH'e ekle
$pythonPath = "C:\Users\PC\AppData\Local\Programs\Python\Python311\"
$pythonScriptsPath = "C:\Users\PC\AppData\Local\Programs\Python\Python311\Scripts\"

# Mevcut PATH'i al ve güncelle
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
$newPath = $currentPath + ";" + $pythonPath + ";" + $pythonScriptsPath

# PATH'i güncelle
[Environment]::SetEnvironmentVariable("Path", $newPath, "User")

Write-Host "✅ Python PATH ayarlandi!" -ForegroundColor Green
Write-Host "Yeni bir PowerShell penceresi acarak test edebilirsiniz." -ForegroundColor Yellow 