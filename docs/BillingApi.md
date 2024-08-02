# openapi_generated.pinterest_client.BillingApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ads_credit_redeem**](BillingApi.md#ads_credit_redeem) | **POST** /ad_accounts/{ad_account_id}/ads_credit/redeem | Redeem ad credits
[**ads_credits_discounts_get**](BillingApi.md#ads_credits_discounts_get) | **GET** /ad_accounts/{ad_account_id}/ads_credit/discounts | Get ads credit discounts
[**billing_profiles_get**](BillingApi.md#billing_profiles_get) | **GET** /ad_accounts/{ad_account_id}/billing_profiles | Get billing profiles
[**ssio_accounts_get**](BillingApi.md#ssio_accounts_get) | **GET** /ad_accounts/{ad_account_id}/ssio/accounts | Get Salesforce account details including bill-to information.
[**ssio_insertion_order_create**](BillingApi.md#ssio_insertion_order_create) | **POST** /ad_accounts/{ad_account_id}/ssio/insertion_orders | Create insertion order through SSIO.
[**ssio_insertion_order_edit**](BillingApi.md#ssio_insertion_order_edit) | **PATCH** /ad_accounts/{ad_account_id}/ssio/insertion_orders | Edit insertion order through SSIO.
[**ssio_insertion_orders_status_get_by_ad_account**](BillingApi.md#ssio_insertion_orders_status_get_by_ad_account) | **GET** /ad_accounts/{ad_account_id}/ssio/insertion_orders/status | Get insertion order status by ad account id.
[**ssio_insertion_orders_status_get_by_pin_order_id**](BillingApi.md#ssio_insertion_orders_status_get_by_pin_order_id) | **GET** /ad_accounts/{ad_account_id}/ssio/insertion_orders/{pin_order_id}/status | Get insertion order status by pin order id.
[**ssio_order_lines_get_by_ad_account**](BillingApi.md#ssio_order_lines_get_by_ad_account) | **GET** /ad_accounts/{ad_account_id}/ssio/order_lines | Get Salesforce order lines by ad account id.


# **ads_credit_redeem**
> AdsCreditRedeemResponse ads_credit_redeem(ad_account_id, ads_credit_redeem_request)

Redeem ad credits

Redeem ads credit on behalf of the ad account id and apply it towards billing.  <strong>This endpoint might not be available to all apps. <a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.</strong>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import billing_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ads_credit_redeem_request import AdsCreditRedeemRequest
from openapi_generated.pinterest_client.model.ads_credit_redeem_response import AdsCreditRedeemResponse
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
    api_instance = billing_api.BillingApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    ads_credit_redeem_request = AdsCreditRedeemRequest(
        offer_code_hash="138e9e0ff7e38cf511b880975eb574c09aa9d5e1657590ab0431040da68caa67",
        validate_only=True,
    ) # AdsCreditRedeemRequest | Redeem ad credits request.

    # example passing only required values which don't have defaults set
    try:
        # Redeem ad credits
        api_response = api_instance.ads_credit_redeem(ad_account_id, ads_credit_redeem_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->ads_credit_redeem: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **ads_credit_redeem_request** | [**AdsCreditRedeemRequest**](AdsCreditRedeemRequest.md)| Redeem ad credits request. |

### Return type

[**AdsCreditRedeemResponse**](AdsCreditRedeemResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully redeemed ad credits. |  -  |
**400** | Error thrown when unable to redeem offer code. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ads_credits_discounts_get**
> bool, date, datetime, dict, float, int, list, str, none_type ads_credits_discounts_get(ad_account_id)

Get ads credit discounts

Returns the list of discounts applied to the account.  <strong>This endpoint might not be available to all apps. <a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.</strong>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import billing_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.ads_credit_discounts_response import AdsCreditDiscountsResponse
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
    api_instance = billing_api.BillingApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get ads credit discounts
        api_response = api_instance.ads_credits_discounts_get(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->ads_credits_discounts_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get ads credit discounts
        api_response = api_instance.ads_credits_discounts_get(ad_account_id, bookmark=bookmark, page_size=page_size)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->ads_credits_discounts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
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
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_profiles_get**
> bool, date, datetime, dict, float, int, list, str, none_type billing_profiles_get(ad_account_id, is_active)

Get billing profiles

Get billing profiles in the advertiser account.  <strong>This endpoint might not be available to all apps. <a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.</strong>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import billing_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.billing_profiles_response import BillingProfilesResponse
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
    api_instance = billing_api.BillingApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    is_active = True # bool | Return active billing profiles, if false return all billing profiles.
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get billing profiles
        api_response = api_instance.billing_profiles_get(ad_account_id, is_active)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->billing_profiles_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get billing profiles
        api_response = api_instance.billing_profiles_get(ad_account_id, is_active, bookmark=bookmark, page_size=page_size)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->billing_profiles_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **is_active** | **bool**| Return active billing profiles, if false return all billing profiles. |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
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
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssio_accounts_get**
> SSIOAccountResponse ssio_accounts_get(ad_account_id)

Get Salesforce account details including bill-to information.

Get Salesforce account details including bill-to information to be used in insertion orders process for <code>ad_account_id</code>. - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a>: Admin, Finance, Campaign.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import billing_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ssio_account_response import SSIOAccountResponse
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
    api_instance = billing_api.BillingApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.

    # example passing only required values which don't have defaults set
    try:
        # Get Salesforce account details including bill-to information.
        api_response = api_instance.ssio_accounts_get(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->ssio_accounts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |

### Return type

[**SSIOAccountResponse**](SSIOAccountResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request parameter. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssio_insertion_order_create**
> SSIOCreateInsertionOrderResponse ssio_insertion_order_create(ad_account_id, ssio_create_insertion_order_request)

Create insertion order through SSIO.

Create insertion order through SSIO for <code>ad_account_id</code>. - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a>: Admin, Finance, Campaign.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import billing_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ssio_create_insertion_order_request import SSIOCreateInsertionOrderRequest
from openapi_generated.pinterest_client.model.ssio_create_insertion_order_response import SSIOCreateInsertionOrderResponse
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
    api_instance = billing_api.BillingApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    ssio_create_insertion_order_request = SSIOCreateInsertionOrderRequest() # SSIOCreateInsertionOrderRequest | Order line to create.

    # example passing only required values which don't have defaults set
    try:
        # Create insertion order through SSIO.
        api_response = api_instance.ssio_insertion_order_create(ad_account_id, ssio_create_insertion_order_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->ssio_insertion_order_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **ssio_create_insertion_order_request** | [**SSIOCreateInsertionOrderRequest**](SSIOCreateInsertionOrderRequest.md)| Order line to create. |

### Return type

[**SSIOCreateInsertionOrderResponse**](SSIOCreateInsertionOrderResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssio_insertion_order_edit**
> SSIOEditInsertionOrderResponse ssio_insertion_order_edit(ad_account_id, ssio_edit_insertion_order_request)

Edit insertion order through SSIO.

Edit insertion order through SSIO for <code>ad_account_id</code>. - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a>: Admin, Finance, Campaign.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import billing_api
from openapi_generated.pinterest_client.model.ssio_edit_insertion_order_response import SSIOEditInsertionOrderResponse
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ssio_edit_insertion_order_request import SSIOEditInsertionOrderRequest
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
    api_instance = billing_api.BillingApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    ssio_edit_insertion_order_request = SSIOEditInsertionOrderRequest() # SSIOEditInsertionOrderRequest | Order line to create.

    # example passing only required values which don't have defaults set
    try:
        # Edit insertion order through SSIO.
        api_response = api_instance.ssio_insertion_order_edit(ad_account_id, ssio_edit_insertion_order_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->ssio_insertion_order_edit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **ssio_edit_insertion_order_request** | [**SSIOEditInsertionOrderRequest**](SSIOEditInsertionOrderRequest.md)| Order line to create. |

### Return type

[**SSIOEditInsertionOrderResponse**](SSIOEditInsertionOrderResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssio_insertion_orders_status_get_by_ad_account**
> bool, date, datetime, dict, float, int, list, str, none_type ssio_insertion_orders_status_get_by_ad_account(ad_account_id)

Get insertion order status by ad account id.

Get insertion order status for account id <code>ad_account_id</code>. - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a>: Admin, Finance, Campaign.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import billing_api
from openapi_generated.pinterest_client.model.ssio_insertion_order_status import SSIOInsertionOrderStatus
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
    api_instance = billing_api.BillingApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get insertion order status by ad account id.
        api_response = api_instance.ssio_insertion_orders_status_get_by_ad_account(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->ssio_insertion_orders_status_get_by_ad_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get insertion order status by ad account id.
        api_response = api_instance.ssio_insertion_orders_status_get_by_ad_account(ad_account_id, bookmark=bookmark, page_size=page_size)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->ssio_insertion_orders_status_get_by_ad_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
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
**400** | Invalid request parameter. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssio_insertion_orders_status_get_by_pin_order_id**
> SSIOInsertionOrderStatusResponse ssio_insertion_orders_status_get_by_pin_order_id(ad_account_id, pin_order_id)

Get insertion order status by pin order id.

Get insertion order status for pin order id <code>pin_order_id</code>. - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a>: Admin, Finance, Campaign.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import billing_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ssio_insertion_order_status_response import SSIOInsertionOrderStatusResponse
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
    api_instance = billing_api.BillingApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    pin_order_id = "0Q01N0000015hekSVDFDC" # str | The pin order id associated with the ssio insertion order

    # example passing only required values which don't have defaults set
    try:
        # Get insertion order status by pin order id.
        api_response = api_instance.ssio_insertion_orders_status_get_by_pin_order_id(ad_account_id, pin_order_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->ssio_insertion_orders_status_get_by_pin_order_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **pin_order_id** | **str**| The pin order id associated with the ssio insertion order |

### Return type

[**SSIOInsertionOrderStatusResponse**](SSIOInsertionOrderStatusResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request parameter. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssio_order_lines_get_by_ad_account**
> bool, date, datetime, dict, float, int, list, str, none_type ssio_order_lines_get_by_ad_account(ad_account_id)

Get Salesforce order lines by ad account id.

Get Salesforce order lines for account id <code>ad_account_id</code>. - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a>: Admin, Finance, Campaign.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import billing_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ssio_order_line import SSIOOrderLine
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
    api_instance = billing_api.BillingApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    pin_order_id = "0Q01N0000015hekSVDFDC" # str | The pin order id associated with the ssio insertino order (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Salesforce order lines by ad account id.
        api_response = api_instance.ssio_order_lines_get_by_ad_account(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->ssio_order_lines_get_by_ad_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Salesforce order lines by ad account id.
        api_response = api_instance.ssio_order_lines_get_by_ad_account(ad_account_id, bookmark=bookmark, page_size=page_size, pin_order_id=pin_order_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BillingApi->ssio_order_lines_get_by_ad_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **pin_order_id** | **str**| The pin order id associated with the ssio insertino order | [optional]

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
**400** | Invalid request parameter. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

