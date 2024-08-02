# AdGroupAudienceSizingRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_targeting_enabled** | **bool** | Enable auto-targeting for ad group. Also known as &lt;a href&#x3D;\&quot;https://help.pinterest.com/en/business/article/expanded-targeting\&quot; target&#x3D;\&quot;_blank\&quot;&gt;\&quot;expanded targeting\&quot;&lt;/a&gt;. | [optional]  if omitted the server will use the default value of True
**placement_group** | **str** | &lt;a href&#x3D;\&quot;/docs/redoc/#section/Placement-group\&quot;&gt;Placement group&lt;/a&gt;. | [optional]  if omitted the server will use the default value of "ALL"
**creative_types** | **[str], none_type** | Pin creative types filter. &lt;/p&gt;&lt;strong&gt;Note:&lt;/strong&gt; SHOP_THE_PIN has been deprecated. Please use COLLECTION instead. | [optional] 
**targeting_spec** | [**TargetingSpec**](TargetingSpec.md) |  | [optional] 
**product_group_ids** | **[str], none_type** | Targeted product group IDs. &lt;/p&gt;&lt;strong&gt;Note:&lt;/strong&gt; This can only be combined with shopping/catalog sales campaigns. For more information, &lt;a href&#x3D;\&quot;https://help.pinterest.com/en/business/article/shopping-ads#section-14571\&quot; target&#x3D;\&quot;_blank\&quot;&gt;click here&lt;/a&gt;. SHOPPING_RETARGETING must be included in targeting_spec object or this field will be ignored. | [optional] 
**keywords** | [**[AdGroupAudienceSizingRequestKeywords], none_type**](AdGroupAudienceSizingRequestKeywords.md) | Array of keyword objects. If the keywords field is missing, all keywords will be targeted. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


