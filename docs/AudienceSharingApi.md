# openapi_generated.pinterest_client.AudienceSharingApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ad_accounts_audiences_shared_accounts_list**](AudienceSharingApi.md#ad_accounts_audiences_shared_accounts_list) | **GET** /ad_accounts/{ad_account_id}/audiences/shared/accounts | List accounts with access to an audience owned by an ad account
[**business_account_audiences_shared_accounts_list**](AudienceSharingApi.md#business_account_audiences_shared_accounts_list) | **GET** /businesses/{business_id}/audiences/shared/accounts | List accounts with access to an audience owned by a business
[**shared_audiences_for_business_list**](AudienceSharingApi.md#shared_audiences_for_business_list) | **GET** /businesses/{business_id}/audiences | List received audiences for a business
[**update_ad_account_to_ad_account_shared_audience**](AudienceSharingApi.md#update_ad_account_to_ad_account_shared_audience) | **PATCH** /ad_accounts/{ad_account_id}/audiences/ad_accounts/shared | Update audience sharing between ad accounts
[**update_ad_account_to_business_shared_audience**](AudienceSharingApi.md#update_ad_account_to_business_shared_audience) | **PATCH** /ad_accounts/{ad_account_id}/audiences/businesses/shared | Update audience sharing from an ad account to businesses
[**update_business_to_ad_account_shared_audience**](AudienceSharingApi.md#update_business_to_ad_account_shared_audience) | **PATCH** /businesses/{business_id}/audiences/ad_accounts/shared | Update audience sharing from a business to ad accounts
[**update_business_to_business_shared_audience**](AudienceSharingApi.md#update_business_to_business_shared_audience) | **PATCH** /businesses/{business_id}/audiences/businesses/shared | Update audience sharing between businesses


# **ad_accounts_audiences_shared_accounts_list**
> bool, date, datetime, dict, float, int, list, str, none_type ad_accounts_audiences_shared_accounts_list(ad_account_id, audience_id, account_type)

List accounts with access to an audience owned by an ad account

List all ad accounts and/or businesses that have access to a specific audience. The audience must be owned by the requesting ad account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import audience_sharing_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.shared_audience_account import SharedAudienceAccount
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.audience_account_type import AudienceAccountType
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
    api_instance = audience_sharing_api.AudienceSharingApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    audience_id = "4" # str | Unique identifier of the audience to use to filter the results.
    account_type = AudienceAccountType("AD_ACCOUNT") # AudienceAccountType | Filter accounts by account type.
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    try:
        # List accounts with access to an audience owned by an ad account
        api_response = api_instance.ad_accounts_audiences_shared_accounts_list(ad_account_id, audience_id, account_type)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceSharingApi->ad_accounts_audiences_shared_accounts_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List accounts with access to an audience owned by an ad account
        api_response = api_instance.ad_accounts_audiences_shared_accounts_list(ad_account_id, audience_id, account_type, page_size=page_size, bookmark=bookmark)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceSharingApi->ad_accounts_audiences_shared_accounts_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **audience_id** | **str**| Unique identifier of the audience to use to filter the results. |
 **account_type** | **AudienceAccountType**| Filter accounts by account type. |
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
**400** | Invalid ad account audiences shared accounts parameters. |  -  |
**404** | Shared accounts not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_account_audiences_shared_accounts_list**
> bool, date, datetime, dict, float, int, list, str, none_type business_account_audiences_shared_accounts_list(business_id, audience_id, account_type)

List accounts with access to an audience owned by a business

List all ad accounts and/or businesses that have access to a specific audience. The audience must either be owned by an ad account in the requesting business, or it must have been shared with the requesting business. If the requesting business is not the owner of the audience, only ad accounts owned by the requesting business will be returned.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import audience_sharing_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.shared_audience_account import SharedAudienceAccount
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.audience_account_type import AudienceAccountType
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
    api_instance = audience_sharing_api.AudienceSharingApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    audience_id = "4" # str | Unique identifier of the audience to use to filter the results.
    account_type = AudienceAccountType("AD_ACCOUNT") # AudienceAccountType | Filter accounts by account type.
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    try:
        # List accounts with access to an audience owned by a business
        api_response = api_instance.business_account_audiences_shared_accounts_list(business_id, audience_id, account_type)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceSharingApi->business_account_audiences_shared_accounts_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List accounts with access to an audience owned by a business
        api_response = api_instance.business_account_audiences_shared_accounts_list(business_id, audience_id, account_type, page_size=page_size, bookmark=bookmark)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceSharingApi->business_account_audiences_shared_accounts_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **audience_id** | **str**| Unique identifier of the audience to use to filter the results. |
 **account_type** | **AudienceAccountType**| Filter accounts by account type. |
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
**400** | Invalid business audiences shared accounts parameters. |  -  |
**404** | Shared accounts not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shared_audiences_for_business_list**
> bool, date, datetime, dict, float, int, list, str, none_type shared_audiences_for_business_list(business_id)

List received audiences for a business

Get a list of received audiences for the given business.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import audience_sharing_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.audience import Audience
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
    api_instance = audience_sharing_api.AudienceSharingApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    order = "ASCENDING" # str | The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # List received audiences for a business
        api_response = api_instance.shared_audiences_for_business_list(business_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceSharingApi->shared_audiences_for_business_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List received audiences for a business
        api_response = api_instance.shared_audiences_for_business_list(business_id, bookmark=bookmark, order=order, page_size=page_size)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceSharingApi->shared_audiences_for_business_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **order** | **str**| The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ad_account_to_ad_account_shared_audience**
> SharedAudienceResponse update_ad_account_to_ad_account_shared_audience(ad_account_id, shared_audience)

Update audience sharing between ad accounts

From an ad account, share a specific audience with another ad account, or revoke access to a previously shared audience. Only the audience owner account can share the audience. The recipient ad account(s) must be in the same <a href='https://help.pinterest.com/en/business/article/create-and-manage-accounts'>Pinterest Business Hierarchy</a> as the business owner of the ad account.<br> This endpoint is not available to all apps.<a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import audience_sharing_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.shared_audience_response import SharedAudienceResponse
from openapi_generated.pinterest_client.model.shared_audience import SharedAudience
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
    api_instance = audience_sharing_api.AudienceSharingApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    shared_audience = SharedAudience() # SharedAudience | 

    # example passing only required values which don't have defaults set
    try:
        # Update audience sharing between ad accounts
        api_response = api_instance.update_ad_account_to_ad_account_shared_audience(ad_account_id, shared_audience)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceSharingApi->update_ad_account_to_ad_account_shared_audience: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **shared_audience** | [**SharedAudience**](SharedAudience.md)|  |

### Return type

[**SharedAudienceResponse**](SharedAudienceResponse.md)

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

# **update_ad_account_to_business_shared_audience**
> BusinessSharedAudienceResponse update_ad_account_to_business_shared_audience(ad_account_id, business_shared_audience)

Update audience sharing from an ad account to businesses

From an ad account, share a specific audience with a business account, or revoke access to a previously shared audience. Only the audience owner account can share the audience. The recipient business account must be in the same business hierarchy as the business owner of the ad account.<br> This endpoint is not available to all apps.<a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import audience_sharing_api
from openapi_generated.pinterest_client.model.business_shared_audience import BusinessSharedAudience
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.business_shared_audience_response import BusinessSharedAudienceResponse
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
    api_instance = audience_sharing_api.AudienceSharingApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    business_shared_audience = BusinessSharedAudience() # BusinessSharedAudience | 

    # example passing only required values which don't have defaults set
    try:
        # Update audience sharing from an ad account to businesses
        api_response = api_instance.update_ad_account_to_business_shared_audience(ad_account_id, business_shared_audience)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceSharingApi->update_ad_account_to_business_shared_audience: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **business_shared_audience** | [**BusinessSharedAudience**](BusinessSharedAudience.md)|  |

### Return type

[**BusinessSharedAudienceResponse**](BusinessSharedAudienceResponse.md)

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

# **update_business_to_ad_account_shared_audience**
> SharedAudienceResponse update_business_to_ad_account_shared_audience(business_id, shared_audience)

Update audience sharing from a business to ad accounts

From a business, share a specific audience with other ad account(s), or revoke access to a previously shared audience. <ul> <li>If the business is the owner of the audience, it can share with any ad account within the same business hierarchy.</li> <li>If the business is the recipient of the audience, it can share with any of its owned ad accounts.</li> </ul> This endpoint is not available to all apps.<a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import audience_sharing_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.shared_audience_response import SharedAudienceResponse
from openapi_generated.pinterest_client.model.shared_audience import SharedAudience
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
    api_instance = audience_sharing_api.AudienceSharingApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    shared_audience = SharedAudience() # SharedAudience | 

    # example passing only required values which don't have defaults set
    try:
        # Update audience sharing from a business to ad accounts
        api_response = api_instance.update_business_to_ad_account_shared_audience(business_id, shared_audience)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceSharingApi->update_business_to_ad_account_shared_audience: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **shared_audience** | [**SharedAudience**](SharedAudience.md)|  |

### Return type

[**SharedAudienceResponse**](SharedAudienceResponse.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_business_to_business_shared_audience**
> BusinessSharedAudienceResponse update_business_to_business_shared_audience(business_id, business_shared_audience)

Update audience sharing between businesses

From a business, share a specific audience with another business account, or revoke access to a previously shared audience. Only the audience owner can share the audience with other businesses, and the recipient business must be within the same business hierarchy.<br> This endpoint is not available to all apps.<a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import audience_sharing_api
from openapi_generated.pinterest_client.model.business_shared_audience import BusinessSharedAudience
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.business_shared_audience_response import BusinessSharedAudienceResponse
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
    api_instance = audience_sharing_api.AudienceSharingApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    business_shared_audience = BusinessSharedAudience() # BusinessSharedAudience | 

    # example passing only required values which don't have defaults set
    try:
        # Update audience sharing between businesses
        api_response = api_instance.update_business_to_business_shared_audience(business_id, business_shared_audience)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceSharingApi->update_business_to_business_shared_audience: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **business_shared_audience** | [**BusinessSharedAudience**](BusinessSharedAudience.md)|  |

### Return type

[**BusinessSharedAudienceResponse**](BusinessSharedAudienceResponse.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

