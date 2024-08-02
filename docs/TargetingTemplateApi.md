# openapi_generated.pinterest_client.TargetingTemplateApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**targeting_template_create**](TargetingTemplateApi.md#targeting_template_create) | **POST** /ad_accounts/{ad_account_id}/targeting_templates | Create targeting templates
[**targeting_template_list**](TargetingTemplateApi.md#targeting_template_list) | **GET** /ad_accounts/{ad_account_id}/targeting_templates | List targeting templates
[**targeting_template_update**](TargetingTemplateApi.md#targeting_template_update) | **PATCH** /ad_accounts/{ad_account_id}/targeting_templates | Update targeting templates


# **targeting_template_create**
> TargetingTemplateGetResponseData targeting_template_create(ad_account_id, targeting_template_create)

Create targeting templates

<p>Targeting templates allow advertisers to save a set of targeting details including audience lists,  keywords & interest, demographics, and placements to use more than once during the campaign creation process.</p>  <p>Templates can be used to build out basic targeting criteria that you plan to use across campaigns and to reuse   performance targeting from prior campaigns for new campaigns.</p>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import targeting_template_api
from openapi_generated.pinterest_client.model.targeting_template_get_response_data import TargetingTemplateGetResponseData
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.targeting_template_create import TargetingTemplateCreate
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
    api_instance = targeting_template_api.TargetingTemplateApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    targeting_template_create = TargetingTemplateCreate() # TargetingTemplateCreate | targeting template creation entity

    # example passing only required values which don't have defaults set
    try:
        # Create targeting templates
        api_response = api_instance.targeting_template_create(ad_account_id, targeting_template_create)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling TargetingTemplateApi->targeting_template_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **targeting_template_create** | [**TargetingTemplateCreate**](TargetingTemplateCreate.md)| targeting template creation entity |

### Return type

[**TargetingTemplateGetResponseData**](TargetingTemplateGetResponseData.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid ad account id. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targeting_template_list**
> bool, date, datetime, dict, float, int, list, str, none_type targeting_template_list(ad_account_id)

List targeting templates

Get a list of the targeting templates in the specified <code>ad_account_id</code>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import targeting_template_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.targeting_template_response_data import TargetingTemplateResponseData
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
    api_instance = targeting_template_api.TargetingTemplateApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    order = "ASCENDING" # str | The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. (optional)
    include_sizing = False # bool | Include audience sizing in result or not (optional) if omitted the server will use the default value of False
    search_query = "gaming" # str | Search keyword for targeting templates (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    try:
        # List targeting templates
        api_response = api_instance.targeting_template_list(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling TargetingTemplateApi->targeting_template_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List targeting templates
        api_response = api_instance.targeting_template_list(ad_account_id, order=order, include_sizing=include_sizing, search_query=search_query, page_size=page_size, bookmark=bookmark)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling TargetingTemplateApi->targeting_template_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **order** | **str**| The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. | [optional]
 **include_sizing** | **bool**| Include audience sizing in result or not | [optional] if omitted the server will use the default value of False
 **search_query** | **str**| Search keyword for targeting templates | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
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
**400** | Invalid ad account id. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targeting_template_update**
> targeting_template_update(ad_account_id, targeting_template_update_request)

Update targeting templates

<p>Update the targeting template given advertiser ID and targeting template ID</p>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import targeting_template_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.targeting_template_update_request import TargetingTemplateUpdateRequest
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
    api_instance = targeting_template_api.TargetingTemplateApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    targeting_template_update_request = TargetingTemplateUpdateRequest(
        operation_type="REMOVE",
        id="643",
    ) # TargetingTemplateUpdateRequest | Operation type and targeting template ID

    # example passing only required values which don't have defaults set
    try:
        # Update targeting templates
        api_instance.targeting_template_update(ad_account_id, targeting_template_update_request)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling TargetingTemplateApi->targeting_template_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **targeting_template_update_request** | [**TargetingTemplateUpdateRequest**](TargetingTemplateUpdateRequest.md)| Operation type and targeting template ID |

### Return type

void (empty response body)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid ad account id. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

