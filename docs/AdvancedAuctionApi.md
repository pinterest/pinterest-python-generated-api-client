# openapi_generated.pinterest_client.AdvancedAuctionApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advanced_auction_items_get_post**](AdvancedAuctionApi.md#advanced_auction_items_get_post) | **POST** /advanced_auction/items/get | Get item bid options (POST)
[**advanced_auction_items_submit_post**](AdvancedAuctionApi.md#advanced_auction_items_submit_post) | **POST** /advanced_auction/items/submit | Operate on item level bid options


# **advanced_auction_items_get_post**
> AdvancedAuctionItems advanced_auction_items_get_post(advanced_auction_items_get_request)

Get item bid options (POST)

Get the bid options for a batch of retail catalog items.  The catalog must be owned by the \"operation user_account\". <a href=\"/docs/api-features/shopping-overview/#Update%20items%20in%20batch\" target=\"_blank\">See detailed documentation here.</a> By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: `Owner`, `Admin`.  This endpoint is not available to all users.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import advanced_auction_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.advanced_auction_items_get_request import AdvancedAuctionItemsGetRequest
from openapi_generated.pinterest_client.model.advanced_auction_items import AdvancedAuctionItems
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
    api_instance = advanced_auction_api.AdvancedAuctionApi(api_client)
    advanced_auction_items_get_request = AdvancedAuctionItemsGetRequest(
        catalog_id="2680059592705",
        items=[
            AdvancedAuctionItemsGetRecord(None),
        ],
    ) # AdvancedAuctionItemsGetRequest | Request object used to get bid options values for a batch of retail catalog items
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get item bid options (POST)
        api_response = api_instance.advanced_auction_items_get_post(advanced_auction_items_get_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdvancedAuctionApi->advanced_auction_items_get_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get item bid options (POST)
        api_response = api_instance.advanced_auction_items_get_post(advanced_auction_items_get_request, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdvancedAuctionApi->advanced_auction_items_get_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advanced_auction_items_get_request** | [**AdvancedAuctionItemsGetRequest**](AdvancedAuctionItemsGetRequest.md)| Request object used to get bid options values for a batch of retail catalog items |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**AdvancedAuctionItems**](AdvancedAuctionItems.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response containing the bid option values for the requested retail catalog items. Items that don&#39;t exist or do not have bid options set won&#39;t be present in the response. |  -  |
**400** | Invalid request parameters. |  -  |
**401** | Not authenticated to get item bid options |  -  |
**403** | Not authorized to get item bid options |  -  |
**500** | Internal error |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **advanced_auction_items_submit_post**
> AdvancedAuctionProcessedItems advanced_auction_items_submit_post(advanced_auction_items_submit_request)

Operate on item level bid options

This endpoint supports multiple operations on a set of one or more bid options (bid price and bid adjustments for targeting categories) for retail catalog items. These advanced auction settings are applied in campaigns using objective_type `CATALOG_SALES` and ad groups using bid_strategy_type `MAX_BID`.  The catalog must be owned by the \"operation user_account\". <a href=\"/docs/api-features/modify-items-in-batch/\" target=\"_blank\">See detailed documentation here.</a> By default, the \"operation user_account\" is the token user_account.  Optional: Business Access: Specify an <code>ad_account_id</code> (obtained via <a href='/docs/api/v5/#operation/ad_accounts/list'>List ad accounts</a>) to use the owner of that ad_account as the \"operation user_account\". In order to do this, the token user_account must have one of the following <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a> roles on the ad_account: `Owner`, `Admin`.  This endpoint is not available to all users.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import advanced_auction_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.advanced_auction_processed_items import AdvancedAuctionProcessedItems
from openapi_generated.pinterest_client.model.advanced_auction_items_submit_request import AdvancedAuctionItemsSubmitRequest
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
    api_instance = advanced_auction_api.AdvancedAuctionApi(api_client)
    advanced_auction_items_submit_request = AdvancedAuctionItemsSubmitRequest(
        catalog_id="2680059592705",
        items=[
            AdvancedAuctionItemsSubmitRecord(
                operation=AdvancedAuctionOperation("UPSERT"),
            ),
        ],
    ) # AdvancedAuctionItemsSubmitRequest | Request object used to upsert or delete bid options for a batch of retail catalog items
    ad_account_id = "4" # str | Unique identifier of an ad account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Operate on item level bid options
        api_response = api_instance.advanced_auction_items_submit_post(advanced_auction_items_submit_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdvancedAuctionApi->advanced_auction_items_submit_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Operate on item level bid options
        api_response = api_instance.advanced_auction_items_submit_post(advanced_auction_items_submit_request, ad_account_id=ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdvancedAuctionApi->advanced_auction_items_submit_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advanced_auction_items_submit_request** | [**AdvancedAuctionItemsSubmitRequest**](AdvancedAuctionItemsSubmitRequest.md)| Request object used to upsert or delete bid options for a batch of retail catalog items |
 **ad_account_id** | **str**| Unique identifier of an ad account. | [optional]

### Return type

[**AdvancedAuctionProcessedItems**](AdvancedAuctionProcessedItems.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response containing the results of the item bid options operations |  -  |
**400** | Invalid request parameters. |  -  |
**401** | Not authenticated to post item bid options |  -  |
**403** | Not authorized to post item bid options |  -  |
**500** | Internal error |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

