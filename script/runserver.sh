python manage.py migrate
python manage.py setpermissions
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:$PORT