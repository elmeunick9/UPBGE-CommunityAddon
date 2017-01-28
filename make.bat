@echo off
set OLD_CD=%CD%
cd ..
set PATH=%PATH%;%CD%\Blender\2.78\python\Scripts;%CD%\Blender\2.78\python\bin
cd %OLD_CD%

echo Executing make...
python.exe make.py %*
echo Done.

pause