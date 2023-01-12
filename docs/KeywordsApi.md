# openapi_generated.pinterest_client.KeywordsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**country_keywords_metrics_get**](KeywordsApi.md#country_keywords_metrics_get) | **GET** /ad_accounts/{ad_account_id}/keywords/metrics | Get country&#39;s keyword metrics
[**keywords_create**](KeywordsApi.md#keywords_create) | **POST** /ad_accounts/{ad_account_id}/keywords | Create keywords
[**keywords_get**](KeywordsApi.md#keywords_get) | **GET** /ad_accounts/{ad_account_id}/keywords | Get keywords
[**keywords_update**](KeywordsApi.md#keywords_update) | **PATCH** /ad_accounts/{ad_account_id}/keywords | Update keywords


# **country_keywords_metrics_get**
> KeywordsMetricsArrayResponse country_keywords_metrics_get(ad_account_id, country_code, keywords)

Get country's keyword metrics

See keyword metrics for a specified country, aggregated across all of Pinterest. (Definitions are available from the \"Get delivery metrics definitions\" <a href=\"/docs/api/v5/#operation/delivery_metrics/get\">API endpoint</a>).

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import keywords_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.keywords_metrics_array_response import KeywordsMetricsArrayResponse
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
    api_instance = keywords_api.KeywordsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    country_code = "US" # str | Two letter country code (ISO 3166-1 alpha-2)
    keywords = [
        "keywords_example",
    ] # [str] | Comma-separated keywords

    # example passing only required values which don't have defaults set
    try:
        # Get country's keyword metrics
        api_response = api_instance.country_keywords_metrics_get(ad_account_id, country_code, keywords)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling KeywordsApi->country_keywords_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **country_code** | **str**| Two letter country code (ISO 3166-1 alpha-2) |
 **keywords** | **[str]**| Comma-separated keywords |

### Return type

[**KeywordsMetricsArrayResponse**](KeywordsMetricsArrayResponse.md)

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

# **keywords_create**
> KeywordsResponse keywords_create(ad_account_id, keywords_request)

Create keywords

<p>Create keywords for following entity types(advertiser, campaign, ad group or ad).</p> <p>For more information, see <a target=\"_blank\" href=\"https://help.pinterest.com/en/business/article/keyword-targeting\">Keyword targeting</a>.</p> <p><b>Notes:</b></p> <ul style=\"list-style-type: square;\"> <li>Advertisers and campaigns can only be assigned keywords with excluding ('_NEGATIVE').</li> <li>All keyword match types are available for ad groups.</li> </ul> <p>For more information on match types, see <a href=\"/docs/redoc/#section/Match-type-(keyword)\">match type enums</a>.</p> <p><b>Returns:</b></p> <ul style=\"list-style-type: square;\"> <li><p>A successful call returns an object containing an array of new keyword objects and an empty &quot;errors&quot; object array.</p></li> <li><p>An unsuccessful call returns an empty keywords array, and, instead, inserts the entire object with nulled/negated properties into the &quot;errors&quot; object array:</p> <pre class=\"last literal-block\"> { \"keywords\": [], \"errors\": [ { \"data\": { \"archived\": null, \"match_type\": \"EXACT\", \"parent_type\": null, \"value\": \"foobar\", \"parent_id\": null, \"type\": \"keyword\", \"id\": null }, \"error_messages\": [ \"Advertisers and Campaigns only accept excluded targeting attributes.\" ] } } </pre></li> </ul> <p><b>Rate limit</b>: <a href=\"/docs/redoc/#tag/Rate-Limits\">WRITE</a>.</p>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import keywords_api
from openapi_generated.pinterest_client.model.keywords_response import KeywordsResponse
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.keywords_request import KeywordsRequest
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
    api_instance = keywords_api.KeywordsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    keywords_request = KeywordsRequest(
        keywords=[
            KeywordsCommon(
                bid=200000,
                match_type=MatchTypeResponse("BROAD"),
                value="value_example",
            ),
        ],
        parent_id="383791336903426391",
    ) # KeywordsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create keywords
        api_response = api_instance.keywords_create(ad_account_id, keywords_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling KeywordsApi->keywords_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **keywords_request** | [**KeywordsRequest**](KeywordsRequest.md)|  |

### Return type

[**KeywordsResponse**](KeywordsResponse.md)

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

# **keywords_get**
> bool, date, datetime, dict, float, int, list, str, none_type keywords_get(ad_account_id)

Get keywords

<p>Get a list of keywords based on the filters provided.</p><p>For more information, see <a target=\"_blank\" href=\"https://help.pinterest.com/en/business/article/keyword-targeting\">Keyword targeting</a>.</p> <p><b>Notes:</b></p> <ul style=\"list-style-type: square;\"> <li>Advertisers and campaigns can only be assigned keywords with excluding ('_NEGATIVE').</li> <li>All keyword match types are available for ad groups.</li> </ul> <p>For more information on match types, see <a href=\"/docs/redoc/#section/Match-type-(keyword)\">match type enums</a>.</p> <p><b>Returns:</b></p> <ul style=\"list-style-type: square;\"> <li><p>A successful call returns an object containing an array of new keyword objects and an empty &quot;errors&quot; object array.</p></li> <li><p>An unsuccessful call returns an empty keywords array, and, instead, inserts the entire object with nulled/negated properties into the &quot;errors&quot; object array:</p> <pre class=\"last literal-block\"> { \"keywords\": [], \"errors\": [ { \"data\": { \"archived\": null, \"match_type\": \"EXACT\", \"parent_type\": null, \"value\": \"foobar\", \"parent_id\": null, \"type\": \"keyword\", \"id\": null }, \"error_messages\": [ \"Advertisers and Campaigns only accept excluded targeting attributes.\" ] } } </pre></li> </ul>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import keywords_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.match_type import MatchType
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
    api_instance = keywords_api.KeywordsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    campaign_id = "4" # str | Campaign Id to use to filter the results. (optional)
    ad_group_id = "123123123" # str | Ad group Id. (optional)
    match_types = [
        MatchType("BROAD"),
    ] # [MatchType] | Keyword <a href=\"/docs/redoc/#section/Match-type-(keyword).\">match type</a> (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/getting-started/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get keywords
        api_response = api_instance.keywords_get(ad_account_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling KeywordsApi->keywords_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get keywords
        api_response = api_instance.keywords_get(ad_account_id, campaign_id=campaign_id, ad_group_id=ad_group_id, match_types=match_types, page_size=page_size, bookmark=bookmark)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling KeywordsApi->keywords_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **campaign_id** | **str**| Campaign Id to use to filter the results. | [optional]
 **ad_group_id** | **str**| Ad group Id. | [optional]
 **match_types** | [**[MatchType]**](MatchType.md)| Keyword &lt;a href&#x3D;\&quot;/docs/redoc/#section/Match-type-(keyword).\&quot;&gt;match type&lt;/a&gt; | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/getting-started/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keywords_update**
> KeywordsResponse keywords_update(ad_account_id, keyword_update_body)

Update keywords

<p>Update one or more keywords' bid and archived fields.</p> <p>Archiving a keyword effectively deletes it - keywords no longer receive metrics and no longer visible within the parent entity's keywords list.</p>

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import keywords_api
from openapi_generated.pinterest_client.model.keywords_response import KeywordsResponse
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.keyword_update_body import KeywordUpdateBody
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
    api_instance = keywords_api.KeywordsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    keyword_update_body = KeywordUpdateBody(
        keywords=[
            KeywordUpdate(
                id="2886364308355",
                archived=False,
                bid=200000,
            ),
        ],
    ) # KeywordUpdateBody | 

    # example passing only required values which don't have defaults set
    try:
        # Update keywords
        api_response = api_instance.keywords_update(ad_account_id, keyword_update_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling KeywordsApi->keywords_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **keyword_update_body** | [**KeywordUpdateBody**](KeywordUpdateBody.md)|  |

### Return type

[**KeywordsResponse**](KeywordsResponse.md)

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

