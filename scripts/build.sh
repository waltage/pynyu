#!/bin/bash

cd ..
pip3 freeze --exclude pynyu > requirements.txt
rm -rf dist/*
python3 -m build
pip3 install dist/*.whl --force-reinstall
