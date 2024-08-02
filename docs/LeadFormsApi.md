# openapi_generated.pinterest_client.LeadFormsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lead_form_get**](LeadFormsApi.md#lead_form_get) | **GET** /ad_accounts/{ad_account_id}/lead_forms/{lead_form_id} | Get lead form by id
[**lead_form_test_create**](LeadFormsApi.md#lead_form_test_create) | **POST** /ad_accounts/{ad_account_id}/lead_forms/{lead_form_id}/test | Create lead form test data
[**lead_forms_create**](LeadFormsApi.md#lead_forms_create) | **POST** /ad_accounts/{ad_account_id}/lead_forms | Create lead forms
[**lead_forms_list**](LeadFormsApi.md#lead_forms_list) | **GET** /ad_accounts/{ad_account_id}/lead_forms | List lead forms
[**lead_forms_update**](LeadFormsApi.md#lead_forms_update) | **PATCH** /ad_accounts/{ad_account_id}/lead_forms | Update lead forms


# **lead_form_get**
> LeadFormResponse lead_form_get(ad_account_id, lead_form_id)

Get lead form by id

<strong>This feature is currently in beta and not available to all apps, if you're interested in joining the beta, please reach out to your Pinterest account manager.</strong>  Gets a lead form given it's ID. It must also be associated with the provided ad account ID.  For more, see <a class=\"reference external\" href=\"https://help.pinterest.com/en/business/article/lead-ads\">Lead ads</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import lead_forms_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.lead_form_response import LeadFormResponse
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
    api_instance = lead_forms_api.LeadFormsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    lead_form_id = "1234567890123" # str | Unique identifier of a lead form.

    # example passing only required values which don't have defaults set
    try:
        # Get lead form by id
        api_response = api_instance.lead_form_get(ad_account_id, lead_form_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadFormsApi->lead_form_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **lead_form_id** | **str**| Unique identifier of a lead form. |

### Return type

[**LeadFormResponse**](LeadFormResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid ad account lead forms parameters. |  -  |
**404** | The lead form ID for the given ad account ID does not exist. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lead_form_test_create**
> LeadFormTestResponse lead_form_test_create(ad_account_id, lead_form_id, lead_form_test_request)

Create lead form test data

Create lead form test data based on the list of answers provided as part of the body. - List of answers should follow the questions creation order.  <strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/getting-started/beta-and-advanced-access/'>Learn more</a>.</strong>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import lead_forms_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.lead_form_test_response import LeadFormTestResponse
from openapi_generated.pinterest_client.model.lead_form_test_request import LeadFormTestRequest
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
    api_instance = lead_forms_api.LeadFormsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    lead_form_id = "1234567890123" # str | Unique identifier of a lead form.
    lead_form_test_request = LeadFormTestRequest(
        answers=["John","Doe","abc@email.com","987654321"],
    ) # LeadFormTestRequest | Subscription to create.

    # example passing only required values which don't have defaults set
    try:
        # Create lead form test data
        api_response = api_instance.lead_form_test_create(ad_account_id, lead_form_id, lead_form_test_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadFormsApi->lead_form_test_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **lead_form_id** | **str**| Unique identifier of a lead form. |
 **lead_form_test_request** | [**LeadFormTestRequest**](LeadFormTestRequest.md)| Subscription to create. |

### Return type

[**LeadFormTestResponse**](LeadFormTestResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid parameters. |  -  |
**404** | Lead not found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lead_forms_create**
> LeadFormArrayResponse lead_forms_create(ad_account_id, lead_form_create_request)

Create lead forms

<strong>This feature is currently in beta and not available to all apps, if you're interested in joining the beta, please reach out to your Pinterest account manager.</strong>  Create lead forms. Lead forms are used in lead ads and allow you to control what text appears on the lead form’ s description, questions and confirmation sections.  For more, see <a class=\"reference external\" href=\"https://help.pinterest.com/en/business/article/lead-ads\">Lead ads</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import lead_forms_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.lead_form_array_response import LeadFormArrayResponse
from openapi_generated.pinterest_client.model.lead_form_create_request import LeadFormCreateRequest
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
    api_instance = lead_forms_api.LeadFormsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    lead_form_create_request = [
        LeadFormCreateRequest(),
    ] # [LeadFormCreateRequest] | List of lead forms to create, size limit [1, 30].

    # example passing only required values which don't have defaults set
    try:
        # Create lead forms
        api_response = api_instance.lead_forms_create(ad_account_id, lead_form_create_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadFormsApi->lead_forms_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **lead_form_create_request** | [**[LeadFormCreateRequest]**](LeadFormCreateRequest.md)| List of lead forms to create, size limit [1, 30]. |

### Return type

[**LeadFormArrayResponse**](LeadFormArrayResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid ad account lead forms parameters. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lead_forms_list**
> bool, date, datetime, dict, float, int, list, str, none_type lead_forms_list(ad_account_id)

List lead forms

<strong>This feature is currently in beta and not available to all apps, if you're interested in joining the beta, please reach out to your Pinterest account manager.</strong>  List lead forms associated with an ad account ID.  For more, see <a class=\"reference external\" href=\"https://help.pinterest.com/en/business/article/lead-ads\">Lead ads</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import lead_forms_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.lead_form_response import LeadFormResponse
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
    api_instance = lead_forms_api.LeadFormsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    order = "ASCENDING" # str | The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. (optional)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    try:
        # List lead forms
        api_response = api_instance.lead_forms_list(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadFormsApi->lead_forms_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List lead forms
        api_response = api_instance.lead_forms_list(ad_account_id, page_size=page_size, order=order, bookmark=bookmark)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadFormsApi->lead_forms_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **order** | **str**| The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. | [optional]
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]

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
**400** | Invalid ad account lead forms parameters. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lead_forms_update**
> LeadFormArrayResponse lead_forms_update(ad_account_id, lead_form_update_request)

Update lead forms

<strong>This feature is currently in beta and not available to all apps, if you're interested in joining the beta, please reach out to your Pinterest account manager.</strong>  Update lead forms. Lead ads help you reach people who are actively looking for, and interested in, your goods and services. The lead form can be associated with an ad to allow people to fill out the form.  For more, see <a class=\"reference external\" href=\"https://help.pinterest.com/en/business/article/lead-ads\">Lead ads</a>.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import lead_forms_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.lead_form_array_response import LeadFormArrayResponse
from openapi_generated.pinterest_client.model.lead_form_update_request import LeadFormUpdateRequest
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
    api_instance = lead_forms_api.LeadFormsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    lead_form_update_request = [
        LeadFormUpdateRequest(),
    ] # [LeadFormUpdateRequest] | List of lead forms to update, size limit [1, 30].

    # example passing only required values which don't have defaults set
    try:
        # Update lead forms
        api_response = api_instance.lead_forms_update(ad_account_id, lead_form_update_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling LeadFormsApi->lead_forms_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **lead_form_update_request** | [**[LeadFormUpdateRequest]**](LeadFormUpdateRequest.md)| List of lead forms to update, size limit [1, 30]. |

### Return type

[**LeadFormArrayResponse**](LeadFormArrayResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid ad account lead forms parameters. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

