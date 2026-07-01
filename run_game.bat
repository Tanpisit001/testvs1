@echo off
title เกมงูกินหาง
echo กำลังเปิดเกมงูกินหาง...
echo.

REM ตรวจสอบว่ามี python ติดตั้งอยู่หรือไม่
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [Error] ไม่พบ Python ในเครื่องนี้
    echo กรุณาติดตั้ง Python จาก https://www.python.org/downloads/
    echo อย่าลืมติ๊กช่อง "Add Python to PATH" ตอนติดตั้งด้วยนะครับ
    pause
    exit /b
)

REM รันเกม (ไฟล์ .py ต้องอยู่โฟลเดอร์เดียวกับ .bat นี้)
python "%~dp0snake_game.py"

pause
