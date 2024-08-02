# InviteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets_summary** | [**InviteAssetsSummary**](InviteAssetsSummary.md) |  | [optional] 
**business_roles** | **[str]** | The access level a user would be granted on the business if the invite/request is accepted. This can be EMPLOYEE, BIZ_ADMIN, or PARTNER. | [optional] 
**created_by_business** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Metadata for the business that created the invite/request. | [optional] 
**created_by_user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Metadata for the user that created the invite/request. | [optional] 
**created_time** | **int** | The time the invite/request was created. Returned in milliseconds. | [optional] 
**id** | **str** | Unique identifier of the invite/request. | [optional] 
**invite_data** | [**BaseInviteDataResponseInviteData**](BaseInviteDataResponseInviteData.md) |  | [optional] 
**is_received_invite** | **bool** | Indicates whether the invite/request was received. | [optional] 
**user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Metadata for the member/partner that was sent the invite/request. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


