@echo off
REM Start the FastAPI backend server
REM This script activates the venv and starts the uvicorn server

cd /d %~dp0
echo.
echo ============================================
echo AI Startup Intelligence - Backend Startup
echo ============================================
echo.

REM Check if venv exists
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate venv
call .\.venv\Scripts\activate.bat

REM Install/upgrade dependencies
echo.
echo Installing dependencies...
pip install -r backend/requirements.txt

REM Start backend
echo.
echo Starting FastAPI server on http://localhost:8000
echo.
cd backend
uvicorn app:app --host 0.0.0.0 --port 8000 --reload

pause
