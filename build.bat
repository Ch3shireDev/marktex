pyinstaller -y --onefile marktex.py
move .\dist\marktex\marktex.exe .\dist
RMDIR /Q /S dist\marktex
RMDIR /Q /S build
