"""
Pinterest config
"""
import json
import os as _os
from dotenv import load_dotenv as _load

_load()

JSON_ENV_VARIABLES = _os.environ.get('PINTEREST_JSON_ENV_VARIABLES', None)

if JSON_ENV_VARIABLES is not None:
    config_json = json.loads(JSON_ENV_VARIABLES)
    for attribute, value in config_json.items():
        _os.environ[attribute] = str(value)

OWNER_USER_ID = _os.environ.get('OWNER_USER_ID', '1072068023705238984')
DEFAULT_AD_ACCOUNT_ID = _os.environ.get('DEFAULT_AD_ACCOUNT_ID', '549764334122')
DEFAULT_AD_ACCOUNT_NAME = _os.environ.get('DEFAULT_AD_ACCOUNT_NAME', 'SDK Test Ad Account')
DEFAULT_AD_ACCOUNT_COUNTRY = _os.environ.get('DEFAULT_AD_ACCOUNT_COUNTRY', 'US')
DEFAULT_BOARD_ID = _os.environ.get('DEFAULT_BOARD_ID', '1072067954986053849')
DEBUG = _os.environ.get('PINTEREST_DEBUG', True)
PORT = _os.environ.get('PORT', 0)
APP_ID = _os.environ.get('PINTEREST_APP_ID', None)
APP_SECRET = _os.environ.get('PINTEREST_APP_SECRET', None)
CLIENT_ID = _os.environ.get('CLIENT_ID', None)
REDIRECT_URI = _os.environ.get('REDIRECT_URI', 'http://localhost')
RESPONSE_TYPE = _os.environ.get('RESPONSE_TYPE', 'code')
SCOPE = _os.environ.get('SCOPE', None)
STATE = _os.environ.get('STATE', 'dev')
ACCESS_TOKEN_JSON_PATH = _os.environ.get('ACCESS_TOKEN_JSON_PATH', '')
ACCESS_TOKEN = _os.environ.get('ACCESS_TOKEN', None)
REFRESH_ACCESS_TOKEN = _os.environ.get('PINTEREST_REFRESH_ACCESS_TOKEN', None)
API_URI = _os.environ.get('PINTEREST_API_URI', 'https://api-latest.pinterest.com/v5')
LOG_FILE = _os.environ.get('LOG_FILE', './http_logs.txt')
DISABLED_CLIENT_SIDE_VALIDATIONS = _os.environ.get('DISABLED_CLIENT_SIDE_VALIDATIONS', False)
LOGGER_FORMAT = _os.environ.get('LOGGER_FORMAT', '%(asctime)s %(levelname)s %(message)s')