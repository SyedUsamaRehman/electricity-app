from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electric_shop_management.settings')

application = get_asgi_application()