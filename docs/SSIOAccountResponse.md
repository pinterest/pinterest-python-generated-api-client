# SSIOAccountResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible** | **bool** | Advertiser eligible to create order lines | [optional] 
**can_edit** | **bool** | Advertiser eligible to update order lines | [optional] 
**billto_infos** | [**[SSIOAccountItem]**](SSIOAccountItem.md) | An array of Salesforce account information that includes address, io terms, etc. | [optional] 
**currency** | **str** |  | [optional] 
**pmp_names** | [**[SSIOAccountPMPName]**](SSIOAccountPMPName.md) |  | [optional] 
**error** | **str** | Error indicator from Salesforce which could be \&quot;No Error\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


