@echo off
start  "wumin" "C:\Windows\System32\cmd.exe"
cd /d G:\Message program\message tools\UTC0000

C:\Users\teddy\AppData\Local\Programs\Python\Python38-32\python.exe "G:\Message program\message tools\UTC0000\allAutoCateUTC0000.py"

taskkill /f /im cmd.exe
exit