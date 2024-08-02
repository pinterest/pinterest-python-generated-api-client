# CatalogsRetailProductGroupUpdateRequest

Request object for updating a retail product group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_type** | **str** | Retail catalog based product group is available only for selected partners at the moment. If you are not eligible, please use feed based one. | [optional]  if omitted the server will use the default value of "RETAIL"
**name** | **str** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**filters** | [**CatalogsProductGroupFiltersRequest**](CatalogsProductGroupFiltersRequest.md) |  | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**locale** | [**CatalogsLocale**](CatalogsLocale.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


