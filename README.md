# kvstore
a simple kvstroe API with flask + gunicorn + supervisor +Redis

```shell
# ubuntu 18
sudo su
apt-get install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
env/bin/gunicorn -D --workers 4 --bind 0.0.0.0:8000 alpine.wsgi:application
```