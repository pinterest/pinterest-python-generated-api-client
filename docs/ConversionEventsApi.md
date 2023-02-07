# openapi_generated.pinterest_client.ConversionEventsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_create**](ConversionEventsApi.md#events_create) | **POST** /ad_accounts/{ad_account_id}/events | Send conversion events to the Pinterest API for Conversions


# **events_create**
> ConversionApiResponse events_create(ad_account_id, conversion_events)

Send conversion events to the Pinterest API for Conversions

The Pinterest API offers advertisers a way to send Pinterest their conversion information (including web conversions, in-app conversions, or even offline conversions) based on their <code>ad_account_id</code>. The request body should be a JSON object. - This endpoint requires an <code>access_token</code> be generated through Ads Manager. Review the <a href=\"/docs/conversions/conversion-management/#Authenticating%20for%20the%20Conversion%20Tracking%20endpoint\">Conversions Guide</a> for more details. - The token's <code>user_account</code> must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via <a href=\"https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts\">Business Access</a>: Admin, Analyst, Audience, Campaign. - If the merchant is submitting this information using both Pinterest conversion tags and the Pinterest API, Pinterest will remove duplicate information before reporting. (Note that events that took place offline cannot be deduplicated.)

### Example

* Bearer Authentication (conversion_token):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import conversion_events_api
from openapi_generated.pinterest_client.model.conversion_events import ConversionEvents
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.conversion_api_response import ConversionApiResponse
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

# Configure Bearer authorization: conversion_token
configuration = openapi_generated.pinterest_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversion_events_api.ConversionEventsApi(api_client)
    ad_account_id = "4" # str | Unique identifier of an ad account.
    conversion_events = ConversionEvents(
        data=[
            ConversionEventsData(
                event_name="checkout",
                action_source="app_ios",
                event_time=1451431341,
                event_id="eventId0001",
                event_source_url="https://example.org/",
                opt_out=False,
                partner_name="partner_name_example",
                user_data=ConversionEventsUserData(
                    ph=[
                        "ph_example",
                    ],
                    ge=[
                        "ge_example",
                    ],
                    db=[
                        "db_example",
                    ],
                    ln=[
                        "ln_example",
                    ],
                    fn=[
                        "fn_example",
                    ],
                    ct=[
                        "ct_example",
                    ],
                    st=[
                        "st_example",
                    ],
                    zp=[
                        "zp_example",
                    ],
                    country=[
                        "country_example",
                    ],
                    external_id=[
                        "external_id_example",
                    ],
                    click_id="dj0yJnU9b2JDcFFHekV4SHJNcmVrbFBkUEdqakh0akdUT1VjVVUmcD0yJm49cnNBQ3F2Q2dOVDBXWWhkWklrUGxBUSZ0PUFBQUFBR1BaY3Bv",
                ),
                custom_data=ConversionEventsCustomData(
                    currency="USD",
                    value="425325.89",
                    content_ids=[
                        "content_ids_example",
                    ],
                    contents=[
                        ConversionEventsCustomDataContents(
                            item_price="1325.12",
                            quantity=1,
                        ),
                    ],
                    num_items=1,
                    order_id="order_id_example",
                    search_string="search_string_example",
                    opt_out_type="LDP",
                    np="np_example",
                ),
                app_id="app_id_example",
                app_name="app_name_example",
                app_version="app_version_example",
                device_brand="device_brand_example",
                device_carrier="device_carrier_example",
                device_model="device_model_example",
                device_type="device_type_example",
                os_version="os_version_example",
                wifi=False,
                language="en",
            ),
        ],
    ) # ConversionEvents | Conversion events.
    test = True # bool | Include query param ?test=true to mark the request as a test request. The events will not be recorded but the API will still return the same response messages. Use this mode to verify your requests are working and your events are constructed correctly. Warning: If you use this query parameter, be certain that it is off (set to false or deleted) before sending a legitimate (non-testing) request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send conversion events to the Pinterest API for Conversions
        api_response = api_instance.events_create(ad_account_id, conversion_events)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ConversionEventsApi->events_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send conversion events to the Pinterest API for Conversions
        api_response = api_instance.events_create(ad_account_id, conversion_events, test=test)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling ConversionEventsApi->events_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_account_id** | **str**| Unique identifier of an ad account. |
 **conversion_events** | [**ConversionEvents**](ConversionEvents.md)| Conversion events. |
 **test** | **bool**| Include query param ?test&#x3D;true to mark the request as a test request. The events will not be recorded but the API will still return the same response messages. Use this mode to verify your requests are working and your events are constructed correctly. Warning: If you use this query parameter, be certain that it is off (set to false or deleted) before sending a legitimate (non-testing) request. | [optional]

### Return type

[**ConversionApiResponse**](ConversionApiResponse.md)

### Authorization

[conversion_token](../README.md#conversion_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The request was invalid. |  -  |
**503** | The endpoint has been ramped down and is currently not accepting any traffic. |  -  |
**0** | Unexpected errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

