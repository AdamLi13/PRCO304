# Project PRCO304

this the PRCO304 proejct - Blockcahin-based fake product identification system.

To be able to run this system, below are prerequisites that you may need to install :

eth-brownie
qrcode

Installation
via pipx
The recommended way to install Brownie is via pipx. pipx installs Brownie into a virtual environment and makes it available directly from the commandline. Once installed, you will never have to activate a virtual environment prior to using Brownie.

To install pipx:

python3 -m pip install --user pipx
python3 -m pipx ensurepath
To install Brownie using pipx:

pipx install eth-brownie
To upgrade to the latest version:

pipx upgrade eth-brownie
To use lastest master or another branch as version:

pipx install git+https://github.com/eth-brownie/brownie.git@master
via pip
You can install the latest release via pip:

pip install eth-brownie
via setuptools
You can clone the repository and use setuptools for the most up-to-date version:

git clone https://github.com/eth-brownie/brownie.git
cd brownie
python3 setup.py install
as a library
If you want to install brownie inside your own project (rather than as a standalone cli tool):

export BROWNIE_LIB=1
pip install eth-brownie
This loosens the pins on all dependencies. You'll want to make sure you have your own requirements.txt to make sure upgrades upstream don't surprise anyone.

for development
There are extra tools that are helpful when developing:

git clone https://github.com/eth-brownie/brownie.git
cd brownie
python3 -m venv venv
./venv/bin/pip install wheel
./venv/bin/pip install -e . -r requirements-dev.txt
Upgrading the pinned versions of dependencies is easy:

./venv/bin/pip-compile --upgrade
./venv/bin/pip-compile --upgrade requirements-dev.in
./venv/bin/pip-compile --upgrade requirements-windows.in


To install QR Code:

pip install qrcode.
