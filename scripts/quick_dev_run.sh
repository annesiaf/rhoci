#!/bin/bash
source .venv/bin/activate
pip install --upgrade .
rhoci run --debug -p 5000
