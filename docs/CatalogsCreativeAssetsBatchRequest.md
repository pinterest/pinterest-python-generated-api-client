# CatalogsCreativeAssetsBatchRequest

Request object to update catalogs creative assets items

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**Country**](Country.md) |  | 
**language** | **bool, date, datetime, dict, float, int, list, str, none_type** | We recommend using the CatalogsLocale values. | 
**items** | [**[CatalogsCreativeAssetsBatchItem]**](CatalogsCreativeAssetsBatchItem.md) | Array with creative assets item operations | 
**catalog_type** | **str** |  | defaults to "CREATIVE_ASSETS"
**catalog_id** | **str** | Catalog id pertaining to the creative assets item. If not provided, default to oldest creative assets catalog | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


