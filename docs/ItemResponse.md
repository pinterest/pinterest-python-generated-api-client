# ItemResponse

Object describing an item record

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The catalog item id in the merchant namespace | [optional] 
**pins** | [**[Pin], none_type**](Pin.md) | &lt;p&gt;&lt;&#x3D; 2000 characters&lt;/p&gt; &lt;p&gt;The pins mapped to the item&lt;/p&gt; | [optional] 
**attributes** | [**ItemAttributes**](ItemAttributes.md) |  | [optional] 
**errors** | [**[ItemValidationEvent]**](ItemValidationEvent.md) | Array with the errors for the item id requested | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


