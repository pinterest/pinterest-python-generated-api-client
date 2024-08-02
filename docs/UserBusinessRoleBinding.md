# UserBusinessRoleBinding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets_summary** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**business_roles** | **[str]** | The access level a user has on the business. This can be EMPLOYEE, BIZ_ADMIN, or PARTNER. | [optional] 
**created_by_business** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Metadata for the business that created the business relationship. | [optional] 
**created_by_user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Metadata for the user that created the business relationship. | [optional] 
**created_time** | **int, none_type** | The time the business relationship was created. Returned in milliseconds. | [optional] 
**id** | **str** | Unique identifier of the business member/business partner/employer. | [optional] 
**is_shared_partner** | **bool** | This field is only relevant when business_role&#x3D;\&quot;PARTNER\&quot;. &lt;br&gt;If is_shared_partner&#x3D;FALSE, the partner can access your business assets. If assets_summary is not empty, the assets listed are your business assets the partner has access to. &lt;br&gt;If is_shared_partner&#x3D;TRUE, you can access the partner&#39;s business asset. If assets_summary is not empty, the assets listed are the partner&#39;s business assets you have access to. | [optional] 
**user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Metadata for the business member/business partner/employer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


