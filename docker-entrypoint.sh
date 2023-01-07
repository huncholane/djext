#!/bin/bash

# postgres stuff
chown postgres:postgres /var/lib/postgresql/data
if [ ! "$(ls -A /var/lib/postgresql/data)" ]; then
  su postgres -c "initdb -D /var/lib/postgresql/data"
fi
sed -i 's/\/run\/postgresql/\/tmp/' /var/lib/postgresql/data/postgresql.conf
su postgres -c 'pg_ctl start -D /var/lib/postgresql/data'

nginx
tail -f /var/lib/nginx/logs/access.log &

cd frontend && npm start &
cd backend && python manage.py migrate
cd /backend && uvicorn backend.asgi:application --host 0.0.0.0