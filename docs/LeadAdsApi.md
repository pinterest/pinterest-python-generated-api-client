# openapi_generated.pinterest_client.LeadAdsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ad_accounts_subscriptions_del_by_id**](LeadAdsApi.md#ad_accounts_subscriptions_del_by_id) | **DELETE** /ad_accounts/{ad_account_id}/leads/subscriptions/{subscription_id} | Delete lead ads subscription
[**ad_accounts_subscriptions_get_by_id**](LeadAdsApi.md#ad_accounts_subscriptions_get_by_id) | **GET** /ad_accounts/{ad_account_id}/leads/subscriptions/{subscription_id} | Get lead ads subscription
[**ad_accounts_subscriptions_get_list**](LeadAdsApi.md#ad_accounts_subscriptions_get_list) | **GET** /ad_accounts/{ad_account_id}/leads/subscriptions | Get lead ads subscriptions
[**ad_accounts_subscriptions_post**](LeadAdsApi.md#ad_accounts_subscriptions_post) | **POST** /ad_accounts/{ad_account_id}/leads/subscriptions | Create lead ads subscription


# **ad_accounts_subscriptions_del_by_id**
> ad_accounts_subscriptions_del_by_id(ad_account_id, subscription_id)

Delete lead ads subscription

Delete an existing lead ads webhook subscription by ID. - Only requests for the OWNER or ADMIN of the ad_account will be allowed.  <strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.</strong>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import lead_ads_api
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
    api_instance = lead_ads_api.LeadAdsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    subscription_id = "4" # str | Unique identifier of a subscription.

    # example passing only required values which don't have defaults set
    try:
        # Delete lead ads subscription
        api_instance.ad_accounts_subscriptions_del_by_id(ad_account_id, subscription_id)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadAdsApi->ad_accounts_subscriptions_del_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **subscription_id** | **str**| Unique identifier of a subscription. |

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
**204** | Subscription deleted successfully |  -  |
**400** | Invalid input parameters. |  -  |
**403** | You are not authorized to delete this subscription. |  -  |
**404** | Subscription not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ad_accounts_subscriptions_get_by_id**
> AdAccountGetSubscriptionResponse ad_accounts_subscriptions_get_by_id(ad_account_id, subscription_id)

Get lead ads subscription

Get a specific lead ads subscription record. - Only requests for the OWNER or ADMIN of the ad_account will be allowed.  <strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.</strong>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import lead_ads_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ad_account_get_subscription_response import AdAccountGetSubscriptionResponse
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
    api_instance = lead_ads_api.LeadAdsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    subscription_id = "4" # str | Unique identifier of a subscription.

    # example passing only required values which don't have defaults set
    try:
        # Get lead ads subscription
        api_response = api_instance.ad_accounts_subscriptions_get_by_id(ad_account_id, subscription_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadAdsApi->ad_accounts_subscriptions_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **subscription_id** | **str**| Unique identifier of a subscription. |

### Return type

[**AdAccountGetSubscriptionResponse**](AdAccountGetSubscriptionResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid input parameters. |  -  |
**403** | Can&#39;t access this subscription. |  -  |
**404** | Subscription not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ad_accounts_subscriptions_get_list**
> bool, date, datetime, dict, float, int, list, str, none_type ad_accounts_subscriptions_get_list(ad_account_id)

Get lead ads subscriptions

Get the advertiser's list of lead ads subscriptions. - Only requests for the OWNER or ADMIN of the ad_account will be allowed.  <strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.</strong>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import lead_ads_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ad_account_get_subscription_response import AdAccountGetSubscriptionResponse
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
    api_instance = lead_ads_api.LeadAdsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get lead ads subscriptions
        api_response = api_instance.ad_accounts_subscriptions_get_list(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadAdsApi->ad_accounts_subscriptions_get_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get lead ads subscriptions
        api_response = api_instance.ad_accounts_subscriptions_get_list(ad_account_id, page_size=page_size, bookmark=bookmark)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadAdsApi->ad_accounts_subscriptions_get_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
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
**403** | Can&#39;t access this subscription. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ad_accounts_subscriptions_post**
> AdAccountCreateSubscriptionResponse ad_accounts_subscriptions_post(ad_account_id, ad_account_create_subscription_request)

Create lead ads subscription

Create a lead ads webhook subscription. Subscriptions allow Pinterest to deliver lead data from Ads Manager directly to the subscriber. Subscriptions can exist for a specific lead form or at ad account level. - Only requests for the OWNER or ADMIN of the ad_account will be allowed. - Advertisers can set up multiple integrations using ad_account_id + lead_form_id but only one integration per unique records. - For data security, egress lead data is encrypted with AES-256-GCM.  <strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.</strong>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import lead_ads_api
from openapi_generated.pinterest_client.model.ad_account_create_subscription_response import AdAccountCreateSubscriptionResponse
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ad_account_create_subscription_request import AdAccountCreateSubscriptionRequest
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
    api_instance = lead_ads_api.LeadAdsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    ad_account_create_subscription_request = AdAccountCreateSubscriptionRequest(
        webhook_url="https://webhook.example.com/xyz",
        lead_form_id="383791336903426390",
        partner_access_token="partner_access_token_example",
        partner_refresh_token="partner_refresh_token_example",
        partner_metadata=AdAccountCreateSubscriptionRequestPartnerMetadata(
            subscriber_key="subscriber_key_example",
        ),
    ) # AdAccountCreateSubscriptionRequest | Subscription to create.

    # example passing only required values which don't have defaults set
    try:
        # Create lead ads subscription
        api_response = api_instance.ad_accounts_subscriptions_post(ad_account_id, ad_account_create_subscription_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadAdsApi->ad_accounts_subscriptions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **ad_account_create_subscription_request** | [**AdAccountCreateSubscriptionRequest**](AdAccountCreateSubscriptionRequest.md)| Subscription to create. |

### Return type

[**AdAccountCreateSubscriptionResponse**](AdAccountCreateSubscriptionResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid input parameters. |  -  |
**403** | Can&#39;t access this subscription. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

