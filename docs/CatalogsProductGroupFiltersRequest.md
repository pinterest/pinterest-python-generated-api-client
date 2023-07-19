# CatalogsProductGroupFiltersRequest

Object holding a group of filters for request on catalog product group. This is a distinct schema It is not possible to create or update a Product Group with empty filters. But some automatically generated Product Groups might have empty filters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any_of** | [**[CatalogsProductGroupFilterKeys]**](CatalogsProductGroupFilterKeys.md) |  | [optional] 
**all_of** | [**[CatalogsProductGroupFilterKeys]**](CatalogsProductGroupFilterKeys.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


