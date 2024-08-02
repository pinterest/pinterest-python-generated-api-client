# CreateMembershipOrPartnershipInvitesBody

Body to be used on path to send Members or Partners Invite or Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_role** | **str** | The business access level to grant member/partner. Note, values are case-sensitive. - EMPLOYEE: Can only view and access assets you assign them to. They cannot see details about other employees, partners, or other assets. - BIZ_ADMIN: Have full control of roles and can add employees and partners as well as grant asset access. - PARTNER: Can only view and access assets you assign them to/or they assign to you. | 
**invite_type** | [**InviteType**](InviteType.md) |  | 
**members** | **[str]** | A list of usernames, emails, or a mix of them. Should be used if invite_type is MEMBER_INVITE | [optional] 
**partners** | **[str]** | A list of partner_id. Should be used if invite_type is PARTNER_INVITE or PARTNER_REQUEST | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


