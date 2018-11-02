rm -rf build
rm -rf dist
rm *.spec
pyinstaller --onefile -w --clean gui.py
chmod 777 dist/gui.app
open ./dist/gui.app