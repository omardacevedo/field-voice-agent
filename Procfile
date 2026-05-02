web: PYTHONPATH=src uvicorn config.asgi:application --host 0.0.0.0 --port $PORT
release: PYTHONPATH=src python manage.py migrate --no-input
