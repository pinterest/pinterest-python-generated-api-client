# openapi_generated.pinterest_client.UserAccountApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_account_analytics**](UserAccountApi.md#user_account_analytics) | **GET** /user_account/analytics | Get user account analytics
[**user_account_analytics_top_pins**](UserAccountApi.md#user_account_analytics_top_pins) | **GET** /user_account/analytics/top_pins | Get user account top pins analytics
[**user_account_analytics_top_video_pins**](UserAccountApi.md#user_account_analytics_top_video_pins) | **GET** /user_account/analytics/top_video_pins | Get user account top video pins analytics
[**user_account_get**](UserAccountApi.md#user_account_get) | **GET** /user_account | Get user account


# **user_account_analytics**
> AnalyticsResponse user_account_analytics(start_date, end_date)

Get user account analytics

Get analytics for the \"operation user_account\" - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an ad_account_id to use the owner of that ad_account as the \"operation user_account\".

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import user_account_api
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
    api_instance = user_account_api.UserAccountApi(api_client)
    start_date = dateutil_parser('1970-01-01').date() # date | Metric report start date (UTC). Format: YYYY-MM-DD
    end_date = dateutil_parser('1970-01-01').date() # date | Metric report end date (UTC). Format: YYYY-MM-DD
    from_claimed_content = "BOTH" # str | Filter on Pins that match your claimed domain. (optional) if omitted the server will use the default value of "BOTH"
    pin_format = "ALL" # str | Pin formats to get data for, default is all. (optional) if omitted the server will use the default value of "ALL"
    app_types = "ALL" # str | Apps or devices to get data for, default is all. (optional) if omitted the server will use the default value of "ALL"
    metric_types = [
        "ENGAGEMENT",
    ] # [str] | Metric types to get data for, default is all.  (optional)
    split_field = "NO_SPLIT" # str | How to split the data into groups. Not including this param means data won't be split. (optional) if omitted the server will use the default value of "NO_SPLIT"
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get user account analytics
        api_response = api_instance.user_account_analytics(start_date, end_date)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling UserAccountApi->user_account_analytics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get user account analytics
        api_response = api_instance.user_account_analytics(start_date, end_date, from_claimed_content=from_claimed_content, pin_format=pin_format, app_types=app_types, metric_types=metric_types, split_field=split_field, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling UserAccountApi->user_account_analytics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Metric report start date (UTC). Format: YYYY-MM-DD |
 **end_date** | **date**| Metric report end date (UTC). Format: YYYY-MM-DD |
 **from_claimed_content** | **str**| Filter on Pins that match your claimed domain. | [optional] if omitted the server will use the default value of "BOTH"
 **pin_format** | **str**| Pin formats to get data for, default is all. | [optional] if omitted the server will use the default value of "ALL"
 **app_types** | **str**| Apps or devices to get data for, default is all. | [optional] if omitted the server will use the default value of "ALL"
 **metric_types** | **[str]**| Metric types to get data for, default is all.  | [optional]
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
**200** | Success |  -  |
**400** | Invalid user accounts analytics parameters. |  -  |
**403** | Not authorized to access the user account analytics. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_analytics_top_pins**
> TopPinsAnalyticsResponse user_account_analytics_top_pins(start_date, end_date, sort_by)

Get user account top pins analytics

Gets analytics data about a user's top pins (limited to the top 50). - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an ad_account_id to use the owner of that ad_account as the \"operation user_account\".

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import user_account_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.top_pins_analytics_response import TopPinsAnalyticsResponse
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
    api_instance = user_account_api.UserAccountApi(api_client)
    start_date = dateutil_parser('1970-01-01').date() # date | Metric report start date (UTC). Format: YYYY-MM-DD
    end_date = dateutil_parser('1970-01-01').date() # date | Metric report end date (UTC). Format: YYYY-MM-DD
    sort_by = "ENGAGEMENT" # str | Specify sorting order for metrics
    from_claimed_content = "BOTH" # str | Filter on Pins that match your claimed domain. (optional) if omitted the server will use the default value of "BOTH"
    pin_format = "ALL" # str | Pin formats to get data for, default is all. (optional) if omitted the server will use the default value of "ALL"
    app_types = "ALL" # str | Apps or devices to get data for, default is all. (optional) if omitted the server will use the default value of "ALL"
    metric_types = [
        "ENGAGEMENT",
    ] # [str] | Metric types to get data for, default is all.  (optional)
    num_of_pins = 25 # int | Number of pins to include, default is 10. Max is 50. (optional) if omitted the server will use the default value of 10
    created_in_last_n_days = 30 # int | Get metrics for pins created in the last \"n\" days. (optional) if omitted the server will use the default value of 30
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get user account top pins analytics
        api_response = api_instance.user_account_analytics_top_pins(start_date, end_date, sort_by)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling UserAccountApi->user_account_analytics_top_pins: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get user account top pins analytics
        api_response = api_instance.user_account_analytics_top_pins(start_date, end_date, sort_by, from_claimed_content=from_claimed_content, pin_format=pin_format, app_types=app_types, metric_types=metric_types, num_of_pins=num_of_pins, created_in_last_n_days=created_in_last_n_days, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling UserAccountApi->user_account_analytics_top_pins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Metric report start date (UTC). Format: YYYY-MM-DD |
 **end_date** | **date**| Metric report end date (UTC). Format: YYYY-MM-DD |
 **sort_by** | **str**| Specify sorting order for metrics |
 **from_claimed_content** | **str**| Filter on Pins that match your claimed domain. | [optional] if omitted the server will use the default value of "BOTH"
 **pin_format** | **str**| Pin formats to get data for, default is all. | [optional] if omitted the server will use the default value of "ALL"
 **app_types** | **str**| Apps or devices to get data for, default is all. | [optional] if omitted the server will use the default value of "ALL"
 **metric_types** | **[str]**| Metric types to get data for, default is all.  | [optional]
 **num_of_pins** | **int**| Number of pins to include, default is 10. Max is 50. | [optional] if omitted the server will use the default value of 10
 **created_in_last_n_days** | **int**| Get metrics for pins created in the last \&quot;n\&quot; days. | [optional] if omitted the server will use the default value of 30
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**TopPinsAnalyticsResponse**](TopPinsAnalyticsResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Not authorized to access the user account analytics. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_analytics_top_video_pins**
> TopVideoPinsAnalyticsResponse user_account_analytics_top_video_pins(start_date, end_date, sort_by)

Get user account top video pins analytics

Gets analytics data about a user's top video pins (limited to the top 50). - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an ad_account_id to use the owner of that ad_account as the \"operation user_account\".

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import user_account_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.top_video_pins_analytics_response import TopVideoPinsAnalyticsResponse
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
    api_instance = user_account_api.UserAccountApi(api_client)
    start_date = dateutil_parser('1970-01-01').date() # date | Metric report start date (UTC). Format: YYYY-MM-DD
    end_date = dateutil_parser('1970-01-01').date() # date | Metric report end date (UTC). Format: YYYY-MM-DD
    sort_by = "IMPRESSION" # str | Specify sorting order for video metrics
    from_claimed_content = "BOTH" # str | Filter on Pins that match your claimed domain. (optional) if omitted the server will use the default value of "BOTH"
    pin_format = "ALL" # str | Pin formats to get data for, default is all. (optional) if omitted the server will use the default value of "ALL"
    app_types = "ALL" # str | Apps or devices to get data for, default is all. (optional) if omitted the server will use the default value of "ALL"
    metric_types = [
        "IMPRESSION",
    ] # [str] | Metric types to get video data for, default is all.  (optional)
    num_of_pins = 25 # int | Number of pins to include, default is 10. Max is 50. (optional) if omitted the server will use the default value of 10
    created_in_last_n_days = 30 # int | Get metrics for pins created in the last \"n\" days. (optional) if omitted the server will use the default value of 30
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get user account top video pins analytics
        api_response = api_instance.user_account_analytics_top_video_pins(start_date, end_date, sort_by)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling UserAccountApi->user_account_analytics_top_video_pins: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get user account top video pins analytics
        api_response = api_instance.user_account_analytics_top_video_pins(start_date, end_date, sort_by, from_claimed_content=from_claimed_content, pin_format=pin_format, app_types=app_types, metric_types=metric_types, num_of_pins=num_of_pins, created_in_last_n_days=created_in_last_n_days, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling UserAccountApi->user_account_analytics_top_video_pins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Metric report start date (UTC). Format: YYYY-MM-DD |
 **end_date** | **date**| Metric report end date (UTC). Format: YYYY-MM-DD |
 **sort_by** | **str**| Specify sorting order for video metrics |
 **from_claimed_content** | **str**| Filter on Pins that match your claimed domain. | [optional] if omitted the server will use the default value of "BOTH"
 **pin_format** | **str**| Pin formats to get data for, default is all. | [optional] if omitted the server will use the default value of "ALL"
 **app_types** | **str**| Apps or devices to get data for, default is all. | [optional] if omitted the server will use the default value of "ALL"
 **metric_types** | **[str]**| Metric types to get video data for, default is all.  | [optional]
 **num_of_pins** | **int**| Number of pins to include, default is 10. Max is 50. | [optional] if omitted the server will use the default value of 10
 **created_in_last_n_days** | **int**| Get metrics for pins created in the last \&quot;n\&quot; days. | [optional] if omitted the server will use the default value of 30
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**TopVideoPinsAnalyticsResponse**](TopVideoPinsAnalyticsResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Not authorized to access the user account analytics. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_account_get**
> Account user_account_get()

Get user account

Get account information for the \"operation user_account\" - By default, the \"operation user_account\" is the token user_account.  If using Business Access: Specify an ad_account_id to use the owner of that ad_account as the \"operation user_account\". See <a href='/docs/reference/business-access/'>Understanding Business Access</a> for more information.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import user_account_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.account import Account
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
    api_instance = user_account_api.UserAccountApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get user account
        api_response = api_instance.user_account_get(ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling UserAccountApi->user_account_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**Account**](Account.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |
**403** | Not authorized to access the user account. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

