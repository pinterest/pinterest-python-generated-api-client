# pinterest.generated.client.BulkApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_download_create**](BulkApi.md#bulk_download_create) | **POST** /ad_accounts/{ad_account_id}/bulk/download | Get advertiser entities in bulk
[**bulk_request_get**](BulkApi.md#bulk_request_get) | **GET** /ad_accounts/{ad_account_id}/bulk/{bulk_request_id} | Download advertiser entities in bulk
[**bulk_upsert_create**](BulkApi.md#bulk_upsert_create) | **POST** /ad_accounts/{ad_account_id}/bulk/upsert | Create/update ad entities in bulk


# **bulk_download_create**
> BulkDownloadResponse bulk_download_create(ad_account_id, bulk_download_request)

Get advertiser entities in bulk

<strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/features/ads-management/'>Learn more</a>.</strong> <p/> Create an asynchronous report that may include information on campaigns, ad groups, product groups, ads, and/or keywords; can filter by campaigns. Though the entities may be active, archived, or paused, only active entities will return data.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import bulk_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.bulk_download_response import BulkDownloadResponse
from pinterest.generated.client.model.bulk_download_request import BulkDownloadRequest
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
    api_instance = bulk_api.BulkApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    bulk_download_request = BulkDownloadRequest(
        entity_types=["CAMPAIGN","AD_GROUP"],
        entity_ids=[
            "4",
        ],
        updated_since="1622848072",
        campaign_filter=BulkDownloadRequestCampaignFilter(
            start_time="1622848072",
            end_time="1622848072",
            name="campaign name",
            campaign_status=[
                CampaignSummaryStatus("RUNNING"),
            ],
            objective_type=[
                ObjectiveType("AWARENESS"),
            ],
        ),
        output_format="output_format_example",
    ) # BulkDownloadRequest | Parameters to get ad entities in bulk

    # example passing only required values which don't have defaults set
    try:
        # Get advertiser entities in bulk
        api_response = api_instance.bulk_download_create(ad_account_id, bulk_download_request)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BulkApi->bulk_download_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **bulk_download_request** | [**BulkDownloadRequest**](BulkDownloadRequest.md)| Parameters to get ad entities in bulk |

### Return type

[**BulkDownloadResponse**](BulkDownloadResponse.md)

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

# **bulk_request_get**
> BulkUpsertStatusResponse bulk_request_get(ad_account_id, bulk_request_id)

Download advertiser entities in bulk

<strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/features/ads-management/'>Learn more</a>.</strong> <p/> Get the status of a bulk request by <code>request_id</code>, along with a download URL that will allow you to download the new or updated entity data (campaigns, ad groups, product groups, ads, or keywords).

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import bulk_api
from pinterest.generated.client.model.bulk_upsert_status_response import BulkUpsertStatusResponse
from pinterest.generated.client.model.error import Error
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
    api_instance = bulk_api.BulkApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    bulk_request_id = "bulk_request_id_example" # str | Unique identifier of a bulk upsert request.

    # example passing only required values which don't have defaults set
    try:
        # Download advertiser entities in bulk
        api_response = api_instance.bulk_request_get(ad_account_id, bulk_request_id)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BulkApi->bulk_request_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **bulk_request_id** | **str**| Unique identifier of a bulk upsert request. |

### Return type

[**BulkUpsertStatusResponse**](BulkUpsertStatusResponse.md)

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

# **bulk_upsert_create**
> BulkUpsertResponse bulk_upsert_create(ad_account_id, bulk_upsert_request)

Create/update ad entities in bulk

<strong>This endpoint is currently in beta and not available to all apps. <a href='/docs/features/ads-management/'>Learn more</a>.</strong> <p/> Either create or update any combination of campaigns, ad groups, product groups, ads, or keywords. Note that this request will be processed asynchronously; the response will include a <code>request_id</code> that can be used to obtain the status of the request.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import bulk_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.bulk_upsert_request import BulkUpsertRequest
from pinterest.generated.client.model.bulk_upsert_response import BulkUpsertResponse
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
    api_instance = bulk_api.BulkApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    bulk_upsert_request = BulkUpsertRequest(
        create=BulkUpsertRequestCreate(
            campaigns=[
                CampaignCreateRequest(),
            ],
            ad_groups=[
                AdGroupCreateRequest(None),
            ],
            ads=[
                AdCreateRequest(None),
            ],
            product_groups=[
                ProductGroupPromotionCreateRequest(
                    ad_group_id="2680059592705",
                    product_group_promotion=[
                        ProductGroupPromotionCommon(
                            status=EntityStatus("ACTIVE"),
                            tracking_url="https://www.pinterest.com",
                            catalogs_product_group_id="1231235",
                            catalogs_product_group_name="catalogProductGroupName",
                            creative_type=CreativeType("REGULAR"),
                            collections_hero_pin_id="123123",
                            collections_hero_destination_url="http://www.pinterest.com",
                            slideshow_collections_title="Title",
                            slideshow_collections_description="Description",
                            is_mdl=True,
                        ),
                    ],
                ),
            ],
            keywords=[
                KeywordsRequest(
                    keywords=[
                        KeywordsCommon(
                            bid=200000,
                            match_type=MatchTypeResponse("BROAD"),
                            value="value_example",
                        ),
                    ],
                    parent_id="383791336903426391",
                ),
            ],
        ),
        update=BulkUpsertRequestUpdate(
            campaigns=[
                CampaignUpdateRequest(),
            ],
            ad_groups=[
                AdGroupUpdateRequest(None),
            ],
            ads=[
                AdUpdateRequest(None),
            ],
            product_groups=[
                ProductGroupPromotionUpdateRequest(
                    ad_group_id="2680059592705",
                    product_group_promotion=[
                        ProductGroupPromotionUpdateItem(None),
                    ],
                ),
            ],
            keywords=[
                KeywordUpdate(
                    id="2886364308355",
                    archived=False,
                    bid=200000,
                ),
            ],
        ),
    ) # BulkUpsertRequest | Parameters to get create/update ad entities in bulk

    # example passing only required values which don't have defaults set
    try:
        # Create/update ad entities in bulk
        api_response = api_instance.bulk_upsert_create(ad_account_id, bulk_upsert_request)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BulkApi->bulk_upsert_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **bulk_upsert_request** | [**BulkUpsertRequest**](BulkUpsertRequest.md)| Parameters to get create/update ad entities in bulk |

### Return type

[**BulkUpsertResponse**](BulkUpsertResponse.md)

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

