# openapi_generated.pinterest_client.SearchApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_partner_pins**](SearchApi.md#search_partner_pins) | **GET** /search/partner/pins | Search pins by a given search term
[**search_user_boards_get**](SearchApi.md#search_user_boards_get) | **GET** /search/boards | Search user&#39;s boards
[**search_user_pins_list**](SearchApi.md#search_user_pins_list) | **GET** /search/pins | Search user&#39;s Pins


# **search_partner_pins**
> bool, date, datetime, dict, float, int, list, str, none_type search_partner_pins(term, country_code)

Search pins by a given search term

<strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.</strong>  Get the top 10 Pins by a given search term.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import search_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.summary_pin import SummaryPin
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

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    term = "term_example" # str | Search term to look up pins.
    country_code = "US" # str | Two letter country code (ISO 3166-1 alpha-2)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    locale = "locale_example" # str | Search locale. (optional)
    limit = 4 # int | Max search result size (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Search pins by a given search term
        api_response = api_instance.search_partner_pins(term, country_code)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling SearchApi->search_partner_pins: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search pins by a given search term
        api_response = api_instance.search_partner_pins(term, country_code, bookmark=bookmark, locale=locale, limit=limit)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling SearchApi->search_partner_pins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| Search term to look up pins. |
 **country_code** | **str**| Two letter country code (ISO 3166-1 alpha-2) |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **locale** | **str**| Search locale. | [optional]
 **limit** | **int**| Max search result size | [optional] if omitted the server will use the default value of 10

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid pins |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_boards_get**
> bool, date, datetime, dict, float, int, list, str, none_type search_user_boards_get()

Search user's boards

Search for boards for the \"operation user_account\". This includes boards of all board types. - By default, the \"operation user_account\" is the token user_account.  If using Business Access: Specify an ad_account_id to use the owner of that ad_account as the \"operation user_account\". See <a href='/docs/getting-started/using-business-access/'>Understanding Business Access</a> for more information.

### Example

* OAuth Authentication (client_credentials):
* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import search_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.board import Board
from openapi_generated.pinterest_client.model.paginated import Paginated
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

# Configure OAuth2 access token for authorization: client_credentials
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    query = "query_example" # str | Search query. Can contain pin description keywords or comma-separated pin IDs. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search user's boards
        api_response = api_instance.search_user_boards_get(ad_account_id=ad_account_id, bookmark=bookmark, page_size=page_size, query=query)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling SearchApi->search_user_boards_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **query** | **str**| Search query. Can contain pin description keywords or comma-separated pin IDs. | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[client_credentials](../README.md#client_credentials), [pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_pins_list**
> bool, date, datetime, dict, float, int, list, str, none_type search_user_pins_list(query)

Search user's Pins

Search for pins for the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  If using Business Access: Specify an ad_account_id to use the owner of that ad_account as the \"operation user_account\". See <a href='/docs/getting-started/using-business-access/'>Understanding Business Access</a> for more information.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import search_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.pin import Pin
from openapi_generated.pinterest_client.model.paginated import Paginated
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

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    query = "Plants" # str | Search query. Can contain pin description keywords or comma-separated pin IDs.
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search user's Pins
        api_response = api_instance.search_user_pins_list(query)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling SearchApi->search_user_pins_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search user's Pins
        api_response = api_instance.search_user_pins_list(query, ad_account_id=ad_account_id, bookmark=bookmark)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling SearchApi->search_user_pins_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query. Can contain pin description keywords or comma-separated pin IDs. |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | User not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

