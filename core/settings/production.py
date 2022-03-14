from core.settings.base import *
DEBUG = False
DB = "sqlite"

if DB == "sqlite":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif DB == "postgres":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB_NAME'),
            'USER': os.environ.get('POSTGRES_DB_USER'),
            'PASSWORD': os.environ.get('POSTGRES_DB_PASSWORD'),
    }
}

