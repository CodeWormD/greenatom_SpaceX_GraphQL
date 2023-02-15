# sleep 10

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -w $SQL_HOST $SQL_PORT; do
#       sleep 0.5
#     done

#     echo "PostgreSQL started"
# fi


# python3 ./spacex/upload_data.py && psql -h postgres -U postgres -d postgres

# alembic upgrade head
# python spacex/upload_data.py
# ls

# exec "$@"

