# CampaignCommon

Campaign Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_account_id** | **str** | Campaign&#39;s Advertiser ID. If you want to create a campaign in a Business Account shared account you need to specify the Business Access advertiser ID in both the query path param as well as the request body schema. | [optional] 
**name** | **str** | Campaign name. | [optional] 
**status** | **str** |  | [optional] 
**lifetime_spend_cap** | **int, none_type** | Campaign total spending cap. Required for Campaign Budget Optimization (CBO) campaigns. This and \&quot;daily_spend_cap\&quot; cannot be set at the same time. | [optional] 
**daily_spend_cap** | **int, none_type** | Campaign daily spending cap. Required for Campaign Budget Optimization (CBO) campaigns. This and \&quot;lifetime_spend_cap\&quot; cannot be set at the same time. | [optional] 
**order_line_id** | **str, none_type** | Order line ID that appears on the invoice. | [optional] 
**tracking_urls** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**start_time** | **int, none_type** | Campaign start time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns. | [optional] 
**end_time** | **int, none_type** | Campaign end time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns. | [optional] 
**is_flexible_daily_budgets** | **bool, none_type** | Determine if a campaign has flexible daily budgets setup. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


