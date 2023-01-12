# openapi_generated.pinterest_client.TermsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terms_related_list**](TermsApi.md#terms_related_list) | **GET** /terms/related | List related terms
[**terms_suggested_list**](TermsApi.md#terms_suggested_list) | **GET** /terms/suggested | List suggested terms


# **terms_related_list**
> RelatedTerms terms_related_list(terms)

List related terms

Get a list of terms logically related to each input term. <p/> Example: the term 'workout' would list related terms like 'one song workout', 'yoga workout', 'workout motivation', etc.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import terms_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.related_terms import RelatedTerms
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
    api_instance = terms_api.TermsApi(api_client)
    terms = [
        "workout",
    ] # [str] | List of input terms.

    # example passing only required values which don't have defaults set
    try:
        # List related terms
        api_response = api_instance.terms_related_list(terms)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling TermsApi->terms_related_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terms** | **[str]**| List of input terms. |

### Return type

[**RelatedTerms**](RelatedTerms.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid terms related parameters. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_suggested_list**
> TermsSuggestedResponse terms_suggested_list(term)

List suggested terms

Get popular search terms that begin with your input term. <p/> Example: 'sport' would return popular terms like 'sports bar' and 'sportswear', but not 'motor sports' since the phrase does not begin with the given term.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import terms_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.terms_suggested_response import TermsSuggestedResponse
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
    api_instance = terms_api.TermsApi(api_client)
    term = "sports" # str | Input term.
    limit = 4 # int | Max suggested terms to return. (optional) if omitted the server will use the default value of 4

    # example passing only required values which don't have defaults set
    try:
        # List suggested terms
        api_response = api_instance.terms_suggested_list(term)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling TermsApi->terms_suggested_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List suggested terms
        api_response = api_instance.terms_suggested_list(term, limit=limit)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling TermsApi->terms_suggested_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| Input term. |
 **limit** | **int**| Max suggested terms to return. | [optional] if omitted the server will use the default value of 4

### Return type

[**TermsSuggestedResponse**](TermsSuggestedResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid terms suggested parameters. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

