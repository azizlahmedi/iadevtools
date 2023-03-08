NeoXam
======

Django
------

python manage.py createsuperuser --username=admin --email=olivier.mansion@neoxam.com

PostgreSQL
----------

psql -c "CREATE USER neoxam_user UNENCRYPTED PASSWORD 'XXX' INHERIT LOGIN"
createdb --owner neoxam_user --template template0 --encoding=UTF8 --lc-ctype=en_US.UTF-8 --lc-collate=en_US.UTF-8 neoxam_db

RabbitMQ
--------

http://www.rabbitmq.com/install-debian.html

sudo rabbitmqctl add_user neoxam 1234
sudo rabbitmqctl add_vhost neoxam
sudo rabbitmqctl set_permissions -p neoxam neoxam ".*" ".*" ".*"

Eclipse compilation
-------------------

Compilation elapsed time can be at max X seconds.

gunicorn:
* --timeout XXX

nginx:
* proxy_read_timeout XXX;


