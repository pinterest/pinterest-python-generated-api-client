# openapi_generated.pinterest_client.LeadsExportApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leads_export_create**](LeadsExportApi.md#leads_export_create) | **POST** /ad_accounts/{ad_account_id}/leads_export | Create a request to export leads collected from a lead ad
[**leads_export_get**](LeadsExportApi.md#leads_export_get) | **GET** /ad_accounts/{ad_account_id}/leads_export/{leads_export_id} | Get the lead export from the lead export create call


# **leads_export_create**
> LeadsExportCreateResponse leads_export_create(ad_account_id, leads_export_create_request)

Create a request to export leads collected from a lead ad

<strong>This feature is currently in beta and not available to all apps, if you're interested in joining the beta, please reach out to your Pinterest account manager.</strong>  Create an export of leads collected from a lead ad. This returns a lead_export_id  token that you can use to download the export when it is ready.  Note: Lead ad data will be available up to 30 days after the lead has been submitted.  For more, see <a class=\"reference external\" href=\"https://help.pinterest.com/en/business/article/lead-ads\">Lead ads</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import leads_export_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.leads_export_create_request import LeadsExportCreateRequest
from openapi_generated.pinterest_client.model.leads_export_create_response import LeadsExportCreateResponse
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
    api_instance = leads_export_api.LeadsExportApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    leads_export_create_request = LeadsExportCreateRequest(
        start_date="2020-12-20",
        end_date="2020-12-20",
        ad_id="687201361754",
    ) # LeadsExportCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a request to export leads collected from a lead ad
        api_response = api_instance.leads_export_create(ad_account_id, leads_export_create_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadsExportApi->leads_export_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **leads_export_create_request** | [**LeadsExportCreateRequest**](LeadsExportCreateRequest.md)|  |

### Return type

[**LeadsExportCreateResponse**](LeadsExportCreateResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid ad account parameter. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_export_get**
> LeadsExportResponseData leads_export_get(ad_account_id, leads_export_id)

Get the lead export from the lead export create call

<strong>This feature is currently in beta and not available to all apps, if you're interested in joining the beta, please reach out to your Pinterest account manager.</strong>  Get the export of leads collected from a lead ad. This returns a URL to a list of lead export given a lead_export_id token returned from the create a lead export call. You can use the URL to download the report.  Note: Lead ad data will be available up to 30 days after the lead has been submitted.  For more, see <a class=\"reference external\" href=\"https://help.pinterest.com/en/business/article/lead-ads\">Lead ads</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import leads_export_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.leads_export_response_data import LeadsExportResponseData
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
    api_instance = leads_export_api.LeadsExportApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    leads_export_id = "123755885175" # str | lead_export_id token returned from the create a lead export endpoint

    # example passing only required values which don't have defaults set
    try:
        # Get the lead export from the lead export create call
        api_response = api_instance.leads_export_get(ad_account_id, leads_export_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadsExportApi->leads_export_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **leads_export_id** | **str**| lead_export_id token returned from the create a lead export endpoint |

### Return type

[**LeadsExportResponseData**](LeadsExportResponseData.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid ad account parameter. |  -  |
**404** | Invalid leads export id parameter. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

