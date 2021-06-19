echo off
color a
cls
:main
echo [---------------------------------------------------------]
pause
git add .
git commit -m "Accepted"
git push -u origin main
goto main