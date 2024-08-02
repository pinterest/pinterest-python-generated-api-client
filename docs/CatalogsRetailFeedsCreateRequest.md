# CatalogsRetailFeedsCreateRequest

Request object for creating a retail feed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name associated to a given feed. | 
**format** | [**CatalogsFormat**](CatalogsFormat.md) |  | 
**default_locale** | **bool, date, datetime, dict, float, int, list, str, none_type** | The locale used within a feed for product descriptions. | 
**location** | **str** | The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing. | 
**catalog_type** | [**CatalogsType**](CatalogsType.md) |  | 
**default_country** | [**Country**](Country.md) |  | 
**default_currency** | [**NullableCurrency**](NullableCurrency.md) |  | [optional] 
**credentials** | [**CatalogsFeedCredentials**](CatalogsFeedCredentials.md) |  | [optional] 
**preferred_processing_schedule** | [**CatalogsFeedProcessingSchedule**](CatalogsFeedProcessingSchedule.md) |  | [optional] 
**default_availability** | [**ProductAvailabilityType**](ProductAvailabilityType.md) |  | [optional] 
**status** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


