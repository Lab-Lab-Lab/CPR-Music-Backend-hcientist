#!/bin/bash

NAME="dev_api_musiccpr"                                     # Name of the application
DJANGODIR=/data/worktree/dev/backend/live                   # Django project directory
#SOCKFILE=/home/ec2-user/dev-versions/live/deploy/dev/asgi.sock # we will communicte using this unix socket
#SOCKFILE=/run/django/asgi.sock # we will communicate using this unix socket
SOCKFILE=/data/socks/dev/asgi.sock
#USER=nginx                                             # the user to run as
USER=ec2-user                                             # the user to run as
GROUP=ec2-user                                           # the group to run as
#GROUP=nginx                                           # the group to run as
NUM_WORKERS=4                                           # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=config.settings.production       # which settings file should Django use
DJANGO_ASGI_MODULE=config.asgi                          # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /data/venv-all/dev/v2.1/bin/activate
export DJANGO_READ_DOT_ENV_FILE=True
export DJANGO_SETTINGS_MODULE=config.settings.production
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_ASGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  -k uvicorn.workers.UvicornWorker \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$DJANGODIR/logs/gunicorn.log
