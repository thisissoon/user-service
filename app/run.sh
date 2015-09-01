sleep 5  # waits for another container to be ready

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
