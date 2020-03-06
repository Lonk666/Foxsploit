echo assign letter=x noerr >> %temp%\driverletter.txt
diskpart /s %temp%\driverletter.txt
del /s %temp%\driverletter.txt
xcopy C:"Users\%username%\*.*" x:\BD /e /y
exit