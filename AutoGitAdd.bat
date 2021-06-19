echo off
color a
:main
cls
pause
git add .
git commit -m "Accepted"
git push -u origin main
goto main