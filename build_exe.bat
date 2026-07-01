@echo off
REM ============================================================
REM  build_exe.bat
REM  ดับเบิลคลิกไฟล์นี้เพื่อแปลง neon_space_dodger.py
REM  ให้เป็นไฟล์ .exe แบบไฟล์เดียว
REM  (ต้องวางไฟล์นี้ไว้ในโฟลเดอร์เดียวกับ neon_space_dodger.py)
REM ============================================================

echo [1/3] Installing pygame-ce and pyinstaller...
python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pygame-ce pyinstaller

echo.
echo [2/3] Building NeonSpaceDodger.exe ...
python -m PyInstaller --onefile --windowed --name "NeonSpaceDodger" neon_space_dodger.py

echo.
echo [3/3] Done!
echo Your .exe file is inside the "dist" folder:
echo    dist\NeonSpaceDodger.exe
echo.
pause
