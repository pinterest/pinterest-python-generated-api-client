# TargetingTemplateGetResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | targeting template name | [optional] 
**auto_targeting_enabled** | **bool** | Enable auto-targeting for ad group. Also known as &lt;a href&#x3D;\&quot;https://help.pinterest.com/en/business/article/expanded-targeting\&quot; target&#x3D;\&quot;_blank\&quot;&gt;\&quot;expanded targeting\&quot;&lt;/a&gt;. | [optional]  if omitted the server will use the default value of True
**targeting_attributes** | [**TargetingSpec**](TargetingSpec.md) |  | [optional] 
**placement_group** | [**PlacementGroupType**](PlacementGroupType.md) |  | [optional] 
**keywords** | [**[TargetingTemplateKeyword]**](TargetingTemplateKeyword.md) |  | [optional] 
**tracking_urls** | [**TrackingUrls**](TrackingUrls.md) |  | [optional] 
**id** | **str** | Targeting template ID. | [optional] 
**created_time** | **int** | Targeting template created time. Unix timestamp in seconds. | [optional] 
**updated_time** | **int** | Targeting template updated time.Unix timestamp in seconds. | [optional] 
**ad_account_id** | **str** | The ID of the advertiser that this targeting template belongs to. | [optional] 
**status** | **str** | Indicate targeting template is active or Deleted | [optional] 
**sizing** | [**TargetingTemplateAudienceSizing**](TargetingTemplateAudienceSizing.md) |  | [optional] 
**valid** | **bool, none_type** | Inform if the targeting template is valid (ex. would be false if has revoked audience) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


