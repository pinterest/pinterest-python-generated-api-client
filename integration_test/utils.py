import json
from base64 import b64encode
import random

import urllib3

from integration_test.config import API_URI, DEBUG, LOG_FILE, LOGGER_FORMAT, APP_ID, APP_SECRET, \
    REFRESH_ACCESS_TOKEN, ACCESS_TOKEN
from openapi_generated.pinterest_client import Configuration, ApiClient


# TODO: duplicate from the SDK project, we should create a repo for the integration test for both libraries
def _get_new_access_token(
        app_id: str = APP_ID,
        app_secret: str = APP_SECRET,
        refresh_access_token: str = REFRESH_ACCESS_TOKEN,
        host: str = API_URI,
) -> str:
    """
    Function used to retrieve a new access token for a user using the refresh token.
    Args:
        app_id (str): APP_ID or CLIENT_ID
        app_secret (str): APP_SECRET
        refresh_access_token (str): Refresh access token retrieved from oauth.
        host (str): base url of the host
    Returns:
        str: New access token
    """
    refresh_auth_token = b64encode(
        s=f"{app_id}:{app_secret}".encode()
    ).decode("utf-8")

    headers = {
        'Authorization': f'Basic {refresh_auth_token}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = f'grant_type=refresh_token&refresh_token={refresh_access_token}'

    response = urllib3.PoolManager().request(
        method='POST',
        url=f'{host}/oauth/token',
        headers=headers,
        body=data,
        timeout=5
    )
    assert response.status == 200
    data = json.loads(response.data)

    if not data.get('access_token'):
        raise KeyError(f"`access_token` not found in response body. response={data}." +
                       "Kindly check input arguments or update REFRESH_TOKEN")

    return data.get('access_token')


# TODO: duplicate from the SDK project, we should create a repo for the integration test for both libraries
def get_default_config(
        access_token=ACCESS_TOKEN,
        api_uri=API_URI,
        debug=DEBUG,
        log_file=LOG_FILE,
        logger_format=LOGGER_FORMAT
):
    config = Configuration(
        access_token=get_access_token(access_token),
        host=api_uri,
    )
    config.debug = debug
    config.logger_file = log_file
    config.logger_format = logger_format
    return config


# TODO: duplicate from the SDK project, we should create a repo for the integration test for both libraries
def get_access_token(
        access_token=ACCESS_TOKEN,
        app_id=APP_ID,
        app_secret=APP_SECRET,
        refresh_access_token=REFRESH_ACCESS_TOKEN,
        api_uri=API_URI,
):
    if not access_token:
        return _get_new_access_token(
            app_id=app_id,
            app_secret=app_secret,
            refresh_access_token=refresh_access_token,
            host=api_uri,
        )
    return access_token


def get_default_client(config=get_default_config()):
    return ApiClient(configuration=config)


def get_random_number():
    return random.randint(0, 999)


def parse_to_object(response):
    return response.get('items')[0].get('data')