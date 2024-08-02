# openapi_generated.pinterest_client.CatalogsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogs_create**](CatalogsApi.md#catalogs_create) | **POST** /catalogs | Create catalog
[**catalogs_list**](CatalogsApi.md#catalogs_list) | **GET** /catalogs | List catalogs
[**catalogs_product_group_pins_list**](CatalogsApi.md#catalogs_product_group_pins_list) | **GET** /catalogs/product_groups/{product_group_id}/products | List products by product group
[**catalogs_product_groups_create**](CatalogsApi.md#catalogs_product_groups_create) | **POST** /catalogs/product_groups | Create product group
[**catalogs_product_groups_create_many**](CatalogsApi.md#catalogs_product_groups_create_many) | **POST** /catalogs/product_groups/multiple | Create product groups
[**catalogs_product_groups_delete**](CatalogsApi.md#catalogs_product_groups_delete) | **DELETE** /catalogs/product_groups/{product_group_id} | Delete product group
[**catalogs_product_groups_delete_many**](CatalogsApi.md#catalogs_product_groups_delete_many) | **DELETE** /catalogs/product_groups/multiple | Delete product groups
[**catalogs_product_groups_get**](CatalogsApi.md#catalogs_product_groups_get) | **GET** /catalogs/product_groups/{product_group_id} | Get product group
[**catalogs_product_groups_list**](CatalogsApi.md#catalogs_product_groups_list) | **GET** /catalogs/product_groups | List product groups
[**catalogs_product_groups_product_counts_get**](CatalogsApi.md#catalogs_product_groups_product_counts_get) | **GET** /catalogs/product_groups/{product_group_id}/product_counts | Get product counts
[**catalogs_product_groups_update**](CatalogsApi.md#catalogs_product_groups_update) | **PATCH** /catalogs/product_groups/{product_group_id} | Update single product group
[**feed_processing_results_list**](CatalogsApi.md#feed_processing_results_list) | **GET** /catalogs/feeds/{feed_id}/processing_results | List feed processing results
[**feeds_create**](CatalogsApi.md#feeds_create) | **POST** /catalogs/feeds | Create feed
[**feeds_delete**](CatalogsApi.md#feeds_delete) | **DELETE** /catalogs/feeds/{feed_id} | Delete feed
[**feeds_get**](CatalogsApi.md#feeds_get) | **GET** /catalogs/feeds/{feed_id} | Get feed
[**feeds_ingest**](CatalogsApi.md#feeds_ingest) | **POST** /catalogs/feeds/{feed_id}/ingest | Ingest feed items
[**feeds_list**](CatalogsApi.md#feeds_list) | **GET** /catalogs/feeds | List feeds
[**feeds_update**](CatalogsApi.md#feeds_update) | **PATCH** /catalogs/feeds/{feed_id} | Update feed
[**items_batch_get**](CatalogsApi.md#items_batch_get) | **GET** /catalogs/items/batch/{batch_id} | Get item batch status
[**items_batch_post**](CatalogsApi.md#items_batch_post) | **POST** /catalogs/items/batch | Operate on item batch
[**items_get**](CatalogsApi.md#items_get) | **GET** /catalogs/items | Get catalogs items
[**items_issues_list**](CatalogsApi.md#items_issues_list) | **GET** /catalogs/processing_results/{processing_result_id}/item_issues | List item issues
[**items_post**](CatalogsApi.md#items_post) | **POST** /catalogs/items | Get catalogs items (POST)
[**products_by_product_group_filter_list**](CatalogsApi.md#products_by_product_group_filter_list) | **POST** /catalogs/products/get_by_product_group_filters | List products by filter
[**reports_create**](CatalogsApi.md#reports_create) | **POST** /catalogs/reports | Build catalogs report
[**reports_get**](CatalogsApi.md#reports_get) | **GET** /catalogs/reports | Get catalogs report
[**reports_stats**](CatalogsApi.md#reports_stats) | **GET** /catalogs/reports/stats | List report stats


# **catalogs_create**
> Catalog catalogs_create(catalogs_create_request)

Create catalog

Create a new catalog owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>  Note: this API only supports the catalog type of HOTEL for now.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_create_request import CatalogsCreateRequest
from openapi_generated.pinterest_client.model.catalog import Catalog
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    catalogs_create_request = CatalogsCreateRequest(
        catalog_type="HOTEL",
        name="name_example",
    ) # CatalogsCreateRequest | Request object used to created a feed.
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create catalog
        api_response = api_instance.catalogs_create(catalogs_create_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create catalog
        api_response = api_instance.catalogs_create(catalogs_create_request, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalogs_create_request** | [**CatalogsCreateRequest**](CatalogsCreateRequest.md)| Request object used to created a feed. |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**Catalog**](Catalog.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid parameters. |  -  |
**401** | Unauthorized access. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_list**
> bool, date, datetime, dict, float, int, list, str, none_type catalogs_list()

List catalogs

Fetch catalogs owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.catalog import Catalog
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List catalogs
        api_response = api_instance.catalogs_list(bookmark=bookmark, page_size=page_size, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

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
**400** | Invalid parameters. |  -  |
**401** | Unauthorized access. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_product_group_pins_list**
> bool, date, datetime, dict, float, int, list, str, none_type catalogs_product_group_pins_list(product_group_id)

List products by product group

Get a list of product pins for a given Catalogs Product Group Id owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_product import CatalogsProduct
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    product_group_id = "4" # str | Unique identifier of a product group
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)
    pin_metrics = False # bool | Specify whether to return 90d and lifetime Pin metrics. Total comments and total reactions are only available with lifetime Pin metrics. If Pin was created before <code>2023-03-20</code> lifetime metrics will only be available for Video and Idea Pin formats. Lifetime metrics are available for all Pin formats since then. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # List products by product group
        api_response = api_instance.catalogs_product_group_pins_list(product_group_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_group_pins_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List products by product group
        api_response = api_instance.catalogs_product_group_pins_list(product_group_id, bookmark=bookmark, page_size=page_size, ad_account_id=ad_account_id, pin_metrics=pin_metrics)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_group_pins_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_group_id** | **str**| Unique identifier of a product group |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]
 **pin_metrics** | **bool**| Specify whether to return 90d and lifetime Pin metrics. Total comments and total reactions are only available with lifetime Pin metrics. If Pin was created before &lt;code&gt;2023-03-20&lt;/code&gt; lifetime metrics will only be available for Video and Idea Pin formats. Lifetime metrics are available for all Pin formats since then. | [optional] if omitted the server will use the default value of False

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
**400** | Invalid parameters. |  -  |
**401** | Unauthorized access. |  -  |
**404** | Catalogs product group not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_product_groups_create**
> CatalogsVerticalProductGroup catalogs_product_groups_create(unknown_base_type)

Create product group

Create product group to use in Catalogs owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>  Note: Access to the Creative Assets catalog type is restricted to a specific group of users. If you require access, please reach out to your partner manager.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_product_group_create_request import CatalogsProductGroupCreateRequest
from openapi_generated.pinterest_client.model.catalogs_vertical_product_group_create_request import CatalogsVerticalProductGroupCreateRequest
from openapi_generated.pinterest_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_generated.pinterest_client.model.catalogs_vertical_product_group import CatalogsVerticalProductGroup
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE | Request object used to create a single catalogs product groups.
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create product group
        api_response = api_instance.catalogs_product_groups_create(unknown_base_type)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create product group
        api_response = api_instance.catalogs_product_groups_create(unknown_base_type, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Request object used to create a single catalogs product groups. |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsVerticalProductGroup**](CatalogsVerticalProductGroup.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Invalid body. |  -  |
**401** | Unauthorized access. |  -  |
**403** | Forbidden. Account not approved for catalog product group mutations yet. |  -  |
**409** | Conflict. Can&#39;t create this catalogs product group with this value. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_product_groups_create_many**
> [str] catalogs_product_groups_create_many(request_body)

Create product groups

Create product group to use in Catalogs owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>  Note: Access to the Creative Assets catalog type is restricted to a specific group of users. If you require access, please reach out to your partner manager.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_product_group_create_request import CatalogsProductGroupCreateRequest
from openapi_generated.pinterest_client.model.catalogs_vertical_product_group_create_request import CatalogsVerticalProductGroupCreateRequest
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    request_body = [{"name":"Few Filters using \"all_of\"","feed_id":"2680059592705","filters":{"all_of":[{"MIN_PRICE":{"values":999.99,"inclusion":true}},{"CURRENCY":{"values":"USD"}},{"CUSTOM_LABEL_0":{"values":["Luxury Items"]}}]}}] # [bool, date, datetime, dict, float, int, list, str, none_type] | Request object used to create one or more catalogs product groups.
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create product groups
        api_response = api_instance.catalogs_product_groups_create_many(request_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_create_many: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create product groups
        api_response = api_instance.catalogs_product_groups_create_many(request_body, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_create_many: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[bool, date, datetime, dict, float, int, list, str, none_type]**| Request object used to create one or more catalogs product groups. |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

**[str]**

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Invalid body. |  -  |
**401** | Unauthorized access. |  -  |
**403** | Forbidden. Account not approved for catalog product group mutations yet. |  -  |
**409** | Conflict. Can&#39;t create this catalogs product group with this value. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_product_groups_delete**
> catalogs_product_groups_delete(product_group_id)

Delete product group

Delete a product group owned by the \"operation user_account\" from being in use in Catalogs. - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    product_group_id = "4" # str | Unique identifier of a product group
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete product group
        api_instance.catalogs_product_groups_delete(product_group_id)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete product group
        api_instance.catalogs_product_groups_delete(product_group_id, ad_account_id=ad_account_id)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_group_id** | **str**| Unique identifier of a product group |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

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
**204** | Catalogs Product Group deleted successfully. |  -  |
**400** | Invalid catalogs product group id parameters. |  -  |
**401** | Unauthorized access. |  -  |
**403** | Forbidden. Account not approved for catalog product group mutations yet. |  -  |
**404** | Catalogs product group not found. |  -  |
**409** | Conflict. Can&#39;t delete this catalogs product group. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_product_groups_delete_many**
> catalogs_product_groups_delete_many(id)

Delete product groups

Delete product groups owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    id = [
        1,
    ] # [int] | Comma-separated list of product group ids
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete product groups
        api_instance.catalogs_product_groups_delete_many(id)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_delete_many: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete product groups
        api_instance.catalogs_product_groups_delete_many(id, ad_account_id=ad_account_id)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_delete_many: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **[int]**| Comma-separated list of product group ids |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

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
**204** | Catalogs Product Groups deleted successfully. |  -  |
**401** | Unauthorized access. |  -  |
**403** | Forbidden. Account not approved for catalog product group mutations yet. |  -  |
**404** | Catalogs product group not found. |  -  |
**409** | Conflict. Can&#39;t delete this catalogs product group. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_product_groups_get**
> CatalogsVerticalProductGroup catalogs_product_groups_get(product_group_id)

Get product group

Get a singe product group for a given Catalogs Product Group Id owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_vertical_product_group import CatalogsVerticalProductGroup
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    product_group_id = "4" # str | Unique identifier of a product group
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get product group
        api_response = api_instance.catalogs_product_groups_get(product_group_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get product group
        api_response = api_instance.catalogs_product_groups_get(product_group_id, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_group_id** | **str**| Unique identifier of a product group |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsVerticalProductGroup**](CatalogsVerticalProductGroup.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid catalogs product group id parameters. |  -  |
**401** | Unauthorized access. |  -  |
**403** | Forbidden. Account not approved for catalog product group mutations yet. |  -  |
**404** | Catalogs product group not found. |  -  |
**409** | Conflict. Can&#39;t get a catalogs product group without an existing catalog. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_product_groups_list**
> bool, date, datetime, dict, float, int, list, str, none_type catalogs_product_groups_list()

List product groups

Get a list of product groups for a given Catalogs Feed Id owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.catalogs_vertical_product_group import CatalogsVerticalProductGroup
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    id = [
        1,
    ] # [int] | Comma-separated list of product group ids (optional)
    feed_id = "4" # str | Filter entities for a given feed_id. If not given, all feeds are considered. (optional)
    catalog_id = "4" # str | Filter entities for a given catalog_id. If not given, all catalogs are considered. (optional)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List product groups
        api_response = api_instance.catalogs_product_groups_list(id=id, feed_id=feed_id, catalog_id=catalog_id, bookmark=bookmark, page_size=page_size, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **[int]**| Comma-separated list of product group ids | [optional]
 **feed_id** | **str**| Filter entities for a given feed_id. If not given, all feeds are considered. | [optional]
 **catalog_id** | **str**| Filter entities for a given catalog_id. If not given, all catalogs are considered. | [optional]
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

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
**400** | Invalid feed parameters. |  -  |
**401** | Unauthorized access. |  -  |
**403** | Forbidden. Account not approved for catalog product group mutations yet. |  -  |
**404** | Data feed not found. |  -  |
**409** | Conflict. Can&#39;t create this catalogs product group with this value. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_product_groups_product_counts_get**
> CatalogsProductGroupProductCountsVertical catalogs_product_groups_product_counts_get(product_group_id)

Get product counts

Get a product counts for a given Catalogs Product Group owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.catalogs_product_group_product_counts_vertical import CatalogsProductGroupProductCountsVertical
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    product_group_id = "4" # str | Unique identifier of a product group
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get product counts
        api_response = api_instance.catalogs_product_groups_product_counts_get(product_group_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_product_counts_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get product counts
        api_response = api_instance.catalogs_product_groups_product_counts_get(product_group_id, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_product_counts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_group_id** | **str**| Unique identifier of a product group |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsProductGroupProductCountsVertical**](CatalogsProductGroupProductCountsVertical.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Product Group Not Found. |  -  |
**409** | Can&#39;t access this feature without an existing catalog. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_product_groups_update**
> CatalogsVerticalProductGroup catalogs_product_groups_update(product_group_id, unknown_base_type)

Update single product group

Update product group owned by the \"operation user_account\" to use in Catalogs. - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>  Note: Access to the Creative Assets catalog type is restricted to a specific group of users. If you require access, please reach out to your partner manager.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.catalogs_product_group_update_request import CatalogsProductGroupUpdateRequest
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_generated.pinterest_client.model.catalogs_vertical_product_group import CatalogsVerticalProductGroup
from openapi_generated.pinterest_client.model.catalogs_vertical_product_group_update_request import CatalogsVerticalProductGroupUpdateRequest
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    product_group_id = "4" # str | Unique identifier of a product group
    unknown_base_type = None # UNKNOWN_BASE_TYPE | Request object used to Update a catalogs product group.
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update single product group
        api_response = api_instance.catalogs_product_groups_update(product_group_id, unknown_base_type)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update single product group
        api_response = api_instance.catalogs_product_groups_update(product_group_id, unknown_base_type, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->catalogs_product_groups_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_group_id** | **str**| Unique identifier of a product group |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Request object used to Update a catalogs product group. |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsVerticalProductGroup**](CatalogsVerticalProductGroup.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid parameters. |  -  |
**401** | Unauthorized access. |  -  |
**403** | Forbidden. Account not approved for catalog product group mutations yet. |  -  |
**404** | Catalogs product group not found. |  -  |
**409** | Conflict. Can&#39;t update this catalogs product group to this value. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feed_processing_results_list**
> bool, date, datetime, dict, float, int, list, str, none_type feed_processing_results_list(feed_id)

List feed processing results

Fetch a feed processing results owned by the \"operation user_account\". Please note that for now the bookmark parameter is not functional and only the first page will be available until it is implemented in some release in the near future. - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.catalogs_feed_processing_result import CatalogsFeedProcessingResult
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    feed_id = "4" # str | Unique identifier of a feed
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List feed processing results
        api_response = api_instance.feed_processing_results_list(feed_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feed_processing_results_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List feed processing results
        api_response = api_instance.feed_processing_results_list(feed_id, bookmark=bookmark, page_size=page_size, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feed_processing_results_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_id** | **str**| Unique identifier of a feed |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

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
**400** | Invalid parameters. |  -  |
**401** | Unauthorized access. |  -  |
**404** | Feed not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feeds_create**
> CatalogsFeed feeds_create(unknown_base_type)

Create feed

Create a new feed owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Please, be aware that \"default_country\" and \"default_locale\" are not required in the spec for forward compatibility but for now the API will not accept requests without those fields.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  For Retail partners, refer to <a href='https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs'>Before you get started with Catalogs</a>. For Hotel parterns, refer to <a href='/docs/api-features/shopping-overview/'>Pinterest API for shopping</a>.  Note: Access to the Creative Assets catalog type is restricted to a specific group of users. If you require access, please reach out to your partner manager.

### Example

* OAuth Authentication (client_credentials):
* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.catalogs_feeds_create_request import CatalogsFeedsCreateRequest
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_generated.pinterest_client.model.catalogs_feed import CatalogsFeed
from openapi_generated.pinterest_client.model.catalogs_vertical_feeds_create_request import CatalogsVerticalFeedsCreateRequest
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE | Request object used to created a feed.
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create feed
        api_response = api_instance.feeds_create(unknown_base_type)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feeds_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create feed
        api_response = api_instance.feeds_create(unknown_base_type, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feeds_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Request object used to created a feed. |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsFeed**](CatalogsFeed.md)

### Authorization

[client_credentials](../README.md#client_credentials), [pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Invalid feed parameters. |  -  |
**401** | Unauthorized access. |  -  |
**403** | Business account required. |  -  |
**409** | User website required. |  -  |
**422** | Unique feed name is required. |  -  |
**501** | Not implemented (absent \&quot;default_country\&quot; or \&quot;default_locale\&quot;). |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feeds_delete**
> feeds_delete(feed_id)

Delete feed

Delete a feed owned by the \"operating user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  For Retail partners, refer to <a href='https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs'>Before you get started with Catalogs</a>. For Hotel parterns, refer to <a href='/docs/api-features/shopping-overview/'>Pinterest API for shopping</a>.

### Example

* OAuth Authentication (client_credentials):
* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    feed_id = "4" # str | Unique identifier of a feed
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete feed
        api_instance.feeds_delete(feed_id)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feeds_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete feed
        api_instance.feeds_delete(feed_id, ad_account_id=ad_account_id)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feeds_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_id** | **str**| Unique identifier of a feed |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

void (empty response body)

### Authorization

[client_credentials](../README.md#client_credentials), [pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Feed deleted successfully. |  -  |
**400** | Invalid feed parameters. |  -  |
**403** | Forbidden. Account not approved for feed mutations yet. |  -  |
**404** | Data feed not found. |  -  |
**409** | Conflict. Can&#39;t delete a feed with active promotions. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feeds_get**
> CatalogsFeed feeds_get(feed_id)

Get feed

Get a single feed owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  For Retail partners, refer to <a href='https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs'>Before you get started with Catalogs</a>. For Hotel parterns, refer to <a href='/docs/api-features/shopping-overview/'>Pinterest API for shopping</a>.

### Example

* OAuth Authentication (client_credentials):
* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_feed import CatalogsFeed
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    feed_id = "4" # str | Unique identifier of a feed
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get feed
        api_response = api_instance.feeds_get(feed_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feeds_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get feed
        api_response = api_instance.feeds_get(feed_id, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feeds_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_id** | **str**| Unique identifier of a feed |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsFeed**](CatalogsFeed.md)

### Authorization

[client_credentials](../README.md#client_credentials), [pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid feed parameters. |  -  |
**401** | Unauthorized access. |  -  |
**404** | Data feed not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feeds_ingest**
> CatalogsFeedIngestion feeds_ingest(feed_id)

Ingest feed items

Ingest items for a given feed owned by the \"operation user_account\".  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>  Note: This endpoint is restricted to a specific group of users. If you require access, please reach out to your partner manager.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_feed_ingestion import CatalogsFeedIngestion
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    feed_id = "4" # str | Unique identifier of a feed
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Ingest feed items
        api_response = api_instance.feeds_ingest(feed_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feeds_ingest: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ingest feed items
        api_response = api_instance.feeds_ingest(feed_id, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feeds_ingest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_id** | **str**| Unique identifier of a feed |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsFeedIngestion**](CatalogsFeedIngestion.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ingestion process was successfully started. |  -  |
**400** | Invalid feed parameters. |  -  |
**403** | Forbidden. Account not approved for feed mutations yet. |  -  |
**404** | Data feed not found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feeds_list**
> bool, date, datetime, dict, float, int, list, str, none_type feeds_list()

List feeds

Fetch feeds owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  For Retail partners, refer to <a href='https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs'>Before you get started with Catalogs</a>. For Hotel parterns, refer to <a href='/docs/api-features/shopping-overview/'>Pinterest API for shopping</a>.

### Example

* OAuth Authentication (client_credentials):
* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.catalogs_feed import CatalogsFeed
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    catalog_id = "4" # str | Filter entities for a given catalog_id. If not given, all catalogs are considered. (optional)
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List feeds
        api_response = api_instance.feeds_list(bookmark=bookmark, page_size=page_size, catalog_id=catalog_id, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feeds_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **catalog_id** | **str**| Filter entities for a given catalog_id. If not given, all catalogs are considered. | [optional]
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

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
**200** | Success |  -  |
**400** | Invalid parameters. |  -  |
**401** | Unauthorized access. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feeds_update**
> CatalogsFeed feeds_update(feed_id, unknown_base_type)

Update feed

Update a feed owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  For Retail partners, refer to <a href='https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs'>Before you get started with Catalogs</a>. For Hotel parterns, refer to <a href='/docs/api-features/shopping-overview/'>Pinterest API for shopping</a>.  Note: Access to the Creative Assets catalog type is restricted to a specific group of users. If you require access, please reach out to your partner manager.

### Example

* OAuth Authentication (client_credentials):
* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_generated.pinterest_client.model.catalogs_vertical_feeds_update_request import CatalogsVerticalFeedsUpdateRequest
from openapi_generated.pinterest_client.model.catalogs_feed import CatalogsFeed
from openapi_generated.pinterest_client.model.catalogs_feeds_update_request import CatalogsFeedsUpdateRequest
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    feed_id = "4" # str | Unique identifier of a feed
    unknown_base_type = None # UNKNOWN_BASE_TYPE | Request object used to update a feed.
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update feed
        api_response = api_instance.feeds_update(feed_id, unknown_base_type)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feeds_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update feed
        api_response = api_instance.feeds_update(feed_id, unknown_base_type, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->feeds_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_id** | **str**| Unique identifier of a feed |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Request object used to update a feed. |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsFeed**](CatalogsFeed.md)

### Authorization

[client_credentials](../README.md#client_credentials), [pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid feed parameters. |  -  |
**403** | Forbidden. Account not approved for feed mutations yet. |  -  |
**404** | Data feed not found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_batch_get**
> CatalogsItemsBatch items_batch_get(batch_id)

Get item batch status

Get a single catalogs items batch owned by the \"operating user_account\". <a href=\"/docs/api-features/shopping-overview/#Update%20items%20in%20batch\" target=\"_blank\">See detailed documentation here.</a> - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.

### Example

* OAuth Authentication (client_credentials):
* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_items_batch import CatalogsItemsBatch
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    batch_id = "595953100599279259-66753b9bb65c46c49bd8503b27fecf9e" # str | Id of a catalogs items batch to fetch
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get item batch status
        api_response = api_instance.items_batch_get(batch_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->items_batch_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get item batch status
        api_response = api_instance.items_batch_get(batch_id, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->items_batch_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| Id of a catalogs items batch to fetch |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsItemsBatch**](CatalogsItemsBatch.md)

### Authorization

[client_credentials](../README.md#client_credentials), [pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response containing the requested catalogs items batch |  -  |
**401** | Not authenticated to access catalogs items batch |  -  |
**403** | Not authorized to access catalogs items batch |  -  |
**404** | Catalogs items batch not found |  -  |
**405** | Method Not Allowed. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_batch_post**
> CatalogsItemsBatch items_batch_post(unknown_base_type)

Operate on item batch

This endpoint supports multiple operations on a set of one or more catalog items owned by the \"operation user_account\". <a href=\"/docs/api-features/shopping-overview/#Update%20items%20in%20batch\" target=\"_blank\">See detailed documentation here.</a> - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  Note: - Access to the Creative Assets catalog type is restricted to a specific group of users. If you require access, please reach out to your partner manager. - The item UPSERT operation is restricted to users without a feed data source. If you plan to migrate item ingestion from feeds to the API, please reach out to your partner manager to get assistance.

### Example

* OAuth Authentication (client_credentials):
* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.unknownbasetype import UNKNOWNBASETYPE
from openapi_generated.pinterest_client.model.catalogs_vertical_batch_request import CatalogsVerticalBatchRequest
from openapi_generated.pinterest_client.model.catalogs_items_batch import CatalogsItemsBatch
from openapi_generated.pinterest_client.model.catalogs_items_batch_request import CatalogsItemsBatchRequest
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    unknown_base_type = None # UNKNOWN_BASE_TYPE | Request object used to create catalogs items in a batch
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Operate on item batch
        api_response = api_instance.items_batch_post(unknown_base_type)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->items_batch_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Operate on item batch
        api_response = api_instance.items_batch_post(unknown_base_type, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->items_batch_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Request object used to create catalogs items in a batch |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsItemsBatch**](CatalogsItemsBatch.md)

### Authorization

[client_credentials](../README.md#client_credentials), [pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response containing the requested catalogs items batch |  -  |
**400** | Invalid request parameters. |  -  |
**401** | Not authenticated to post catalogs items |  -  |
**403** | Not authorized to post catalogs items |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_get**
> CatalogsItems items_get(country, language)

Get catalogs items

Get the items of the catalog owned by the \"operation user_account\". <a href=\"/docs/api-features/shopping-overview/#Update%20items%20in%20batch\" target=\"_blank\">See detailed documentation here.</a> - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  Note: this endpoint is deprecated and will be deleted soon. Please use <a href='/docs/api/v5/#operation/items/post'>Get catalogs items (POST)</a> instead.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_items import CatalogsItems
from openapi_generated.pinterest_client.model.catalogs_items_filters import CatalogsItemsFilters
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    country = "US" # str | Country for the Catalogs Items
    language = "EN" # str | Language for the Catalogs Items
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)
    item_ids = ["CR123"] # [str] | This parameter is deprecated. Use filters instead. (optional)
    filters = CatalogsItemsFilters(
        catalog_type=CatalogsType("RETAIL"),
    ) # CatalogsItemsFilters | Identifies items to be retrieved. This is a required parameter. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get catalogs items
        api_response = api_instance.items_get(country, language)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->items_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get catalogs items
        api_response = api_instance.items_get(country, language, ad_account_id=ad_account_id, item_ids=item_ids, filters=filters)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->items_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Country for the Catalogs Items |
 **language** | **str**| Language for the Catalogs Items |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]
 **item_ids** | **[str]**| This parameter is deprecated. Use filters instead. | [optional]
 **filters** | **CatalogsItemsFilters**| Identifies items to be retrieved. This is a required parameter. | [optional]

### Return type

[**CatalogsItems**](CatalogsItems.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response containing the requested catalogs items |  -  |
**400** | Invalid request parameters. |  -  |
**401** | Not authorized to access catalogs items |  -  |
**403** | Not authorized to access catalogs items |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_issues_list**
> bool, date, datetime, dict, float, int, list, str, none_type items_issues_list(processing_result_id)

List item issues

List item validation issues for a given feed processing result owned by the \"operation user_account\". Up to 20 random samples of affected items are returned for each error and warning code. Please note that for now query parameters 'item_numbers' and 'item_validation_issue' cannot be used simultaneously until it is implemented in some release in the future. - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  Note: To get a list of all affected items instead of sampled issues, please refer to <a href='/docs/api/v5/#operation/reports/create'>Build catalogs report</a> and <a href='/docs/api/v5/#operation/reports/get'>Get catalogs report</a> endpoints. Moreover, they support multiple types of catalogs.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_item_validation_issue import CatalogsItemValidationIssue
from openapi_generated.pinterest_client.model.catalogs_item_validation_issues import CatalogsItemValidationIssues
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    processing_result_id = "5224831246441439241" # str | Unique identifier of a feed processing result. It can be acquired from the \"id\" field of the \"items\" array within the response of the [List processing results for a given feed](/docs/api/v5/#operation/feed_processing_results/list).
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    item_numbers = [1,5] # [int] | Item number based on order of appearance in the Catalogs Feed. For example, '0' refers to first item found in a feed that was downloaded from a 'location' specified during feed creation. (optional)
    item_validation_issue = CatalogsItemValidationIssue("TITLE_MISSING") # CatalogsItemValidationIssue | Filter item validation issues that have a given type of item validation issue. (optional)
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List item issues
        api_response = api_instance.items_issues_list(processing_result_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->items_issues_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List item issues
        api_response = api_instance.items_issues_list(processing_result_id, bookmark=bookmark, page_size=page_size, item_numbers=item_numbers, item_validation_issue=item_validation_issue, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->items_issues_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processing_result_id** | **str**| Unique identifier of a feed processing result. It can be acquired from the \&quot;id\&quot; field of the \&quot;items\&quot; array within the response of the [List processing results for a given feed](/docs/api/v5/#operation/feed_processing_results/list). |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **item_numbers** | **[int]**| Item number based on order of appearance in the Catalogs Feed. For example, &#39;0&#39; refers to first item found in a feed that was downloaded from a &#39;location&#39; specified during feed creation. | [optional]
 **item_validation_issue** | **CatalogsItemValidationIssue**| Filter item validation issues that have a given type of item validation issue. | [optional]
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

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
**401** | Unauthorized access. |  -  |
**404** | Processing Result not found. |  -  |
**501** | Not implemented. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_post**
> CatalogsItems items_post(catalogs_items_request)

Get catalogs items (POST)

Get the items of the catalog owned by the \"operation user_account\". <a href=\"/docs/api-features/shopping-overview/#Update%20items%20in%20batch\" target=\"_blank\">See detailed documentation here.</a> - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  Note: Access to the Creative Assets catalog type is restricted to a specific group of users. If you require access, please reach out to your partner manager.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_items_request import CatalogsItemsRequest
from openapi_generated.pinterest_client.model.catalogs_items import CatalogsItems
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    catalogs_items_request = CatalogsItemsRequest(
        country=Country("US"),
        language=None,
        filters=CatalogsItemsPostFilters(
            catalog_type=CatalogsType("RETAIL"),
        ),
    ) # CatalogsItemsRequest | Request object used to get catalogs items
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get catalogs items (POST)
        api_response = api_instance.items_post(catalogs_items_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->items_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get catalogs items (POST)
        api_response = api_instance.items_post(catalogs_items_request, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->items_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalogs_items_request** | [**CatalogsItemsRequest**](CatalogsItemsRequest.md)| Request object used to get catalogs items |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsItems**](CatalogsItems.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response containing the requested catalogs items |  -  |
**400** | Invalid request |  -  |
**401** | Not authorized to access catalogs items |  -  |
**403** | Not authorized to access catalogs items |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_by_product_group_filter_list**
> bool, date, datetime, dict, float, int, list, str, none_type products_by_product_group_filter_list(catalogs_list_products_by_filter_request)

List products by filter

List products Pins owned by the \"operation user_account\" that meet the criteria specified in the Catalogs Product Group Filter given in the request. - This endpoint has been implemented in POST to allow for complex filters. This specific POST endpoint is designed to be idempotent. - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.  Note: This endpoint only supports RETAIL catalog at the moment.  <a href='/docs/api-features/shopping-overview/'>Learn more</a>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_product import CatalogsProduct
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.catalogs_list_products_by_filter_request import CatalogsListProductsByFilterRequest
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    catalogs_list_products_by_filter_request = CatalogsListProductsByFilterRequest() # CatalogsListProductsByFilterRequest | Object holding a group of filters for a catalog product group
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)
    pin_metrics = False # bool | Specify whether to return 90d and lifetime Pin metrics. Total comments and total reactions are only available with lifetime Pin metrics. If Pin was created before <code>2023-03-20</code> lifetime metrics will only be available for Video and Idea Pin formats. Lifetime metrics are available for all Pin formats since then. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # List products by filter
        api_response = api_instance.products_by_product_group_filter_list(catalogs_list_products_by_filter_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->products_by_product_group_filter_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List products by filter
        api_response = api_instance.products_by_product_group_filter_list(catalogs_list_products_by_filter_request, bookmark=bookmark, page_size=page_size, ad_account_id=ad_account_id, pin_metrics=pin_metrics)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->products_by_product_group_filter_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalogs_list_products_by_filter_request** | [**CatalogsListProductsByFilterRequest**](CatalogsListProductsByFilterRequest.md)| Object holding a group of filters for a catalog product group |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]
 **pin_metrics** | **bool**| Specify whether to return 90d and lifetime Pin metrics. Total comments and total reactions are only available with lifetime Pin metrics. If Pin was created before &lt;code&gt;2023-03-20&lt;/code&gt; lifetime metrics will only be available for Video and Idea Pin formats. Lifetime metrics are available for all Pin formats since then. | [optional] if omitted the server will use the default value of False

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized access. |  -  |
**409** | Conflict. Can&#39;t get products. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_create**
> CatalogsCreateReportResponse reports_create(catalogs_report_parameters)

Build catalogs report

Async request to create a report of the catalog owned by the \"operation user_account\". This endpoint generates a report upon receiving the first approved request of the day. Any following requests with identical parameters will yield the same report even if data has changed. - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.catalogs_create_report_response import CatalogsCreateReportResponse
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_report_parameters import CatalogsReportParameters
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    catalogs_report_parameters = CatalogsReportParameters(
        catalog_type=CatalogsType("RETAIL"),
    ) # CatalogsReportParameters | Request object to asynchronously create a report.
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Build catalogs report
        api_response = api_instance.reports_create(catalogs_report_parameters)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->reports_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Build catalogs report
        api_response = api_instance.reports_create(catalogs_report_parameters, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->reports_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalogs_report_parameters** | [**CatalogsReportParameters**](CatalogsReportParameters.md)| Request object to asynchronously create a report. |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsCreateReportResponse**](CatalogsCreateReportResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response containing the report token |  -  |
**404** | Entity (e.g., catalog, feed or processing_result) not found |  -  |
**409** | Can&#39;t access this feature without an existing catalog. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_get**
> CatalogsReport reports_get(token)

Get catalogs report

This returns a URL to a report given a token returned from <a href='/docs/api/v5/#operation/reports/create'>Build catalogs report</a>. You can use the URL to download the report. - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.catalogs_report import CatalogsReport
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    token = "token_example" # str | Token returned from async build report call
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get catalogs report
        api_response = api_instance.reports_get(token)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->reports_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get catalogs report
        api_response = api_instance.reports_get(token, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->reports_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token returned from async build report call |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**CatalogsReport**](CatalogsReport.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response that contains a link to download the report |  -  |
**400** | The token you provided is not valid or has expired. |  -  |
**409** | Can&#39;t access this feature without an existing catalog. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_stats**
> bool, date, datetime, dict, float, int, list, str, none_type reports_stats(parameters)

List report stats

List aggregated numbers of issues for a catalog owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: Owner, Admin, Catalogs Manager.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import catalogs_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.catalogs_report_stats import CatalogsReportStats
from openapi_generated.pinterest_client.model.catalogs_report_parameters import CatalogsReportParameters
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    parameters = CatalogsReportParameters(
        catalog_type=CatalogsType("RETAIL"),
    ) # CatalogsReportParameters | Contains the parameters for report identification.
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    try:
        # List report stats
        api_response = api_instance.reports_stats(parameters)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->reports_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List report stats
        api_response = api_instance.reports_stats(parameters, ad_account_id=ad_account_id, page_size=page_size, bookmark=bookmark)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling CatalogsApi->reports_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | **CatalogsReportParameters**| Contains the parameters for report identification. |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]
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
**200** | Response containing the diagnostics aggregated counters |  -  |
**401** | Not authorized to access catalogs |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

