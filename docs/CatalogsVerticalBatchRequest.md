# CatalogsVerticalBatchRequest

A request object that can have multiple operations on a single batch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_type** | **str** |  | defaults to "CREATIVE_ASSETS"
**catalog_id** | **str** | Catalog id pertaining to the creative assets item. If not provided, default to oldest creative assets catalog | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**language** | **bool, date, datetime, dict, float, int, list, str, none_type** | We recommend using the CatalogsLocale values. | [optional] 
**items** | [**[CatalogsCreativeAssetsBatchItem]**](CatalogsCreativeAssetsBatchItem.md) | Array with creative assets item operations | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


