@echo off
:restart
title EZ Browser
echo Building application...
pyuic5 ui/browser.ui -o browser.py
echo Running...
python ezbrowser.py %*
if errorlevel 1 (goto restart)
pause