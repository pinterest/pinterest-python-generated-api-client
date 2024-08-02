# FeedFields1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | A human-friendly name associated to a given feed. This value is currently nullable due to historical reasons. It is expected to become non-nullable in the future. | 
**format** | [**CatalogsFormat**](CatalogsFormat.md) |  | 
**catalog_type** | [**CatalogsType**](CatalogsType.md) |  | 
**credentials** | [**CatalogsFeedCredentials**](CatalogsFeedCredentials.md) |  | 
**location** | **str** | The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing. | 
**preferred_processing_schedule** | [**CatalogsFeedProcessingSchedule**](CatalogsFeedProcessingSchedule.md) |  | 
**status** | [**CatalogsStatus**](CatalogsStatus.md) |  | 
**default_currency** | [**NullableCurrency**](NullableCurrency.md) |  | 
**default_locale** | **str** | The locale used within a feed for product descriptions. | 
**catalog_id** | **str, none_type** | Catalog id pertaining to the feed. If not provided, feed will use a default catalog based on type. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


