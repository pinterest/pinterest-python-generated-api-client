# pinterest.generated.client.AudienceInsightsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audience_insights_get**](AudienceInsightsApi.md#audience_insights_get) | **GET** /ad_accounts/{ad_account_id}/audience_insights | Get audience insights


# **audience_insights_get**
> AudienceInsightsResponse audience_insights_get(ad_account_id, audience_insight_type)

Get audience insights

<strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/ads/ads-management/'>Learn more</a>.</strong> <p/> Get Audience Insights for an ad account. The response will return insights for 3 types of audiences: the ad account's engaged audience on Pinterest, the ad account's total audience on Pinterest and Pinterest's total audience.<p/> <a href=\"https://help.pinterest.com/en/business/article/audience-insights\" target=\"_blank\">Learn more about Audience Insights</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import audience_insights_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.audience_insight_type import AudienceInsightType
from pinterest.generated.client.model.audience_insights_response import AudienceInsightsResponse
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
    api_instance = audience_insights_api.AudienceInsightsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    audience_insight_type = AudienceInsightType("YOUR_TOTAL_AUDIENCE") # AudienceInsightType | Type of audience insights.

    # example passing only required values which don't have defaults set
    try:
        # Get audience insights
        api_response = api_instance.audience_insights_get(ad_account_id, audience_insight_type)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
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

