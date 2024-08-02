# InviteExceptionResponse

An exception object if there is an error performing the action. Will only be provided if there is an error.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invite_or_request_id** | **str, none_type** | Unique identifier of the invite/request. | [optional] 
**code** | **int** | Error code associated with the error in performing the action on the invite/request. | [optional] 
**message** | **str** | Error message associated with the error in performing the action on the invite/request. | [optional] 
**users_or_partner_ids** | **[str], none_type** | A list of users&#39; usernames or emails OR a list of partner ids that caused the error. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


