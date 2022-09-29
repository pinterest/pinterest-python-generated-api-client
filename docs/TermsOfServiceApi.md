# pinterest.generated.client.TermsOfServiceApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terms_of_service_get**](TermsOfServiceApi.md#terms_of_service_get) | **GET** /ad_accounts/{ad_account_id}/terms_of_service | Get terms of service


# **terms_of_service_get**
> TermsOfService terms_of_service_get(ad_account_id)

Get terms of service

Get the text of the terms of service and see whether the advertiser has accepted the terms of service.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import terms_of_service_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.terms_of_service import TermsOfService
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
    api_instance = terms_of_service_api.TermsOfServiceApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    include_html = False # bool | Return HTML in TOS text. (optional) if omitted the server will use the default value of False
    tos_type = "tos_type_example" # str | Request type. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get terms of service
        api_response = api_instance.terms_of_service_get(ad_account_id)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling TermsOfServiceApi->terms_of_service_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get terms of service
        api_response = api_instance.terms_of_service_get(ad_account_id, include_html=include_html, tos_type=tos_type)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling TermsOfServiceApi->terms_of_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **include_html** | **bool**| Return HTML in TOS text. | [optional] if omitted the server will use the default value of False
 **tos_type** | **str**| Request type. | [optional]

### Return type

[**TermsOfService**](TermsOfService.md)

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

