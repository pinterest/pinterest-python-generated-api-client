# CatalogsRetailProductGroupCreateRequest

Request object for creating a product group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**filters** | [**CatalogsProductGroupFiltersRequest**](CatalogsProductGroupFiltersRequest.md) |  | 
**catalog_id** | **str** | Catalog id pertaining to the retail product group. | 
**country** | [**Country**](Country.md) |  | 
**locale** | [**CatalogsLocale**](CatalogsLocale.md) |  | 
**catalog_type** | **str** | Retail catalog based product group is available only for selected partners at the moment. If you are not eligible, please use feed based one. | defaults to "RETAIL"
**description** | **str, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


