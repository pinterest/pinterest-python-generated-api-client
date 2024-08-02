# IntegrationLog

Schema for log sent from an integration application.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_timestamp** | **int** | Timestamp in milliseconds of when the log was executed at the client. | 
**event_type** | **str** | Log event type | 
**log_level** | **str** | Log level type | 
**external_business_id** | **str, none_type** |  | [optional] 
**advertiser_id** | **str, none_type** |  | [optional] 
**merchant_id** | **str, none_type** |  | [optional] 
**tag_id** | **str, none_type** |  | [optional] 
**feed_profile_id** | **str, none_type** |  | [optional] 
**message** | **str** | Explanation of the event that occured. | [optional] 
**app_version_number** | **str** | Version number of the integration application. | [optional] 
**platform_version_number** | **str** | Version number of the platform the integration application is running on. | [optional] 
**error** | [**IntegrationLogClientError**](IntegrationLogClientError.md) |  | [optional] 
**request** | [**IntegrationLogClientRequest**](IntegrationLogClientRequest.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


