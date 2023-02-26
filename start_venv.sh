#!/bin/bash

# starts an in-tree virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip3 install requirements.txt
pre-commit install
echo "run 'source .venv/bin/activate'"