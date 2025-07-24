@echo off
echo Python PATH ayarlaniyor...

REM Python dizinlerini PATH'e ekle
setx PATH "%PATH%;C:\Users\PC\AppData\Local\Programs\Python\Python311\;C:\Users\PC\AppData\Local\Programs\Python\Python311\Scripts\"

echo.
echo Python PATH ayarlandi!
echo Yeni bir komut satiri acarak test edebilirsiniz.
echo.
pause 