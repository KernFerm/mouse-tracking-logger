@echo off
REM Save the current directory
pushd %~dp0

REM Run the Python script and check for errors
echo Running config.py...
python config.py
if %errorlevel% neq 0 (
    echo Error: mouse.py did not run successfully.
    popd
    exit /b %errorlevel%
)

REM Provide success feedback
echo config.py ran successfully.

REM Return to the original directory
popd
