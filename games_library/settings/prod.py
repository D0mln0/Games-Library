from .base import *


# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["USER"],
        "PASSWORD": os.environ["PASSWORD"],
        "HOST": os.environ["HOST"],
        "PORT": int(os.environ["PORT"]),
    }
}
