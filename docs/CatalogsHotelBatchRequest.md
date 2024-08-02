# CatalogsHotelBatchRequest

Request object to update catalogs hotel items

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**Country**](Country.md) |  | 
**language** | **bool, date, datetime, dict, float, int, list, str, none_type** | We recommend using the CatalogsLocale values. | 
**items** | [**[CatalogsHotelBatchItem]**](CatalogsHotelBatchItem.md) | Array with catalogs item operations | 
**catalog_type** | **str** |  | defaults to "HOTEL"
**catalog_id** | **str** | Catalog id pertaining to the hotel item. If not provided, default to oldest hotel catalog | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


