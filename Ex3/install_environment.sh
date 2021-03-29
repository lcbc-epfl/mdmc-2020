#!/bin/sh

# Install necessary packages for mdmc course on juptyer hub
python3 -m venv my_venvs/mdmc
source my_venvs/mdmcbin/activate
pip install numpy matplotlib ipykernel py3Dmol
python3 -m ipykernel install --user --name=mdmc