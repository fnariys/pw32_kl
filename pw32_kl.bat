@echo off
set URL=
set OUTPUT=C:\\

powershell -Command "Invoke-WebRequest -Uri %URL% -OutFile %OUTPUT%"

exit
