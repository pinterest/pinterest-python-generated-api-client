# pinterest.generated.client.AudiencesApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audiences_create**](AudiencesApi.md#audiences_create) | **POST** /ad_accounts/{ad_account_id}/audiences | Create audience
[**audiences_get**](AudiencesApi.md#audiences_get) | **GET** /ad_accounts/{ad_account_id}/audiences/{audience_id} | Get audience
[**audiences_list**](AudiencesApi.md#audiences_list) | **GET** /ad_accounts/{ad_account_id}/audiences | List audiences
[**audiences_update**](AudiencesApi.md#audiences_update) | **PATCH** /ad_accounts/{ad_account_id}/audiences/{audience_id} | Update audience


# **audiences_create**
> Audience audiences_create(ad_account_id, audience_create_request)

Create audience

<strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/features/ads-management/'>Learn more</a>.</strong> <p/> Create an audience you can use in targeting for specific ad groups. Targeting combines customer information with the ways users interact with Pinterest to help you reach specific groups of users; you can include or exclude specific audience_ids when you create an ad group. <p/> For more, see <a class=\"reference external\" href=\"https://help.pinterest.com/en/business/article/audience-targeting\" target=\"_blank\">Audience targeting</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import audiences_api
from pinterest.generated.client.model.audience import Audience
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.audience_create_request import AudienceCreateRequest
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
    api_instance = audiences_api.AudiencesApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    audience_create_request = AudienceCreateRequest() # AudienceCreateRequest | List of ads to create, size limit [1, 30]

    # example passing only required values which don't have defaults set
    try:
        # Create audience
        api_response = api_instance.audiences_create(ad_account_id, audience_create_request)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling AudiencesApi->audiences_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **audience_create_request** | [**AudienceCreateRequest**](AudienceCreateRequest.md)| List of ads to create, size limit [1, 30] |

### Return type

[**Audience**](Audience.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_get**
> Audience audiences_get(ad_account_id, audience_id)

Get audience

<strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/features/ads-management/'>Learn more</a>.</strong> <p/> Get a specific audience given the audience ID.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import audiences_api
from pinterest.generated.client.model.audience import Audience
from pinterest.generated.client.model.error import Error
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
    api_instance = audiences_api.AudiencesApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    audience_id = "4" # str | Unique identifier of an audience

    # example passing only required values which don't have defaults set
    try:
        # Get audience
        api_response = api_instance.audiences_get(ad_account_id, audience_id)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling AudiencesApi->audiences_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **audience_id** | **str**| Unique identifier of an audience |

### Return type

[**Audience**](Audience.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Audience not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_list**
> bool, date, datetime, dict, float, int, list, str, none_type audiences_list(ad_account_id)

List audiences

<strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/features/ads-management/'>Learn more</a>.</strong> <p/> Get list of audiences for the ad account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import audiences_api
from pinterest.generated.client.model.paginated import Paginated
from pinterest.generated.client.model.get_audiences_order_by import GetAudiencesOrderBy
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.audience_type import AudienceType
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
    api_instance = audiences_api.AudiencesApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    audience_ids = [
        "4",
    ] # [str] | List of audience ids to use to filter the results. (optional)
    audience_type = "4" # str | The type of audience to filter for. (optional)
    audience_types = [
        AudienceType("ACTALIKE"),
    ] # [AudienceType] | The types of audience to filter for. (optional)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    entity_statuses = [
        "ACTIVE",
    ] # [str] | Entity status (optional)
    flatten_rule = True # bool | Uniform the format of Audiences rules for presentation on Web UI. (optional)
    order = "ASCENDING" # str | The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. (optional)
    order_by = GetAudiencesOrderBy("NAME") # GetAudiencesOrderBy | The audience field to order results by. (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/getting-started/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    search_query = "search_query_example" # str | String keywords to search for audiences by. (optional)
    start_index = "4" # str | he starting index for returned list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List audiences
        api_response = api_instance.audiences_list(ad_account_id)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling AudiencesApi->audiences_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List audiences
        api_response = api_instance.audiences_list(ad_account_id, audience_ids=audience_ids, audience_type=audience_type, audience_types=audience_types, bookmark=bookmark, entity_statuses=entity_statuses, flatten_rule=flatten_rule, order=order, order_by=order_by, page_size=page_size, search_query=search_query, start_index=start_index)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling AudiencesApi->audiences_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **audience_ids** | **[str]**| List of audience ids to use to filter the results. | [optional]
 **audience_type** | **str**| The type of audience to filter for. | [optional]
 **audience_types** | [**[AudienceType]**](AudienceType.md)| The types of audience to filter for. | [optional]
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **entity_statuses** | **[str]**| Entity status | [optional]
 **flatten_rule** | **bool**| Uniform the format of Audiences rules for presentation on Web UI. | [optional]
 **order** | **str**| The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. | [optional]
 **order_by** | **GetAudiencesOrderBy**| The audience field to order results by. | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/getting-started/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **search_query** | **str**| String keywords to search for audiences by. | [optional]
 **start_index** | **str**| he starting index for returned list. | [optional]

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
**400** | Invalid ad account audience parameters. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audiences_update**
> Audience audiences_update(ad_account_id, audience_id)

Update audience

<strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/features/ads-management/'>Learn more</a>.</strong> <p/> Update (edit or remove) an existing targeting audience.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import audiences_api
from pinterest.generated.client.model.audience import Audience
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.audience_update_request import AudienceUpdateRequest
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
    api_instance = audiences_api.AudiencesApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    audience_id = "4" # str | Unique identifier of an audience
    audience_update_request = AudienceUpdateRequest(None) # AudienceUpdateRequest | The audience to be updated. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update audience
        api_response = api_instance.audiences_update(ad_account_id, audience_id)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling AudiencesApi->audiences_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update audience
        api_response = api_instance.audiences_update(ad_account_id, audience_id, audience_update_request=audience_update_request)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling AudiencesApi->audiences_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **audience_id** | **str**| Unique identifier of an audience |
 **audience_update_request** | [**AudienceUpdateRequest**](AudienceUpdateRequest.md)| The audience to be updated. | [optional]

### Return type

[**Audience**](Audience.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

