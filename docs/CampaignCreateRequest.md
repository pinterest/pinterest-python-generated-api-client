# CampaignCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_account_id** | **str** | Campaign&#39;s Advertiser ID. | 
**name** | **str** | Campaign name. | 
**objective_type** | [**ObjectiveType**](ObjectiveType.md) |  | 
**status** | **str** |  | [optional]  if omitted the server will use the default value of "ACTIVE"
**lifetime_spend_cap** | **int, none_type** | Campaign total spending cap. | [optional] 
**daily_spend_cap** | **int, none_type** | Campaign daily spending cap. | [optional] 
**order_line_id** | **str, none_type** | Order line ID that appears on the invoice. | [optional] 
**tracking_urls** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**start_time** | **int, none_type** | Campaign start time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns. | [optional] 
**end_time** | **int, none_type** | Campaign end time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns. | [optional] 
**is_campaign_budget_optimization** | **bool** |  | [optional]  if omitted the server will use the default value of False
**is_flexible_daily_budgets** | **bool** |  | [optional]  if omitted the server will use the default value of False
**default_ad_group_budget_in_micro_currency** | **int, none_type** | When transitioning from campaign budget optimization to non-campaign budget optimization, the default_ad_group_budget_in_micro_currency will propagate to each child ad groups daily budget. Unit is micro currency of the associated advertiser account. | [optional] 
**is_automated_campaign** | **bool** |  | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


