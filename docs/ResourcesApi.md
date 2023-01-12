# openapi_generated.pinterest_client.ResourcesApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ad_account_countries_get**](ResourcesApi.md#ad_account_countries_get) | **GET** /resources/ad_account_countries | Get ad accounts countries
[**delivery_metrics_get**](ResourcesApi.md#delivery_metrics_get) | **GET** /resources/delivery_metrics | Get available metrics&#39; definitions
[**interest_targeting_options_get**](ResourcesApi.md#interest_targeting_options_get) | **GET** /resources/targeting/interests/{interest_id} | Get interest details
[**metrics_ready_state_get**](ResourcesApi.md#metrics_ready_state_get) | **GET** /resources/metrics_ready_state | Get metrics ready state
[**targeting_options_get**](ResourcesApi.md#targeting_options_get) | **GET** /resources/targeting/{targeting_type} | Get targeting options


# **ad_account_countries_get**
> AdAccountsCountryResponse ad_account_countries_get()

Get ad accounts countries

Get Ad Accounts countries

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import resources_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.ad_accounts_country_response import AdAccountsCountryResponse
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
    api_instance = resources_api.ResourcesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get ad accounts countries
        api_response = api_instance.ad_account_countries_get()
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ResourcesApi->ad_account_countries_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AdAccountsCountryResponse**](AdAccountsCountryResponse.md)

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

# **delivery_metrics_get**
> DeliveryMetricsResponse delivery_metrics_get()

Get available metrics' definitions

Get the definitions for ads and organic metrics available across both synchronous and asynchronous report endpoints. The `display_name` attribute will match how the metric is named in our native tools like Ads Manager. See <a href='/docs/content/analytics/'>Organic Analytics</a> and <a href='/docs/ads/ad-analytics-reporting/'>Ads Analytics</a> for more information.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import resources_api
from openapi_generated.pinterest_client.model.delivery_metrics_response import DeliveryMetricsResponse
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
    api_instance = resources_api.ResourcesApi(api_client)
    report_type = "SYNC" # str | Report type. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get available metrics' definitions
        api_response = api_instance.delivery_metrics_get(report_type=report_type)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ResourcesApi->delivery_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_type** | **str**| Report type. | [optional]

### Return type

[**DeliveryMetricsResponse**](DeliveryMetricsResponse.md)

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

# **interest_targeting_options_get**
> SingleInterestTargetingOptionResponse interest_targeting_options_get(interest_id)

Get interest details

<p>Get details of a specific interest given interest ID.</p> <p>Click <a href=\"https://docs.google.com/spreadsheets/d/1HxL-0Z3p2fgxis9YBP2HWC3tvPrs1hAuHDRtH-NJTIM/edit#gid=118370875\" target=\"_blank\">here</a> for a spreadsheet listing interests and their IDs.</p>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import resources_api
from openapi_generated.pinterest_client.model.single_interest_targeting_option_response import SingleInterestTargetingOptionResponse
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
    api_instance = resources_api.ResourcesApi(api_client)
    interest_id = "4" # str | Unique identifier of an interest.

    # example passing only required values which don't have defaults set
    try:
        # Get interest details
        api_response = api_instance.interest_targeting_options_get(interest_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ResourcesApi->interest_targeting_options_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interest_id** | **str**| Unique identifier of an interest. |

### Return type

[**SingleInterestTargetingOptionResponse**](SingleInterestTargetingOptionResponse.md)

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

# **metrics_ready_state_get**
> BookClosedResponse metrics_ready_state_get(date)

Get metrics ready state

Learn whether conversion or non-conversion metrics are finalized and ready to query.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import resources_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.book_closed_response import BookClosedResponse
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
    api_instance = resources_api.ResourcesApi(api_client)
    date = "2022-07-13" # str | Analytics reports request date (UTC). Format: YYYY-MM-DD

    # example passing only required values which don't have defaults set
    try:
        # Get metrics ready state
        api_response = api_instance.metrics_ready_state_get(date)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ResourcesApi->metrics_ready_state_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **str**| Analytics reports request date (UTC). Format: YYYY-MM-DD |

### Return type

[**BookClosedResponse**](BookClosedResponse.md)

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

# **targeting_options_get**
> TargetingOptionResponse targeting_options_get(targeting_type)

Get targeting options

<p>You can use targeting values in ads placement to define your intended audience. </p> <p>Targeting metrics are organized around targeting specifications.</p> <p>For more information on ads targeting, see <a class=\"reference external\" href=\"https://help.pinterest.com/en/business/article/audience-targeting\" target=\"_blank\">Audience targeting</a>.</p> <p><b>Sample return:</b></p> <pre class=\"literal-block\"> [{&quot;36313&quot;: &quot;Australia: Moreton Bay - North&quot;, &quot;124735&quot;: &quot;Canada: North Battleford&quot;, &quot;36109&quot;: &quot;Australia: Murray&quot;, &quot;36108&quot;: &quot;Australia: Mid North Coast&quot;, &quot;36101&quot;: &quot;Australia: Capital Region&quot;, &quot;811&quot;: &quot;U.S.: Reno&quot;, &quot;36103&quot;: &quot;Australia: Central West&quot;, &quot;36102&quot;: &quot;Australia: Central Coast&quot;, &quot;36105&quot;: &quot;Australia: Far West and Orana&quot;, &quot;36104&quot;: &quot;Australia: Coffs Harbour - Grafton&quot;, &quot;36107&quot;: &quot;Australia: Illawarra&quot;, &quot;36106&quot;: &quot;Australia: Hunter Valley Exc Newcastle&quot;, &quot;554017&quot;: &quot;New Zealand: Wanganui&quot;, &quot;554016&quot;: &quot;New Zealand: Marlborough&quot;, &quot;554015&quot;: &quot;New Zealand: Gisborne&quot;, &quot;554014&quot;: &quot;New Zealand: Tararua&quot;, &quot;554013&quot;: &quot;New Zealand: Invercargill&quot;, &quot;GR&quot;: &quot;Greece&quot;, &quot;554011&quot;: &quot;New Zealand: Whangarei&quot;, &quot;554010&quot;: &quot;New Zealand: Far North&quot;, &quot;717&quot;: &quot;U.S.: Quincy-Hannibal-Keokuk&quot;, &quot;716&quot;: &quot;U.S.: Baton Rouge&quot;,...}] </pre>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import resources_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.targeting_option_response import TargetingOptionResponse
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
    api_instance = resources_api.ResourcesApi(api_client)
    targeting_type = "APPTYPE" # str | Public targeting type.
    client_id = "1094834" # str | Client ID. (optional)
    oauth_signature = "8209f" # str | Oauth signature (optional)
    timestamp = "1618338184277" # str | Timestamp (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get targeting options
        api_response = api_instance.targeting_options_get(targeting_type)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ResourcesApi->targeting_options_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get targeting options
        api_response = api_instance.targeting_options_get(targeting_type, client_id=client_id, oauth_signature=oauth_signature, timestamp=timestamp)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ResourcesApi->targeting_options_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targeting_type** | **str**| Public targeting type. |
 **client_id** | **str**| Client ID. | [optional]
 **oauth_signature** | **str**| Oauth signature | [optional]
 **timestamp** | **str**| Timestamp | [optional]

### Return type

[**TargetingOptionResponse**](TargetingOptionResponse.md)

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

