# CatalogsVerticalsListProductsByCatalogBasedFilterRequest

Request object to list products for a given catalog_id and product group filter.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_type** | **str** |  | defaults to "CREATIVE_ASSETS"
**catalog_id** | **str** | Catalog id pertaining to the creative assets product group. | [optional] 
**filters** | [**CatalogsCreativeAssetsProductGroupFilters**](CatalogsCreativeAssetsProductGroupFilters.md) |  | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**locale** | [**CatalogsLocale**](CatalogsLocale.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


