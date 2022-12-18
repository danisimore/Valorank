#!/bin/sh

if [ "$SQL_DATABASE" = "valorank" ]
then
  echo "Watching for valorank..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
    done

    echo 'PostgreSQL stated'
fi

exec "$@"