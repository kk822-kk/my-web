import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
application = get_wsgi_application()

if __name__ == "__main__":
    import django
    django.setup()
    from django.core.management import call_command
    call_command('runserver', '0.0.0.0:8000')