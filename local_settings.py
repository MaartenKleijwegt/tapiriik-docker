import os

# Look in settings.py for more settings to override
# including mongodb, rabbitmq, and redis connection settings

MONGO_HOST = "mongo"
REDIS_HOST = "redis"
RABBITMQ_BROKER_URL = "amqp://guest:guest@rabbitmq/"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'tapiriik': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    }
}

# This is the url that is used for redirects after logging in to each service
# It only needs to be accessible to the client browser
WEB_ROOT = os.environ.get("WEB_ROOT", "http://localhost:8000")

# This is where sync logs show up
# It is the only directory that needs to be writable by the webapp user
USER_SYNC_LOGS = os.environ.get("USER_SYNC_LOGS", "###")

# These settings are used to communicate with each respective service
# Register your installation with each service to get these values

RUNKEEPER_CLIENT_ID = os.environ.get("RUNKEEPER_CLIENT_ID", "###")
RUNKEEPER_CLIENT_SECRET = os.environ.get("RUNKEEPER_CLIENT_SECRET", "###")

DROPBOX_FULL_APP_KEY = os.environ.get("DROPBOX_FULL_APP_KEY", "###")
DROPBOX_FULL_APP_SECRET = os.environ.get("DROPBOX_FULL_APP_SECRET", "###")

DROPBOX_APP_KEY = os.environ.get("DROPBOX_APP_KEY", "###")
DROPBOX_APP_SECRET = os.environ.get("DROPBOX_APP_SECRET", "###")

STRAVA_CLIENT_SECRET = os.environ.get("STRAVA_CLIENT_SECRET", "###")
STRAVA_CLIENT_ID = os.environ.get("STRAVA_CLIENT_ID", "###")

STRAVA_RATE_LIMITS = os.environ.get("STRAVA_RATE_LIMITS", "###")

SPORTTRACKS_CLIENT_ID = os.environ.get("SPORTTRACKS_CLIENT_ID", "###")
SPORTTRACKS_CLIENT_SECRET = os.environ.get("SPORTTRACKS_CLIENT_SECRET", "###")

ENDOMONDO_CLIENT_KEY = os.environ.get("ENDOMONDO_CLIENT_KEY", "###")
ENDOMONDO_CLIENT_SECRET = os.environ.get("ENDOMONDO_CLIENT_SECRET", "###")

NIKEPLUS_CLIENT_NAME = os.environ.get("NIKEPLUS_CLIENT_NAME", "###")
NIKEPLUS_CLIENT_ID = os.environ.get("NIKEPLUS_CLIENT_ID", "###")
NIKEPLUS_CLIENT_SECRET = os.environ.get("NIKEPLUS_CLIENT_SECRET", "###")

RWGPS_APIKEY = os.environ.get("RWGPS_APIKEY", "###")

# See http://api.smashrun.com for info.
# For now, you need to email hi@smashrun.com for access
SMASHRUN_CLIENT_ID = os.environ.get("SMASHRUN_CLIENT_ID", "###")
SMASHRUN_CLIENT_SECRET = os.environ.get("SMASHRUN_CLIENT_SECRET", "###")

MOTIVATO_PREMIUM_USERS_LIST_URL = os.environ.get("MOTIVATO_PREMIUM_USERS_LIST_URL", "###")

CREDENTIAL_STORAGE_PUBLIC_KEY = bytes.fromhex(os.environ.get("CREDENTIAL_STORAGE_PUBLIC_KEY", "###"))
CREDENTIAL_STORAGE_PRIVATE_KEY = bytes.fromhex(os.environ.get("CREDENTIAL_STORAGE_PRIVATE_KEY", "###"))
