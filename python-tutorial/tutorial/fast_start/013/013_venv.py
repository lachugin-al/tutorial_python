"""
sudo apt install python3-venv
python3 -m venv venv

source venv/
source venv/bin/activate

pip -V
pip install -U pip
pip install selenium

pip freeze

pip install requests==2.24.0



.gitignore
venv/

requirements.txt
в него кладем библиотеки которые мы хотим переносить вместе с развертыванием окружения

deactivate

source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
"""