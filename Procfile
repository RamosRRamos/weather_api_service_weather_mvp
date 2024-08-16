web: gunicorn weather_api_service.wsgi --log-file -
worker: celery -A weather_api_service worker --loglevel=info
