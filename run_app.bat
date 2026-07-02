@echo off
:: Change directory to the folder where this batch script is located
cd /d "%~dp0"

echo ===================================================
echo   Starting Arabic Sentiment Analysis Application
echo ===================================================

:: Start Flask API Server
echo [1/2] Starting Flask backend server in a new window...
start "Arabic Sentiment Analysis - Flask API" cmd /k "venv\Scripts\python.exe app.py"

:: Wait for Flask server to initialize
echo Waiting for Flask server to initialize...
timeout /t 5 /nobreak > nul

:: Start Streamlit UI
echo [2/2] Starting Streamlit frontend UI...
venv\Scripts\streamlit.exe run UI.py

echo.
echo Application is running!
echo You can close this window and the API window to stop the application.
pause
