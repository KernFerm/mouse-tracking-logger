@echo off

REM Installing pywin32 306 - it is for the project !!

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

echo Installing pywin32==306...

pip install pywin32==306

if %errorlevel% neq 0 (
    echo Installation failed.
    exit /b %errorlevel%
) else (
    echo Installation completed successfully.
)
echo.
echo You May Now Close..
pause
