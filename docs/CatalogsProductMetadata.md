# CatalogsProductMetadata

Product metadata entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The user-created unique ID that represents the product. | 
**item_group_id** | **str, none_type** | The parent ID of the product. | 
**availability** | [**NonNullableProductAvailabilityType**](NonNullableProductAvailabilityType.md) |  | 
**price** | **float** | The price of the product. | 
**sale_price** | **float, none_type** | The discounted price of the product. | 
**currency** | [**NonNullableCatalogsCurrency**](NonNullableCatalogsCurrency.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


