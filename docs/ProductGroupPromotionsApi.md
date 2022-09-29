# pinterest.generated.client.ProductGroupPromotionsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_group_promotion_get**](ProductGroupPromotionsApi.md#product_group_promotion_get) | **GET** /ad_accounts/{ad_account_id}/product_group_promotions/{product_group_promotion_id} | Get a product group promotion by id
[**product_group_promotions_create**](ProductGroupPromotionsApi.md#product_group_promotions_create) | **POST** /ad_accounts/{ad_account_id}/product_group_promotions | Create product group promotions
[**product_group_promotions_update**](ProductGroupPromotionsApi.md#product_group_promotions_update) | **PATCH** /ad_accounts/{ad_account_id}/product_group_promotions | Update product group promotions
[**product_groups_analytics**](ProductGroupPromotionsApi.md#product_groups_analytics) | **GET** /ad_accounts/{ad_account_id}/product_groups/analytics | Get product group analytics


# **product_group_promotion_get**
> ProductGroupPromotion product_group_promotion_get(ad_account_id, product_group_promotion_id)

Get a product group promotion by id

Get a product group promotion by id

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import product_group_promotions_api
from pinterest.generated.client.model.product_group_promotion import ProductGroupPromotion
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
    api_instance = product_group_promotions_api.ProductGroupPromotionsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    product_group_promotion_id = "4" # str | Unique identifier of a product group promotion

    # example passing only required values which don't have defaults set
    try:
        # Get a product group promotion by id
        api_response = api_instance.product_group_promotion_get(ad_account_id, product_group_promotion_id)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling ProductGroupPromotionsApi->product_group_promotion_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **product_group_promotion_id** | **str**| Unique identifier of a product group promotion |

### Return type

[**ProductGroupPromotion**](ProductGroupPromotion.md)

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

# **product_group_promotions_create**
> ProductGroupPromotionArrayResponse product_group_promotions_create(ad_account_id, product_group_promotion_create_request)

Create product group promotions

Add one or more product groups from your catalog to an existing ad group. (Product groups added to an ad group are a 'product group promotion.')

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import product_group_promotions_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.product_group_promotion_array_response import ProductGroupPromotionArrayResponse
from pinterest.generated.client.model.product_group_promotion_create_request import ProductGroupPromotionCreateRequest
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
    api_instance = product_group_promotions_api.ProductGroupPromotionsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    product_group_promotion_create_request = ProductGroupPromotionCreateRequest(
        ad_group_id="2680059592705",
        product_group_promotion=[
            ProductGroupPromotionCommon(
                status=EntityStatus("ACTIVE"),
                tracking_url="https://www.pinterest.com",
                catalogs_product_group_id="1231235",
                catalogs_product_group_name="catalogProductGroupName",
                creative_type=CreativeType("REGULAR"),
                collections_hero_pin_id="123123",
                collections_hero_destination_url="http://www.pinterest.com",
                slideshow_collections_title="Title",
                slideshow_collections_description="Description",
            ),
        ],
    ) # ProductGroupPromotionCreateRequest | List of Product Group Promotions to create, size limit [1, 30].

    # example passing only required values which don't have defaults set
    try:
        # Create product group promotions
        api_response = api_instance.product_group_promotions_create(ad_account_id, product_group_promotion_create_request)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling ProductGroupPromotionsApi->product_group_promotions_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **product_group_promotion_create_request** | [**ProductGroupPromotionCreateRequest**](ProductGroupPromotionCreateRequest.md)| List of Product Group Promotions to create, size limit [1, 30]. |

### Return type

[**ProductGroupPromotionArrayResponse**](ProductGroupPromotionArrayResponse.md)

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

# **product_group_promotions_update**
> [ProductGroupPromotionUpdateResponseItem] product_group_promotions_update(ad_account_id, product_group_promotion_update_request)

Update product group promotions

Update multiple existing Product Group Promotions (by product_group_id)

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import product_group_promotions_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.product_group_promotion_update_request import ProductGroupPromotionUpdateRequest
from pinterest.generated.client.model.product_group_promotion_update_response_item import ProductGroupPromotionUpdateResponseItem
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
    api_instance = product_group_promotions_api.ProductGroupPromotionsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    product_group_promotion_update_request = ProductGroupPromotionUpdateRequest(
        ad_group_id="2680059592705",
        product_group_promotion=[
            ProductGroupPromotionUpdateItem(None),
        ],
    ) # ProductGroupPromotionUpdateRequest | Parameters to update Product group promotions

    # example passing only required values which don't have defaults set
    try:
        # Update product group promotions
        api_response = api_instance.product_group_promotions_update(ad_account_id, product_group_promotion_update_request)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling ProductGroupPromotionsApi->product_group_promotions_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **product_group_promotion_update_request** | [**ProductGroupPromotionUpdateRequest**](ProductGroupPromotionUpdateRequest.md)| Parameters to update Product group promotions |

### Return type

[**[ProductGroupPromotionUpdateResponseItem]**](ProductGroupPromotionUpdateResponseItem.md)

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

# **product_groups_analytics**
> ProductGroupAnalyticsResponse product_groups_analytics(ad_account_id, start_date, end_date, product_group_ids, columns, granularity)

Get product group analytics

Get analytics for the specified product groups in the specified <code>ad_account_id</code>, filtered by the specified options. - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a>: Admin, Analyst, Campaign Manager.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import product_group_promotions_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.product_group_analytics_response import ProductGroupAnalyticsResponse
from pinterest.generated.client.model.granularity import Granularity
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
    api_instance = product_group_promotions_api.ProductGroupPromotionsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    start_date = dateutil_parser('1970-01-01').date() # date | Metric report start date (UTC). Format: YYYY-MM-DD
    end_date = dateutil_parser('1970-01-01').date() # date | Metric report end date (UTC). Format: YYYY-MM-DD
    product_group_ids = [
        "4",
    ] # [str] | List of Product group Ids to use to filter the results.
    columns = [
        "SPEND_IN_DOLLAR",
    ] # [str] | Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.<br/>For example, if the advertiser's currency is GBP (British pound sterling), all MICRO_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).<br/>If a column has no value, it may not be returned
    granularity = Granularity("DAY") # Granularity | TOTAL - metrics are aggregated over the specified date range.<br> DAY - metrics are broken down daily.<br> HOUR - metrics are broken down hourly.<br>WEEKLY - metrics are broken down weekly.<br>MONTHLY - metrics are broken down monthly
    click_window_days = 1 # int | Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. (optional) if omitted the server will use the default value of 30
    engagement_window_days = 30 # int | Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. (optional) if omitted the server will use the default value of 30
    view_window_days = 1 # int | Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. (optional) if omitted the server will use the default value of 1
    conversion_report_time = "TIME_OF_AD_ACTION" # str | The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. (optional) if omitted the server will use the default value of "TIME_OF_AD_ACTION"

    # example passing only required values which don't have defaults set
    try:
        # Get product group analytics
        api_response = api_instance.product_groups_analytics(ad_account_id, start_date, end_date, product_group_ids, columns, granularity)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling ProductGroupPromotionsApi->product_groups_analytics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get product group analytics
        api_response = api_instance.product_groups_analytics(ad_account_id, start_date, end_date, product_group_ids, columns, granularity, click_window_days=click_window_days, engagement_window_days=engagement_window_days, view_window_days=view_window_days, conversion_report_time=conversion_report_time)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling ProductGroupPromotionsApi->product_groups_analytics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **start_date** | **date**| Metric report start date (UTC). Format: YYYY-MM-DD |
 **end_date** | **date**| Metric report end date (UTC). Format: YYYY-MM-DD |
 **product_group_ids** | **[str]**| List of Product group Ids to use to filter the results. |
 **columns** | **[str]**| Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO_DOLLARS returns a value based on the advertiser profile&#39;s currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it&#39;s microdollars. Otherwise, it&#39;s in microunits of the advertiser&#39;s currency.&lt;br/&gt;For example, if the advertiser&#39;s currency is GBP (British pound sterling), all MICRO_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).&lt;br/&gt;If a column has no value, it may not be returned |
 **granularity** | **Granularity**| TOTAL - metrics are aggregated over the specified date range.&lt;br&gt; DAY - metrics are broken down daily.&lt;br&gt; HOUR - metrics are broken down hourly.&lt;br&gt;WEEKLY - metrics are broken down weekly.&lt;br&gt;MONTHLY - metrics are broken down monthly |
 **click_window_days** | **int**| Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;30&#x60; days. | [optional] if omitted the server will use the default value of 30
 **engagement_window_days** | **int**| Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;30&#x60; days. | [optional] if omitted the server will use the default value of 30
 **view_window_days** | **int**| Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;1&#x60; day. | [optional] if omitted the server will use the default value of 1
 **conversion_report_time** | **str**| The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. | [optional] if omitted the server will use the default value of "TIME_OF_AD_ACTION"

### Return type

[**ProductGroupAnalyticsResponse**](ProductGroupAnalyticsResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid ad account ads analytics parameters. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

