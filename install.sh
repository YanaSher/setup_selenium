PATH=$PATH:$WORKSPACE
python3 -m venv venv
. venv/bin/activate
pip3 install -r tests/requirements.txt