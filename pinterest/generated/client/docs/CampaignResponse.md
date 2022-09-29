# CampaignResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Campaign ID. | [optional] 
**ad_account_id** | **str** | Campaign&#39;s Advertiser ID. | [optional] 
**name** | **str** | Campaign name. | [optional] 
**status** | **str** |  | [optional] 
**lifetime_spend_cap** | **int, none_type** | Campaign total spending cap. | [optional] 
**daily_spend_cap** | **int, none_type** | Campaign daily spending cap. | [optional] 
**order_line_id** | **str, none_type** | Order line ID that appears on the invoice. | [optional] 
**tracking_urls** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**start_time** | **int, none_type** | Campaign start time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns. | [optional] 
**end_time** | **int, none_type** | Campaign end time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns. | [optional] 
**objective_type** | [**ObjectiveType**](ObjectiveType.md) |  | [optional] 
**created_time** | **int** | Campaign creation time. Unix timestamp in seconds. | [optional] 
**updated_time** | **int** | UTC timestamp. Last update time. | [optional] 
**type** | **str** | Always \&quot;campaign\&quot;. | [optional] 
**is_flexible_daily_budgets** | **bool, none_type** | Determines if a campaign has flexible daily budgets setup. | [optional] 
**is_campaign_budget_optimization** | **bool, none_type** | Determines if a campaign automatically generate ad-group level budgets given a campaign budget to maximize campaign outcome. When transitioning from non-cbo to cbo, all previous child ad group budget will be cleared. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


