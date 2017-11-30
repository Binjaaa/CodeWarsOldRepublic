@echo off
cls

set mypath=%cd%
@echo %mypath%

".paket\paket.exe" restore
if errorlevel 1 (
  exit /b %errorlevel%
)

"packages\FAKE\tools\Fake.exe" build.fsx
pause