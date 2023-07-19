# openapi_generated.pinterest_client.ProductGroupsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ad_accounts_catalogs_product_groups_list**](ProductGroupsApi.md#ad_accounts_catalogs_product_groups_list) | **GET** /ad_accounts/{ad_account_id}/product_groups/catalogs | Get catalog product groups


# **ad_accounts_catalogs_product_groups_list**
> bool, date, datetime, dict, float, int, list, str, none_type ad_accounts_catalogs_product_groups_list(ad_account_id)

Get catalog product groups

This endpoint is completely deprecated. Please use <a href='/docs/api/v5/#operation/catalogs_product_groups/list'>List product groups</a> from Catalogs API instead.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import product_groups_api
from openapi_generated.pinterest_client.model.error import Error
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
    api_instance = product_groups_api.ProductGroupsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    feed_profile_id = "4" # str | The feed profile id whose catalog product groups we want to return. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get catalog product groups
        api_response = api_instance.ad_accounts_catalogs_product_groups_list(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ProductGroupsApi->ad_accounts_catalogs_product_groups_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get catalog product groups
        api_response = api_instance.ad_accounts_catalogs_product_groups_list(ad_account_id, feed_profile_id=feed_profile_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ProductGroupsApi->ad_accounts_catalogs_product_groups_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **feed_profile_id** | **str**| The feed profile id whose catalog product groups we want to return. | [optional]

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
**400** | Invalid ad account ads parameters. |  -  |
**401** | Access Denied. This can happen if account is not yet approved to operate as Merchant on Pinterest. |  -  |
**404** | Merchant data not found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

