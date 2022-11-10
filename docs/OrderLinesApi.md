# pinterest.generated.client.OrderLinesApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_lines_get**](OrderLinesApi.md#order_lines_get) | **GET** /ad_accounts/{ad_account_id}/order_lines/{order_line_id} | Get order line
[**order_lines_list**](OrderLinesApi.md#order_lines_list) | **GET** /ad_accounts/{ad_account_id}/order_lines | Get Order Lines


# **order_lines_get**
> OrderLineSingleResponse order_lines_get(ad_account_id, order_line_id)

Get order line

<strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/ads/ads-management/'>Learn more</a>.</strong> <p/> Get a specific existing order line associated with an ad account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import order_lines_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.order_line_single_response import OrderLineSingleResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = order_lines_api.OrderLinesApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    order_line_id = "4" # str | Unique identifier of an order line.

    # example passing only required values which don't have defaults set
    try:
        # Get order line
        api_response = api_instance.order_lines_get(ad_account_id, order_line_id)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling OrderLinesApi->order_lines_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **order_line_id** | **str**| Unique identifier of an order line. |

### Return type

[**OrderLineSingleResponse**](OrderLineSingleResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_lines_list**
> OrderLinesArrayResponse order_lines_list(ad_account_id)

Get Order Lines

<strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/ads/ads-management/'>Learn more</a>.</strong> <p/> List existing order lines associated with an ad account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import order_lines_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.order_lines_array_response import OrderLinesArrayResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = order_lines_api.OrderLinesApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/getting-started/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    order = "ASCENDING" # str | The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. (optional)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Order Lines
        api_response = api_instance.order_lines_list(ad_account_id)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling OrderLinesApi->order_lines_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Order Lines
        api_response = api_instance.order_lines_list(ad_account_id, page_size=page_size, order=order, bookmark=bookmark)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling OrderLinesApi->order_lines_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/getting-started/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **order** | **str**| The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. | [optional]
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]

### Return type

[**OrderLinesArrayResponse**](OrderLinesArrayResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

