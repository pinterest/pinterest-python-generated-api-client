# openapi_generated.pinterest_client.ConversionTagsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversion_tags_create**](ConversionTagsApi.md#conversion_tags_create) | **POST** /ad_accounts/{ad_account_id}/conversion_tags | Create conversion tag
[**conversion_tags_get**](ConversionTagsApi.md#conversion_tags_get) | **GET** /ad_accounts/{ad_account_id}/conversion_tags/{conversion_tag_id} | Get conversion tag
[**conversion_tags_list**](ConversionTagsApi.md#conversion_tags_list) | **GET** /ad_accounts/{ad_account_id}/conversion_tags | Get conversion tags
[**ocpm_eligible_conversion_tags_get**](ConversionTagsApi.md#ocpm_eligible_conversion_tags_get) | **GET** /ad_accounts/{ad_account_id}/conversion_tags/ocpm_eligible | Get Ocpm eligible conversion tags
[**page_visit_conversion_tags_get**](ConversionTagsApi.md#page_visit_conversion_tags_get) | **GET** /ad_accounts/{ad_account_id}/conversion_tags/page_visit | Get page visit conversion tags


# **conversion_tags_create**
> ConversionTagResponse conversion_tags_create(ad_account_id, conversion_tag_create)

Create conversion tag

Create a conversion tag, also known as <a href=\"https://help.pinterest.com/en/business/article/set-up-the-pinterest-tag\" target=\"_blank\">Pinterest tag</a>, with the option to enable enhanced match.<p/> The Pinterest Tag tracks actions people take on the ad account’s website after they view the ad account's ad on Pinterest. The advertiser needs to customize this tag to track conversions.<p/> For more information, see:<p/> <a class=\"reference external\" href=\"https://help.pinterest.com/en/business/article/set-up-the-pinterest-tag\">Set up the Pinterest tag</a><p/> <a class=\"reference external\" href=\"https://developers.pinterest.com/docs/conversions/pinterest-tag/\">Pinterest Tag</a><p/> <a class=\"reference external\" href=\"https://developers.pinterest.com/docs/conversions/enhanced-match/\">Enhanced match</a>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import conversion_tags_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.conversion_tag_create import ConversionTagCreate
from openapi_generated.pinterest_client.model.conversion_tag_response import ConversionTagResponse
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
    api_instance = conversion_tags_api.ConversionTagsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    conversion_tag_create = ConversionTagCreate(
        name="ACME Tools Tag",
    ) # ConversionTagCreate | Conversion Tag to create

    # example passing only required values which don't have defaults set
    try:
        # Create conversion tag
        api_response = api_instance.conversion_tags_create(ad_account_id, conversion_tag_create)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ConversionTagsApi->conversion_tags_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **conversion_tag_create** | [**ConversionTagCreate**](ConversionTagCreate.md)| Conversion Tag to create |

### Return type

[**ConversionTagResponse**](ConversionTagResponse.md)

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

# **conversion_tags_get**
> ConversionTagResponse conversion_tags_get(ad_account_id, conversion_tag_id)

Get conversion tag

Get information about an existing conversion tag.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import conversion_tags_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.conversion_tag_response import ConversionTagResponse
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
    api_instance = conversion_tags_api.ConversionTagsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    conversion_tag_id = "2617998078212" # str | Id of the conversion tag.

    # example passing only required values which don't have defaults set
    try:
        # Get conversion tag
        api_response = api_instance.conversion_tags_get(ad_account_id, conversion_tag_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ConversionTagsApi->conversion_tags_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **conversion_tag_id** | **str**| Id of the conversion tag. |

### Return type

[**ConversionTagResponse**](ConversionTagResponse.md)

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

# **conversion_tags_list**
> ConversionTagListResponse conversion_tags_list(ad_account_id)

Get conversion tags

List conversion tags associated with an ad account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import conversion_tags_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.conversion_tag_list_response import ConversionTagListResponse
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
    api_instance = conversion_tags_api.ConversionTagsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    filter_deleted = True # bool | Filter out deleted tags. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get conversion tags
        api_response = api_instance.conversion_tags_list(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ConversionTagsApi->conversion_tags_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get conversion tags
        api_response = api_instance.conversion_tags_list(ad_account_id, filter_deleted=filter_deleted)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ConversionTagsApi->conversion_tags_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **filter_deleted** | **bool**| Filter out deleted tags. | [optional] if omitted the server will use the default value of False

### Return type

[**ConversionTagListResponse**](ConversionTagListResponse.md)

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

# **ocpm_eligible_conversion_tags_get**
> ConversionTagsOcpmEligibleResponse ocpm_eligible_conversion_tags_get(ad_account_id)

Get Ocpm eligible conversion tags

Get Ocpm eligible conversion tag events for an ad account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import conversion_tags_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.conversion_tags_ocpm_eligible_response import ConversionTagsOcpmEligibleResponse
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
    api_instance = conversion_tags_api.ConversionTagsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.

    # example passing only required values which don't have defaults set
    try:
        # Get Ocpm eligible conversion tags
        api_response = api_instance.ocpm_eligible_conversion_tags_get(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ConversionTagsApi->ocpm_eligible_conversion_tags_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |

### Return type

[**ConversionTagsOcpmEligibleResponse**](ConversionTagsOcpmEligibleResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Unexpected errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **page_visit_conversion_tags_get**
> bool, date, datetime, dict, float, int, list, str, none_type page_visit_conversion_tags_get(ad_account_id)

Get page visit conversion tags

Get all page visit conversion tag events for an ad account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import conversion_tags_api
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
    api_instance = conversion_tags_api.ConversionTagsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/getting-started/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    order = "ASCENDING" # str | The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. (optional)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get page visit conversion tags
        api_response = api_instance.page_visit_conversion_tags_get(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ConversionTagsApi->page_visit_conversion_tags_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get page visit conversion tags
        api_response = api_instance.page_visit_conversion_tags_get(ad_account_id, page_size=page_size, order=order, bookmark=bookmark)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ConversionTagsApi->page_visit_conversion_tags_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/getting-started/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **order** | **str**| The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. | [optional]
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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

