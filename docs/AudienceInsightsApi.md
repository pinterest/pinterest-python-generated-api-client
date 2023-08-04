# openapi_generated.pinterest_client.AudienceInsightsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audience_insights_get**](AudienceInsightsApi.md#audience_insights_get) | **GET** /ad_accounts/{ad_account_id}/audience_insights | Get audience insights
[**audience_insights_scope_and_type_get**](AudienceInsightsApi.md#audience_insights_scope_and_type_get) | **GET** /ad_accounts/{ad_account_id}/insights/audiences | Get audience insights scope and type
[**audiences_insights_category_list**](AudienceInsightsApi.md#audiences_insights_category_list) | **GET** /ad_accounts/{ad_account_id}/insights/audiences/{scope}/{type}/{category_id} | Get category sub-interest (DEPRECATED)


# **audience_insights_get**
> AudienceInsightsResponse audience_insights_get(ad_account_id, audience_insight_type)

Get audience insights

Get Audience Insights for an ad account. The response will return insights for 3 types of audiences: the ad account's engaged audience on Pinterest, the ad account's total audience on Pinterest and Pinterest's total audience.<p/> <a href=\"https://help.pinterest.com/en/business/article/audience-insights\" target=\"_blank\">Learn more about Audience Insights</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import audience_insights_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.audience_insights_response import AudienceInsightsResponse
from openapi_generated.pinterest_client.model.audience_insight_type import AudienceInsightType
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
    api_instance = audience_insights_api.AudienceInsightsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    audience_insight_type = AudienceInsightType("YOUR_TOTAL_AUDIENCE") # AudienceInsightType | Type of audience insights.

    # example passing only required values which don't have defaults set
    try:
        # Get audience insights
        api_response = api_instance.audience_insights_get(ad_account_id, audience_insight_type)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceInsightsApi->audience_insights_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **audience_insight_type** | **AudienceInsightType**| Type of audience insights. |

### Return type

[**AudienceInsightsResponse**](AudienceInsightsResponse.md)

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

# **audience_insights_scope_and_type_get**
> AudienceDefinitionResponse audience_insights_scope_and_type_get(ad_account_id)

Get audience insights scope and type

Get the scope and type of available audiences, which along with a date, is an audience that has recently had an interaction (referred to here as a type) on pins. Interacted pins can belong to at least the most common **partner** or **Pinterest** scopes. This means that user interactions made on advertiser or partner pins will have the **partner** scope. You can also have user interactions performed in general on Pinterest with the **Pinterest** scope. In that case, you can then use the returned type and scope values together on requests to other endpoints to retrieve insight metrics for a desired audience.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import audience_insights_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.audience_definition_response import AudienceDefinitionResponse
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
    api_instance = audience_insights_api.AudienceInsightsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.

    # example passing only required values which don't have defaults set
    try:
        # Get audience insights scope and type
        api_response = api_instance.audience_insights_scope_and_type_get(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceInsightsApi->audience_insights_scope_and_type_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |

### Return type

[**AudienceDefinitionResponse**](AudienceDefinitionResponse.md)

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

# **audiences_insights_category_list**
> AudienceInsightCategoryArrayResponse audiences_insights_category_list(ad_account_id, scope, type, category_id)

Get category sub-interest (DEPRECATED)

Get information about a category's sub-level interests. For a list of interests, their IDs, and hierarchy, see the [list of interests](https://docs.google.com/spreadsheets/d/1HxL-0Z3p2fgxis9YBP2HWC3tvPrs1hAuHDRtH-NJTIM/edit#gid=118370875). Also, a category is a level-one (L1) interest. For example, in the interest hierarchy see **Animals** > **Mammals** > **Dogs**, **Animals** is the category.  This endpoint has been deprecated.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import audience_insights_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.audience_insight_category_array_response import AudienceInsightCategoryArrayResponse
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
    api_instance = audience_insights_api.AudienceInsightsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    scope = "scope_example" # str | Generated audience scope to request.
    type = "type_example" # str | Generated audience type to request.
    category_id = "4" # str | Category (L1 interest) numeric ID.
    sort = "RATIO" # str | Sort method. Only RATIO is supported. (optional) if omitted the server will use the default value of "RATIO"

    # example passing only required values which don't have defaults set
    try:
        # Get category sub-interest (DEPRECATED)
        api_response = api_instance.audiences_insights_category_list(ad_account_id, scope, type, category_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceInsightsApi->audiences_insights_category_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get category sub-interest (DEPRECATED)
        api_response = api_instance.audiences_insights_category_list(ad_account_id, scope, type, category_id, sort=sort)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling AudienceInsightsApi->audiences_insights_category_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **scope** | **str**| Generated audience scope to request. |
 **type** | **str**| Generated audience type to request. |
 **category_id** | **str**| Category (L1 interest) numeric ID. |
 **sort** | **str**| Sort method. Only RATIO is supported. | [optional] if omitted the server will use the default value of "RATIO"

### Return type

[**AudienceInsightCategoryArrayResponse**](AudienceInsightCategoryArrayResponse.md)

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

