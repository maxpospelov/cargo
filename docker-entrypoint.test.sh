#!/bin/bash
set -e

task="$1"

case $task in
    superuser)
        echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
        ;;
    flush)
        python3 manage.py flush --noinput
        ;;
    migrate)
        python3 manage.py makemigrations --noinput
        python3 manage.py migrate
        ;;
esac