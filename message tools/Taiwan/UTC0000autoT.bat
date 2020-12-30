@echo off
start  "wumin" "C:\Windows\System32\cmd.exe"
cd /d G:\Message program\message tools\Taiwan

C:\Users\teddy\AppData\Local\Programs\Python\Python38-32\python.exe "G:\Message program\message tools\Taiwan\allUTCcopyToTaiwan.py"

pause
taskkill /f /im cmd.exe
exit
