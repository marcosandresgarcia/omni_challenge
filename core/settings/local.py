from core.settings.base import *
DEBUG = True
DB = "postgres"

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
            'NAME': 'omni',
            'USER': 'omni',
            'PASSWORD': 'omni',
    }
}

