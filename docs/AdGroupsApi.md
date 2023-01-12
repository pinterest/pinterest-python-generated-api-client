# openapi_generated.pinterest_client.AdGroupsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ad_groups_analytics**](AdGroupsApi.md#ad_groups_analytics) | **GET** /ad_accounts/{ad_account_id}/ad_groups/analytics | Get ad group analytics
[**ad_groups_bid_floor_get**](AdGroupsApi.md#ad_groups_bid_floor_get) | **POST** /ad_accounts/{ad_account_id}/bid_floor | Get bid floors
[**ad_groups_create**](AdGroupsApi.md#ad_groups_create) | **POST** /ad_accounts/{ad_account_id}/ad_groups | Create ad groups
[**ad_groups_get**](AdGroupsApi.md#ad_groups_get) | **GET** /ad_accounts/{ad_account_id}/ad_groups/{ad_group_id} | Get ad group
[**ad_groups_list**](AdGroupsApi.md#ad_groups_list) | **GET** /ad_accounts/{ad_account_id}/ad_groups | List ad groups
[**ad_groups_targeting_analytics_get**](AdGroupsApi.md#ad_groups_targeting_analytics_get) | **GET** /ad_accounts/{ad_account_id}/ad_groups/targeting_analytics | Get targeting analytics for ad groups
[**ad_groups_update**](AdGroupsApi.md#ad_groups_update) | **PATCH** /ad_accounts/{ad_account_id}/ad_groups | Update ad groups


# **ad_groups_analytics**
> AdGroupsAnalyticsResponse ad_groups_analytics(ad_account_id, start_date, end_date, ad_group_ids, columns, granularity)

Get ad group analytics

Get analytics for the specified ad groups in the specified <code>ad_account_id</code>, filtered by the specified options. - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a>: Admin, Analyst, Campaign Manager.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import ad_groups_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ad_groups_analytics_response import AdGroupsAnalyticsResponse
from openapi_generated.pinterest_client.model.granularity import Granularity
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    start_date = dateutil_parser('1970-01-01').date() # date | Metric report start date (UTC). Format: YYYY-MM-DD
    end_date = dateutil_parser('1970-01-01').date() # date | Metric report end date (UTC). Format: YYYY-MM-DD
    ad_group_ids = [
        "4",
    ] # [str] | List of Ad group Ids to use to filter the results.
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
        # Get ad group analytics
        api_response = api_instance.ad_groups_analytics(ad_account_id, start_date, end_date, ad_group_ids, columns, granularity)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdGroupsApi->ad_groups_analytics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get ad group analytics
        api_response = api_instance.ad_groups_analytics(ad_account_id, start_date, end_date, ad_group_ids, columns, granularity, click_window_days=click_window_days, engagement_window_days=engagement_window_days, view_window_days=view_window_days, conversion_report_time=conversion_report_time)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdGroupsApi->ad_groups_analytics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **start_date** | **date**| Metric report start date (UTC). Format: YYYY-MM-DD |
 **end_date** | **date**| Metric report end date (UTC). Format: YYYY-MM-DD |
 **ad_group_ids** | **[str]**| List of Ad group Ids to use to filter the results. |
 **columns** | **[str]**| Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO_DOLLARS returns a value based on the advertiser profile&#39;s currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it&#39;s microdollars. Otherwise, it&#39;s in microunits of the advertiser&#39;s currency.&lt;br/&gt;For example, if the advertiser&#39;s currency is GBP (British pound sterling), all MICRO_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).&lt;br/&gt;If a column has no value, it may not be returned |
 **granularity** | **Granularity**| TOTAL - metrics are aggregated over the specified date range.&lt;br&gt; DAY - metrics are broken down daily.&lt;br&gt; HOUR - metrics are broken down hourly.&lt;br&gt;WEEKLY - metrics are broken down weekly.&lt;br&gt;MONTHLY - metrics are broken down monthly |
 **click_window_days** | **int**| Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;30&#x60; days. | [optional] if omitted the server will use the default value of 30
 **engagement_window_days** | **int**| Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;30&#x60; days. | [optional] if omitted the server will use the default value of 30
 **view_window_days** | **int**| Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;1&#x60; day. | [optional] if omitted the server will use the default value of 1
 **conversion_report_time** | **str**| The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. | [optional] if omitted the server will use the default value of "TIME_OF_AD_ACTION"

### Return type

[**AdGroupsAnalyticsResponse**](AdGroupsAnalyticsResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid ad account group analytics parameters. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ad_groups_bid_floor_get**
> BidFloor ad_groups_bid_floor_get(ad_account_id, bid_floor_request)

Get bid floors

List bid floors for your campaign configuration. Bid floors are given in microcurrency values based on the currency in the bid floor specification. <p/> <p>Microcurrency is used to track very small transactions, based on the currency set in the advertiser’s profile.</p> <p>A microcurrency unit is 10^(-6) of the standard unit of currency selected in the advertiser’s profile.</p> <p><strong>Equivalency equations</strong>, using dollars as an example currency:</p> <ul>   <li>$1 = 1,000,000 microdollars</li>   <li>1 microdollar = $0.000001 </li> </ul> <p><strong>To convert between currency and microcurrency</strong>, using dollars as an example currency:</p> <ul>   <li>To convert dollars to microdollars, mutiply dollars by 1,000,000</li>   <li>To convert microdollars to dollars, divide microdollars by 1,000,000</li> </ul> For more on bid floors see <a class=\"reference external\" href=\"https://help.pinterest.com/en/business/article/set-your-bid\"> Set your bid</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import ad_groups_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.bid_floor import BidFloor
from openapi_generated.pinterest_client.model.bid_floor_request import BidFloorRequest
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    bid_floor_request = BidFloorRequest(
        bid_floor_specs=[
            BidFloorSpec(
                countries=[
                    Country("US"),
                ],
                currency=Currency("USD"),
                objective_type=ObjectiveType("AWARENESS"),
                billable_event=ActionType("CLICKTHROUGH"),
                optimization_goal_metadata=OptimizationGoalMetadata(
                    conversion_tag_v3_goal_metadata=OptimizationGoalMetadataConversionTagV3GoalMetadata(
                        attribution_windows=OptimizationGoalMetadataConversionTagV3GoalMetadataAttributionWindows(
                            click_window_days=1,
                            engagement_window_days=1,
                            view_window_days=1,
                        ),
                        conversion_event="PAGE_VISIT",
                        conversion_tag_id="4",
                        cpa_goal_value_in_micro_currency="4",
                        is_roas_optimized=True,
                        learning_mode_type="ACTIVE",
                    ),
                    frequency_goal_metadata=OptimizationGoalMetadataFrequencyGoalMetadata(
                        frequency=1,
                        timerange="DAY",
                    ),
                    scrollup_goal_metadata=OptimizationGoalMetadataScrollupGoalMetadata(
                        scrollup_goal_value_in_micro_currency="4",
                    ),
                ),
                creative_type=CreativeType("REGULAR"),
            ),
        ],
        targeting_spec=TargetingSpec1(
            age_bucket=["25-34"],
            apptype=["iphone"],
            audience_exclude=["2542620905475"],
            audience_include=["2542620905473"],
            gender=["male"],
            geo=["BE-VOV"],
            interest=["925056443165"],
            locale=["cs"],
            location=["US"],
            shopping_retargeting=[
                TargetingSpecSHOPPINGRETARGETING(
                    lookback_window=30,
                    tag_types=[0,6],
                    exclusion_window=14,
                ),
            ],
            targeting_strategy=["CHOOSE_YOUR_OWN"],
        ),
    ) # BidFloorRequest | Parameters to get bid_floor info

    # example passing only required values which don't have defaults set
    try:
        # Get bid floors
        api_response = api_instance.ad_groups_bid_floor_get(ad_account_id, bid_floor_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdGroupsApi->ad_groups_bid_floor_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **bid_floor_request** | [**BidFloorRequest**](BidFloorRequest.md)| Parameters to get bid_floor info |

### Return type

[**BidFloor**](BidFloor.md)

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

# **ad_groups_create**
> AdGroupArrayResponse ad_groups_create(ad_account_id, ad_group_create_request)

Create ad groups

Create multiple new ad groups. All ads in a given ad group will have the same budget, bid, run dates, targeting, and placement (search, browse, other). For more information, <a href=\"https://help.pinterest.com/en/business/article/campaign-structure\" target=\"_blank\"> click here</a>.</p> <strong>Note:</strong> - 'bid_in_micro_currency' and 'budget_in_micro_currency' should be expressed in microcurrency amounts based on the currency field set in the advertiser's profile.<p/> <p>Microcurrency is used to track very small transactions, based on the currency set in the advertiser’s profile.</p> <p>A microcurrency unit is 10^(-6) of the standard unit of currency selected in the advertiser’s profile.</p> <p><strong>Equivalency equations</strong>, using dollars as an example currency:</p> <ul>   <li>$1 = 1,000,000 microdollars</li>   <li>1 microdollar = $0.000001 </li> </ul> <p><strong>To convert between currency and microcurrency</strong>, using dollars as an example currency:</p> <ul>   <li>To convert dollars to microdollars, mutiply dollars by 1,000,000</li>   <li>To convert microdollars to dollars, divide microdollars by 1,000,000</li> </ul> - Ad groups belong to ad campaigns. Some types of campaigns (e.g. budget optimization) have limits on the number of ad groups they can hold. If you exceed those limits, you will get an error message.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import ad_groups_api
from openapi_generated.pinterest_client.model.ad_group_create_request import AdGroupCreateRequest
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ad_group_array_response import AdGroupArrayResponse
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    ad_group_create_request = [
        AdGroupCreateRequest(None),
    ] # [AdGroupCreateRequest] | List of ad groups to create, size limit [1, 30].

    # example passing only required values which don't have defaults set
    try:
        # Create ad groups
        api_response = api_instance.ad_groups_create(ad_account_id, ad_group_create_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdGroupsApi->ad_groups_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **ad_group_create_request** | [**[AdGroupCreateRequest]**](AdGroupCreateRequest.md)| List of ad groups to create, size limit [1, 30]. |

### Return type

[**AdGroupArrayResponse**](AdGroupArrayResponse.md)

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

# **ad_groups_get**
> AdGroupResponse ad_groups_get(ad_account_id, ad_group_id)

Get ad group

Get a specific ad given the ad ID. If your pin is rejected, rejected_reasons will contain additional information from the Ad Review process. For more information about our policies and rejection reasons see the <a href=\"https://www.pinterest.com/_/_/policy/advertising-guidelines/\" target=\"_blank\">Pinterest advertising standards</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import ad_groups_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ad_group_response import AdGroupResponse
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    ad_group_id = "4" # str | Unique identifier of an ad group.

    # example passing only required values which don't have defaults set
    try:
        # Get ad group
        api_response = api_instance.ad_groups_get(ad_account_id, ad_group_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdGroupsApi->ad_groups_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **ad_group_id** | **str**| Unique identifier of an ad group. |

### Return type

[**AdGroupResponse**](AdGroupResponse.md)

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

# **ad_groups_list**
> bool, date, datetime, dict, float, int, list, str, none_type ad_groups_list(ad_account_id)

List ad groups

List ad groups based on provided campaign IDs or ad group IDs.(campaign_ids or ad_group_ids). <p/> <strong>Note:</strong><p/> Provide only campaign_id or ad_group_id. Do not provide both.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import ad_groups_api
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    campaign_ids = [
        "4",
    ] # [str] | List of Campaign Ids to use to filter the results. (optional)
    ad_group_ids = [
        "4",
    ] # [str] | List of Ad group Ids to use to filter the results. (optional)
    entity_statuses = [
        "ACTIVE",
    ] # [str] | Entity status (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/getting-started/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    order = "ASCENDING" # str | The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. (optional)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    translate_interests_to_names = False # bool | Return interests as text names (if value is true) rather than topic IDs. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # List ad groups
        api_response = api_instance.ad_groups_list(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdGroupsApi->ad_groups_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List ad groups
        api_response = api_instance.ad_groups_list(ad_account_id, campaign_ids=campaign_ids, ad_group_ids=ad_group_ids, entity_statuses=entity_statuses, page_size=page_size, order=order, bookmark=bookmark, translate_interests_to_names=translate_interests_to_names)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdGroupsApi->ad_groups_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **campaign_ids** | **[str]**| List of Campaign Ids to use to filter the results. | [optional]
 **ad_group_ids** | **[str]**| List of Ad group Ids to use to filter the results. | [optional]
 **entity_statuses** | **[str]**| Entity status | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/getting-started/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **order** | **str**| The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. | [optional]
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **translate_interests_to_names** | **bool**| Return interests as text names (if value is true) rather than topic IDs. | [optional] if omitted the server will use the default value of False

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
**400** | Invalid ad account group parameters. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ad_groups_targeting_analytics_get**
> MetricsResponse ad_groups_targeting_analytics_get(ad_account_id, ad_group_ids, start_date, end_date, targeting_types, columns, granularity)

Get targeting analytics for ad groups

Get targeting analytics for one or more ad groups. For the requested ad group(s) and metrics, the response will include the requested metric information (e.g. SPEND_IN_DOLLAR) for the requested target type (e.g. \"age_bucket\") for applicable values (e.g. \"45-49\"). <p/> - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a>: Admin, Analyst, Campaign Manager.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import ad_groups_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.granularity import Granularity
from openapi_generated.pinterest_client.model.ads_analytics_targeting_type import AdsAnalyticsTargetingType
from openapi_generated.pinterest_client.model.conversion_report_attribution_type import ConversionReportAttributionType
from openapi_generated.pinterest_client.model.metrics_response import MetricsResponse
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    ad_group_ids = [
        "4",
    ] # [str] | List of Ad group Ids to use to filter the results.
    start_date = dateutil_parser('1970-01-01').date() # date | Metric report start date (UTC). Format: YYYY-MM-DD
    end_date = dateutil_parser('1970-01-01').date() # date | Metric report end date (UTC). Format: YYYY-MM-DD
    targeting_types = [
        AdsAnalyticsTargetingType("APPTYPE"),
    ] # [AdsAnalyticsTargetingType] | Targeting type breakdowns for the report. The reporting per targeting type <br> is independent from each other.
    columns = [
        "SPEND_IN_DOLLAR",
    ] # [str] | Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.<br/>For example, if the advertiser's currency is GBP (British pound sterling), all MICRO_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).<br/>If a column has no value, it may not be returned
    granularity = Granularity("DAY") # Granularity | TOTAL - metrics are aggregated over the specified date range.<br> DAY - metrics are broken down daily.<br> HOUR - metrics are broken down hourly.<br>WEEKLY - metrics are broken down weekly.<br>MONTHLY - metrics are broken down monthly
    click_window_days = 1 # int | Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. (optional) if omitted the server will use the default value of 30
    engagement_window_days = 30 # int | Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. (optional) if omitted the server will use the default value of 30
    view_window_days = 1 # int | Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. (optional) if omitted the server will use the default value of 1
    conversion_report_time = "TIME_OF_AD_ACTION" # str | The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. (optional) if omitted the server will use the default value of "TIME_OF_AD_ACTION"
    attribution_types = ConversionReportAttributionType("INDIVIDUAL") # ConversionReportAttributionType | List of types of attribution for the conversion report (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get targeting analytics for ad groups
        api_response = api_instance.ad_groups_targeting_analytics_get(ad_account_id, ad_group_ids, start_date, end_date, targeting_types, columns, granularity)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdGroupsApi->ad_groups_targeting_analytics_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get targeting analytics for ad groups
        api_response = api_instance.ad_groups_targeting_analytics_get(ad_account_id, ad_group_ids, start_date, end_date, targeting_types, columns, granularity, click_window_days=click_window_days, engagement_window_days=engagement_window_days, view_window_days=view_window_days, conversion_report_time=conversion_report_time, attribution_types=attribution_types)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdGroupsApi->ad_groups_targeting_analytics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **ad_group_ids** | **[str]**| List of Ad group Ids to use to filter the results. |
 **start_date** | **date**| Metric report start date (UTC). Format: YYYY-MM-DD |
 **end_date** | **date**| Metric report end date (UTC). Format: YYYY-MM-DD |
 **targeting_types** | [**[AdsAnalyticsTargetingType]**](AdsAnalyticsTargetingType.md)| Targeting type breakdowns for the report. The reporting per targeting type &lt;br&gt; is independent from each other. |
 **columns** | **[str]**| Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO_DOLLARS returns a value based on the advertiser profile&#39;s currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it&#39;s microdollars. Otherwise, it&#39;s in microunits of the advertiser&#39;s currency.&lt;br/&gt;For example, if the advertiser&#39;s currency is GBP (British pound sterling), all MICRO_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).&lt;br/&gt;If a column has no value, it may not be returned |
 **granularity** | **Granularity**| TOTAL - metrics are aggregated over the specified date range.&lt;br&gt; DAY - metrics are broken down daily.&lt;br&gt; HOUR - metrics are broken down hourly.&lt;br&gt;WEEKLY - metrics are broken down weekly.&lt;br&gt;MONTHLY - metrics are broken down monthly |
 **click_window_days** | **int**| Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;30&#x60; days. | [optional] if omitted the server will use the default value of 30
 **engagement_window_days** | **int**| Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;30&#x60; days. | [optional] if omitted the server will use the default value of 30
 **view_window_days** | **int**| Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;1&#x60; day. | [optional] if omitted the server will use the default value of 1
 **conversion_report_time** | **str**| The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. | [optional] if omitted the server will use the default value of "TIME_OF_AD_ACTION"
 **attribution_types** | **ConversionReportAttributionType**| List of types of attribution for the conversion report | [optional]

### Return type

[**MetricsResponse**](MetricsResponse.md)

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

# **ad_groups_update**
> AdGroupArrayResponse ad_groups_update(ad_account_id, ad_group_update_request)

Update ad groups

Update multiple existing ad groups.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import ad_groups_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ad_group_update_request import AdGroupUpdateRequest
from openapi_generated.pinterest_client.model.ad_group_array_response import AdGroupArrayResponse
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
    api_instance = ad_groups_api.AdGroupsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    ad_group_update_request = [
        AdGroupUpdateRequest(None),
    ] # [AdGroupUpdateRequest] | List of ad groups to update, size limit [1, 30].

    # example passing only required values which don't have defaults set
    try:
        # Update ad groups
        api_response = api_instance.ad_groups_update(ad_account_id, ad_group_update_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AdGroupsApi->ad_groups_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **ad_group_update_request** | [**[AdGroupUpdateRequest]**](AdGroupUpdateRequest.md)| List of ad groups to update, size limit [1, 30]. |

### Return type

[**AdGroupArrayResponse**](AdGroupArrayResponse.md)

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

