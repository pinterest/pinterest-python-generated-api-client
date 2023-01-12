# openapi_generated.pinterest_client.PinsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pins_analytics**](PinsApi.md#pins_analytics) | **GET** /pins/{pin_id}/analytics | Get Pin analytics
[**pins_create**](PinsApi.md#pins_create) | **POST** /pins | Create Pin
[**pins_delete**](PinsApi.md#pins_delete) | **DELETE** /pins/{pin_id} | Delete Pin
[**pins_get**](PinsApi.md#pins_get) | **GET** /pins/{pin_id} | Get Pin
[**pins_save**](PinsApi.md#pins_save) | **POST** /pins/{pin_id}/save | Save Pin


# **pins_analytics**
> AnalyticsResponse pins_analytics(pin_id, start_date, end_date, metric_types)

Get Pin analytics

Get analytics for a Pin owned by the \"operation user_account\" - or on a group board that has been shared with this account. - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href=\"https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list\">List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account:  - For Pins on public or protected boards: Admin, Analyst. - For Pins on secret boards: Admin.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import pins_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.analytics_response import AnalyticsResponse
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
    api_instance = pins_api.PinsApi(api_client)
    pin_id = "pin_id_example" # str | Unique identifier of a Pin.
    start_date = dateutil_parser('1970-01-01').date() # date | Metric report start date (UTC). Format: YYYY-MM-DD
    end_date = dateutil_parser('1970-01-01').date() # date | Metric report end date (UTC). Format: YYYY-MM-DD
    metric_types = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | Pin metric types to get data for, default is all.
    app_types = "ALL" # str | Apps or devices to get data for, default is all. (optional) if omitted the server will use the default value of "ALL"
    split_field = "NO_SPLIT" # str | How to split the data into groups. Not including this param means data won't be split. (optional) if omitted the server will use the default value of "NO_SPLIT"
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Pin analytics
        api_response = api_instance.pins_analytics(pin_id, start_date, end_date, metric_types)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling PinsApi->pins_analytics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Pin analytics
        api_response = api_instance.pins_analytics(pin_id, start_date, end_date, metric_types, app_types=app_types, split_field=split_field, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling PinsApi->pins_analytics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pin_id** | **str**| Unique identifier of a Pin. |
 **start_date** | **date**| Metric report start date (UTC). Format: YYYY-MM-DD |
 **end_date** | **date**| Metric report end date (UTC). Format: YYYY-MM-DD |
 **metric_types** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| Pin metric types to get data for, default is all. |
 **app_types** | **str**| Apps or devices to get data for, default is all. | [optional] if omitted the server will use the default value of "ALL"
 **split_field** | **str**| How to split the data into groups. Not including this param means data won&#39;t be split. | [optional] if omitted the server will use the default value of "NO_SPLIT"
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**AnalyticsResponse**](AnalyticsResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |
**400** | Invalid pins analytics parameters. |  -  |
**403** | Not authorized to access board or Pin. |  -  |
**404** | Pin not found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pins_create**
> Pin pins_create(pin)

Create Pin

Create a Pin on a board or board section owned by the \"operation user_account\".  Note: If the current \"operation user_account\" (defined by the access token) has access to another user's Ad Accounts via Pinterest Business Access, you can modify your request to make use of the current operation_user_account's permissions to those Ad Accounts by including the ad_account_id in the path parameters for the request (e.g. .../?ad_account_id=12345&...).  - This function is intended solely for publishing new content created by the user. If you are interested in saving content created by others to your Pinterest boards, sometimes called 'curated content', please use our <a href='/docs/add-ons/save-button'>Save button</a> instead. For more tips on creating fresh content for Pinterest, review our <a href='/docs/solutions/content-apps'>Content App Solutions Guide</a>.  <strong><a href='/docs/solutions/content-apps/#creatingvideopins'>Learn more</a></strong> about video Pin creation.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import pins_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.pin import Pin
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
    api_instance = pins_api.PinsApi(api_client)
    pin = Pin(
        link="https://www.pinterest.com/",
        title="title_example",
        description="description_example",
        dominant_color="#6E7874",
        alt_text="alt_text_example",
        board_id="4",
        board_section_id="4",
        media_source={},
        parent_pin_id="4",
    ) # Pin | Create a new Pin.

    # example passing only required values which don't have defaults set
    try:
        # Create Pin
        api_response = api_instance.pins_create(pin)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling PinsApi->pins_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pin** | [**Pin**](Pin.md)| Create a new Pin. |

### Return type

[**Pin**](Pin.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful pin creation. |  -  |
**400** | Invalid Pin parameters response |  -  |
**403** | The Pin&#39;s image is too small, too large or is broken |  -  |
**404** | Board or section not found |  -  |
**429** | This request exceeded a rate limit. This can happen if the client exceeds one of the published rate limits or if multiple write operations are applied to an object within a short time window. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pins_delete**
> pins_delete(pin_id)

Delete Pin

Delete a Pins owned by the \"operation user_account\" - or on a group board that has been shared with this account. - By default, the \"operation user_account\" is the token user_account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import pins_api
from openapi_generated.pinterest_client.model.error import Error
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
    api_instance = pins_api.PinsApi(api_client)
    pin_id = "pin_id_example" # str | Unique identifier of a Pin.

    # example passing only required values which don't have defaults set
    try:
        # Delete Pin
        api_instance.pins_delete(pin_id)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling PinsApi->pins_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pin_id** | **str**| Unique identifier of a Pin. |

### Return type

void (empty response body)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted Pin |  -  |
**403** | Not authorized to access board or Pin. |  -  |
**404** | Pin not found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pins_get**
> Pin pins_get(pin_id)

Get Pin

Get a Pin owned by the \"operation user_account\" - or on a group board that has been shared with this account. - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account:  - For Pins on public or protected boards: Owner, Admin, Analyst, Campaign Manager. - For Pins on secret boards: Owner, Admin.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import pins_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.pin import Pin
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
    api_instance = pins_api.PinsApi(api_client)
    pin_id = "pin_id_example" # str | Unique identifier of a Pin.
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Pin
        api_response = api_instance.pins_get(pin_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling PinsApi->pins_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Pin
        api_response = api_instance.pins_get(pin_id, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling PinsApi->pins_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pin_id** | **str**| Unique identifier of a Pin. |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**Pin**](Pin.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |
**403** | Not authorized to access board or Pin. |  -  |
**404** | Pin not found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pins_save**
> Pin pins_save(pin_id, inline_object)

Save Pin

Save a Pin on a board or board section owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account. - Any Pin type can be saved: image Pin, video Pin, Idea Pin, product Pin, etc. - Any public Pin can be saved given a pin ID.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import pins_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.pin import Pin
from openapi_generated.pinterest_client.model.inline_object import InlineObject
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
    api_instance = pins_api.PinsApi(api_client)
    pin_id = "pin_id_example" # str | Unique identifier of a Pin.
    inline_object = InlineObject(
        board_id="4",
        board_section_id="4",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Save Pin
        api_response = api_instance.pins_save(pin_id, inline_object)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling PinsApi->pins_save: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pin_id** | **str**| Unique identifier of a Pin. |
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

[**Pin**](Pin.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully saved pin. |  -  |
**403** | Not authorized to access Board or Pin. |  -  |
**404** | Board or Pin not found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

