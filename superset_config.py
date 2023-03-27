# https://github.com/apache/superset/blob/master/superset/config.py

from datetime import date, timedelta
import os

# from custom_sso_security_manager import CustomSsoSecurityManager
# CUSTOM_SECURITY_MANAGER = CustomSsoSecurityManager
#

SIP_15_ENABLED = True
# SIP_15_GRACE_PERIOD_END = date(<YYYY>, <MM>, <DD>)

REDIS_ADDRESS = os.environ.get("REDIS_ADDRESS")

CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 60 * 60 * 24, # 1 day default (in secs)
    'CACHE_KEY_PREFIX': 'superset_results',
    'CACHE_REDIS_URL': f'redis://{REDIS_ADDRESS}:6379/0',
}

SUPERSET_WEBSERVER_TIMEOUT = int(timedelta(minutes=2).total_seconds())

# DATA_CACHE_CONFIG = {
#     'CACHE_TYPE': 'redis',
#     'CACHE_DEFAULT_TIMEOUT': 60 * 60 * 24, # 1 day default (in secs)
#     'CACHE_KEY_PREFIX': 'superset_chart_results',
#     'CACHE_REDIS_URL': f'redis://{REDIS_ADDRESS}:6379/0',
# }

FEATURE_FLAGS = { 'ENABLE_TEMPLATE_PROCESSING': True}

CACHE_NO_NULL_WARNING = True

# Superset specific config
ROW_LIMIT = 5000

SUPERSET_WEBSERVER_PORT = 8088

# Flask App Builder configuration
# Your App secret key
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''

from flask_appbuilder.security.manager import AUTH_OAUTH
AUTH_TYPE = AUTH_OAUTH
OAUTH_PROVIDERS = [
    {   'name':'MaterialAzureSSO',
        'token_key':'access_token', # Name of the token in the response of access_token_url
        'remote_app': {
            'client_id':'OAUTH_CLIENT_ID',  # Client Id (Identify Superset application)
            'client_secret':'OAUTH_CLIENT_SECRET', # Secret for this Client Id (Identify Superset application)
            'client_kwargs':{
                'scope': 'https://graph.microsoft.com/.default'               # Scope for the Authorization
            },
            'access_token_method':'POST',    # HTTP Method to call access_token_url
            'access_token_params':{        # Additional parameters for calls to access_token_url
                'client_id':'OAUTH_CLIENT_ID'
            },
            'access_token_headers':{    # Additional headers for calls to access_token_url
                'Authorization': 'Basic Base64EncodedClientIdAndSecret'
            },
            'base_url':'OAUTH_BASE_URL',
            'access_token_url':'OAUTH_BASE_URL/token',
            'authorize_url':'OAUTH_BASE_URL/authorize'
        }
    }
]

# Will allow user self registration, allowing to create Flask users from Authorized User
AUTH_USER_REGISTRATION = True

# The default user self registration role
if os.environ.get("ENVIRONMENT") == "dev":
    AUTH_USER_REGISTRATION_ROLE = "Admin"
if os.environ.get("ENVIRONMENT") == "prod":
    AUTH_USER_REGISTRATION_ROLE = "Material Reader"

from custom_sso_security_manager import CustomSsoSecurityManager
CUSTOM_SECURITY_MANAGER = CustomSsoSecurityManager