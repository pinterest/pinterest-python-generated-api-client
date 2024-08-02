# UpdatePartnerAssetsResult

An object containing the permissions a business partner has on the asset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | Unique identifier of a business asset. | [optional] 
**asset_type** | **str** | Type of asset. Currently we only support AD_ACCOUNT and PROFILE, and ASSET_GROUP. | [optional] 
**partner_id** | **str** | Unique identifier of a business partner. | [optional] 
**permissions** | [**PermissionsResponse**](PermissionsResponse.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


