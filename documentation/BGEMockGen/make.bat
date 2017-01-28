@echo off
set OLD_CD=%CD%
cd ..
cd ..
cd ..
set PATH=%PATH%;%CD%\Blender\2.78\python\Scripts;%CD%\Blender\2.78\python\bin
cd %OLD_CD%

python.exe make.py %*

pause