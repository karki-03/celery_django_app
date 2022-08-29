# celery_django_app
Simple application to demonstrate sending mail asynchronously using RabbitMQ, Celery and Django.

## How to configure
1. Run `python manage.py migrate`
2. Make a virtual environment and then execute the requirements.txt file.
    a. Inside the project directory run: `python -m venv env`
    b. On windows type: `env\Scripts\activate` to activate the virtual environment. Alternatively, type: `source env/bin/activate` on linux.
    c. Run `pip install -r requirements.txt`
3. Then run `python manage.py runserver`
4. Make sure to run the message broker server (RabbitMQ in our case) and Consumer/Worker (Celery in our case)
5. Run celery worker: `celery -A celerytutorial worker -l info -P eventlet`
6. Run RabbitMQ: `rabbitmq-server`
7. Run flower for celery visualization: `celery -A celerytutorial flower --address=127.0.0.6 --port=5566`
8. Make a .env file in the root directory defining your configurations for: EMAIL_HOST_USER & EMAIL_HOST_PASSWORD 
9. For more details, check out my blog on <b><a href="https://github.com/karki-03/django-rabbitMQ-celery">How to Use Celery and RabbitMQ and Flower with Django?</a></b>