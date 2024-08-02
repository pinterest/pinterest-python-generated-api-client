# DeleteInvitesResultsResponseArray

Response to delete invites sent to Members or Partners, if there is an exception, return the exception mapped with the invite id

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[DeleteInvitesResultsResponseArrayItems]**](DeleteInvitesResultsResponseArrayItems.md) | List of invite/Request deletion status. If there is an error, an exception object will be returned. If the invite/request was successfully cancelled, an invite object will be returned for the invite that was cancelled. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


