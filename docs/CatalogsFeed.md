# CatalogsFeed

Catalogs Feed object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_country** | [**Country**](Country.md) |  | 
**default_availability** | [**ProductAvailabilityType**](ProductAvailabilityType.md) |  | 
**default_currency** | [**NullableCurrency**](NullableCurrency.md) |  | 
**name** | **str, none_type** | A human-friendly name associated to a given feed. This value is currently nullable due to historical reasons. It is expected to become non-nullable in the future. | 
**format** | [**CatalogsFormat**](CatalogsFormat.md) |  | 
**default_locale** | **str** | The locale used within a feed for product descriptions. | 
**credentials** | [**CatalogsFeedCredentials**](CatalogsFeedCredentials.md) |  | 
**location** | **str** | The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing. | 
**preferred_processing_schedule** | [**CatalogsFeedProcessingSchedule**](CatalogsFeedProcessingSchedule.md) |  | 
**status** | [**CatalogsStatus**](CatalogsStatus.md) |  | 
**created_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


