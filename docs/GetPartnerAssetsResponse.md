# GetPartnerAssetsResponse

An object containing the permissions a you/your business partner has on the asset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | Unique identifier of a business asset. | [optional] 
**asset_type** | **str** | Type of asset. Currently we only support AD_ACCOUNT and PROFILE, and ASSET_GROUP. | [optional] 
**permissions** | **[str]** | The permissions you or your partner has on the asset. If partner_type&#x3D;INTERNAL, the permission levels are for the access the partner has to your business asset.&lt;br&gt; If partner_type&#x3D;EXTERNAL, the permission levels are for the access you have to the partner&#39;s business asset. | [optional] 
**asset_group_info** | [**AssetGroupBinding**](AssetGroupBinding.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


