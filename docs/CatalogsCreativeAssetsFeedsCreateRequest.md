# CatalogsCreativeAssetsFeedsCreateRequest

Request object for creating a feed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name associated to a given feed. | 
**format** | [**CatalogsFormat**](CatalogsFormat.md) |  | 
**default_locale** | **bool, date, datetime, dict, float, int, list, str, none_type** | The locale used within a feed for product descriptions. | 
**default_country** | [**Country**](Country.md) |  | 
**location** | **str** | The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing. | 
**catalog_type** | [**CatalogsType**](CatalogsType.md) |  | 
**default_currency** | [**NullableCurrency**](NullableCurrency.md) |  | [optional] 
**credentials** | [**CatalogsFeedCredentials**](CatalogsFeedCredentials.md) |  | [optional] 
**preferred_processing_schedule** | [**CatalogsFeedProcessingSchedule**](CatalogsFeedProcessingSchedule.md) |  | [optional] 
**catalog_id** | **str, none_type** | Catalog id pertaining to the feed. If not provided, feed will use a default catalog based on type. At the moment a catalog can not have multiple creative assets feeds but this will change in the future. | [optional] 
**status** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


