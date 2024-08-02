# DeletePartnerAssetAccessBodyAccesses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | Unique identifier of a business partner to update asset access to. | 
**asset_id** | **str** | Unique identifier of the business asset. | 
**partner_type** | **str** | If partner_type&#x3D;INTERNAL, the deleted asset access is for the access the partner has to your business asset.&lt;br&gt; If partner_type&#x3D;EXTERNAL, the deleted asset access is for the access you have to the partner&#39;s business asset. | [optional]  if omitted the server will use the default value of "INTERNAL"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


