# CatalogsFeed

Catalogs Feed object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_type** | [**CatalogsType**](CatalogsType.md) |  | 
**created_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**name** | **str, none_type** | A human-friendly name associated to a given feed. This value is currently nullable due to historical reasons. It is expected to become non-nullable in the future. | [optional] 
**format** | [**CatalogsFormat**](CatalogsFormat.md) |  | [optional] 
**credentials** | [**CatalogsFeedCredentials**](CatalogsFeedCredentials.md) |  | [optional] 
**location** | **str** | The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing. | [optional] 
**preferred_processing_schedule** | [**CatalogsFeedProcessingSchedule**](CatalogsFeedProcessingSchedule.md) |  | [optional] 
**status** | [**CatalogsStatus**](CatalogsStatus.md) |  | [optional] 
**default_currency** | [**NullableCurrency**](NullableCurrency.md) |  | [optional] 
**default_locale** | **str** | The locale used within a feed for product descriptions. | [optional] 
**default_country** | [**Country**](Country.md) |  | [optional] 
**default_availability** | [**ProductAvailabilityType**](ProductAvailabilityType.md) |  | [optional] 
**catalog_id** | **str, none_type** | Catalog id pertaining to the feed. If not provided, feed will use a default catalog based on type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


