#!/bin/bash
pip3 install pyinstaller
pyinstaller --onefile main.py
cp dist/main main