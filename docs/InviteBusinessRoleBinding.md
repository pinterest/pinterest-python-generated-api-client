# InviteBusinessRoleBinding

An invite object if the invite/request was successfully updated. Will only be provided if the an invite/request is successfully updated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_business_id** | **str** | Unique identifier for the business that created the invite/request. | [optional] 
**created_by_user_id** | **str** | Unique identifier for the user that created the invite/request. | [optional] 
**user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Metadata for the user that updated the invite/request. | [optional] 
**id** | **str** | Unique identifier of the invite/request. | [optional] 
**invite_data** | [**BaseInviteDataResponseInviteData**](BaseInviteDataResponseInviteData.md) |  | [optional] 
**is_received_invite** | **bool** | Indicates whether the invite/request was received. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


