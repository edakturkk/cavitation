@echo off
echo Command Prompt icin Python PATH ayarlaniyor...

REM Sistem PATH'ine Python dizinlerini ekle
setx PATH "%PATH%;C:\Users\PC\AppData\Local\Programs\Python\Python311\;C:\Users\PC\AppData\Local\Programs\Python\Python311\Scripts\" /M

echo.
echo Python PATH ayarlandi!
echo Yeni bir Command Prompt acarak test edebilirsiniz.
echo.
pause 