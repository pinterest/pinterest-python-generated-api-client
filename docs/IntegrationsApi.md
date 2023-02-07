# openapi_generated.pinterest_client.IntegrationsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrations_commerce_del**](IntegrationsApi.md#integrations_commerce_del) | **DELETE** /integrations/commerce/{external_business_id} | Delete commerce integration
[**integrations_commerce_get**](IntegrationsApi.md#integrations_commerce_get) | **GET** /integrations/commerce/{external_business_id} | Get commerce integration
[**integrations_commerce_patch**](IntegrationsApi.md#integrations_commerce_patch) | **PATCH** /integrations/commerce/{external_business_id} | Update commerce integration
[**integrations_commerce_post**](IntegrationsApi.md#integrations_commerce_post) | **POST** /integrations/commerce | Create commerce integration


# **integrations_commerce_del**
> integrations_commerce_del(external_business_id)

Delete commerce integration

Delete commerce integration metadata for the given external business ID.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import integrations_api
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    external_business_id = "external_business_id_example" # str | External business ID for the integration.

    # example passing only required values which don't have defaults set
    try:
        # Delete commerce integration
        api_instance.integrations_commerce_del(external_business_id)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_commerce_del: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_business_id** | **str**| External business ID for the integration. |

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
**204** | Commerce Integration deleted successfully |  -  |
**404** | Integration not found. |  -  |
**409** | Can&#39;t access this integration metadata. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_commerce_get**
> IntegrationMetadata integrations_commerce_get(external_business_id)

Get commerce integration

Get commerce integration metadata associated with the given external business ID

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import integrations_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.integration_metadata import IntegrationMetadata
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    external_business_id = "external_business_id_example" # str | External business ID for the integration.

    # example passing only required values which don't have defaults set
    try:
        # Get commerce integration
        api_response = api_instance.integrations_commerce_get(external_business_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_commerce_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_business_id** | **str**| External business ID for the integration. |

### Return type

[**IntegrationMetadata**](IntegrationMetadata.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Integration not found. |  -  |
**409** | Can&#39;t access this integration metadata. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_commerce_patch**
> IntegrationMetadata integrations_commerce_patch(external_business_id)

Update commerce integration

Update commerce integration metadata for the given external business ID

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import integrations_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.integration_metadata import IntegrationMetadata
from openapi_generated.pinterest_client.model.integration_request_patch import IntegrationRequestPatch
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    external_business_id = "external_business_id_example" # str | External business ID for the integration.
    integration_request_patch = IntegrationRequestPatch(
        connected_merchant_id="connected_merchant_id_example",
        connected_advertiser_id="connected_advertiser_id_example",
        connected_lba_id="connected_lba_id_example",
        connected_tag_id="connected_tag_id_example",
        partner_access_token="partner_access_token_example",
        partner_primary_email="partner_primary_email_example",
    ) # IntegrationRequestPatch | Parameters to get create/update the Integration Metadata (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update commerce integration
        api_response = api_instance.integrations_commerce_patch(external_business_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_commerce_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update commerce integration
        api_response = api_instance.integrations_commerce_patch(external_business_id, integration_request_patch=integration_request_patch)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_commerce_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_business_id** | **str**| External business ID for the integration. |
 **integration_request_patch** | [**IntegrationRequestPatch**](IntegrationRequestPatch.md)| Parameters to get create/update the Integration Metadata | [optional]

### Return type

[**IntegrationMetadata**](IntegrationMetadata.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Integration not found. |  -  |
**409** | Can&#39;t access this integration metadata. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_commerce_post**
> IntegrationMetadata integrations_commerce_post()

Create commerce integration

Create commerce integration metadata to link an external business ID with a Pinterest merchant & ad account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import integrations_api
from openapi_generated.pinterest_client.model.integration_request import IntegrationRequest
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.integration_metadata import IntegrationMetadata
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    integration_request = IntegrationRequest(
        external_business_id="external_business_id_example",
        connected_merchant_id="connected_merchant_id_example",
        connected_advertiser_id="connected_advertiser_id_example",
        connected_lba_id="connected_lba_id_example",
        connected_tag_id="connected_tag_id_example",
        partner_access_token="partner_access_token_example",
        partner_primary_email="partner_primary_email_example",
    ) # IntegrationRequest | Parameters to get create/update the Integration Metadata (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create commerce integration
        api_response = api_instance.integrations_commerce_post(integration_request=integration_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_commerce_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_request** | [**IntegrationRequest**](IntegrationRequest.md)| Parameters to get create/update the Integration Metadata | [optional]

### Return type

[**IntegrationMetadata**](IntegrationMetadata.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Integration not found. |  -  |
**409** | Can&#39;t access this integration metadata. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

