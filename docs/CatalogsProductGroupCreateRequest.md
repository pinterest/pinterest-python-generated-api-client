# CatalogsProductGroupCreateRequest

Request object for creating a product group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str, none_type** |  | [optional] 
**is_featured** | **bool** | boolean indicator of whether the product group is being featured or not | [optional]  if omitted the server will use the default value of False
**name** | **str** |  | [optional] 
**filters** | [**CatalogsProductGroupFiltersRequest**](CatalogsProductGroupFiltersRequest.md) |  | [optional] 
**feed_id** | **str** | Catalog Feed id pertaining to the catalog product group. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


