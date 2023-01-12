# openapi_generated.pinterest_client.OauthApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_token**](OauthApi.md#oauth_token) | **POST** /oauth/token | Generate OAuth access token


# **oauth_token**
> OauthAccessTokenResponse oauth_token(grant_type)

Generate OAuth access token

Generate an OAuth access token by using an authorization code or a refresh token.  IMPORTANT: You need to start the OAuth flow via www.pinterest.com/oauth before calling this endpoint (or have an existing refresh token).  See <a href='/docs/getting-started/authentication/'>Authentication</a> for more.

### Example

* Basic Authentication (basic):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import oauth_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.oauth_access_token_response import OauthAccessTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = openapi_generated.pinterest_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oauth_api.OauthApi(api_client)
    grant_type = "authorization_code" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Generate OAuth access token
        api_response = api_instance.oauth_token(grant_type)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling OauthApi->oauth_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  |

### Return type

[**OauthAccessTokenResponse**](OauthAccessTokenResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

