# CatalogsRetailFeedsUpdateRequest

Request object for updating a feed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_type** | [**CatalogsType**](CatalogsType.md) |  | 
**default_currency** | [**NullableCurrency**](NullableCurrency.md) |  | [optional] 
**name** | **str** | A human-friendly name associated to a given feed. | [optional] 
**format** | [**CatalogsFormat**](CatalogsFormat.md) |  | [optional] 
**credentials** | [**CatalogsFeedCredentials**](CatalogsFeedCredentials.md) |  | [optional] 
**location** | **str** | The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing. | [optional] 
**preferred_processing_schedule** | [**CatalogsFeedProcessingSchedule**](CatalogsFeedProcessingSchedule.md) |  | [optional] 
**status** | [**CatalogsStatus**](CatalogsStatus.md) |  | [optional] 
**default_availability** | [**ProductAvailabilityType**](ProductAvailabilityType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


