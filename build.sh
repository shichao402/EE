#!/usr/bin/env bash
source /Users/firo/.bash_profile
pyenv shell EE
rm -rf build
rm -rf dist
rm *.spec
pyinstaller --onefile -w --clean gui.py
chmod 777 dist/gui.app
cp -f log_config.json dist/
open ./dist/gui.app
echo "!"