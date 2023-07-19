# ItemBatchRecord

Object describing an item batch record

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The catalog item id in the merchant namespace | [optional] 
**attributes** | [**UpdatableItemAttributes**](UpdatableItemAttributes.md) |  | [optional] 
**update_mask** | **[str], none_type** | The list of product attributes to be updated. Attributes specified in the update mask without a value specified in the body will be deleted from the product item. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


