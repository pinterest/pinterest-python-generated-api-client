# CatalogsRetailListProductsByCatalogBasedFilterRequest

Request object to list products for a given retail catalog_id and product group filter.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_id** | **str** | Catalog id pertaining to the retail product group. | 
**filters** | [**CatalogsProductGroupFilters**](CatalogsProductGroupFilters.md) |  | 
**country** | [**Country**](Country.md) |  | 
**locale** | [**CatalogsLocale**](CatalogsLocale.md) |  | 
**catalog_type** | **str** | Retail catalog based product group is available only for selected partners at the moment. If you are not eligible, please use feed based one. | defaults to "RETAIL"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


