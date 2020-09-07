sed 's/#.*//' apt-requirements | xargs sudo apt-get install
pip3 install -r requirements.txt
