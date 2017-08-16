# steemfriend
http://steemfriend.com 의 django project 코드

## How to serve
uwsgi -H venv/ --http :8000 --wsgi-file steemfriend/wsgi.py

## Prepare settings
### For Centos
sudo yum install python34-devel
sudo yum install libffi-devel
sudo yum install openssl-devel
sudo yum install freetds freetds-devel python-devel
### For Linux Ubuntu
sudo apt-get install python3.4-dev
