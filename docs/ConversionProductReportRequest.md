# ConversionProductReportRequest

Request for a brand, category, SKU report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_name** | **str** | Name of the conversion product report. | 
**start_date** | **str** | Metric report start date (UTC). Format: YYYY-MM-DD.&lt;br&gt; Start date must be after 2024-03-16. 7 day minimum time window for report is required. | 
**end_date** | **str** | Metric report end date (UTC). Format: YYYY-MM-DD.&lt;br&gt; A max of 1 year is allowed between the start and end date for reports. | 
**granularity** | **str** | TOTAL - metrics are aggregated over the specified date range.&lt;br&gt; WEEK - metrics are broken down weekly.&lt;br&gt; MONTH - metrics are broken down monthly. | 
**level** | **str** | Level of the report | 
**columns** | [**[ConversionProductReportingColumn]**](ConversionProductReportingColumn.md) | Metric and entity columns | 
**click_window_days** | **int** | Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;30&#x60; days. | [optional]  if omitted the server will use the default value of 30
**view_window_days** | **int** | Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;30&#x60; day. | [optional]  if omitted the server will use the default value of 30
**conversion_report_time** | **str** | The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. | [optional]  if omitted the server will use the default value of "TIME_OF_AD_ACTION"
**conversion_product_breakdown** | **str** | Report breakdown type. This is used to specify the breakdown of the report by brand, category, or SKU. | [optional]  if omitted the server will use the default value of "PRODUCT_BRAND"
**conversion_product_attribution_type** | **str** | Required attribution type of the B/C/S report.&lt;br&gt;When the attribution type is BRAND_ATTRIBUTION, start_date for the report must be after 2025-04-01. | [optional]  if omitted the server will use the default value of "DEFAULT"
**campaign_objective_types** | [**[ObjectiveType]**](ObjectiveType.md) | List of values for filtering. Default is [&#39;CONSIDERATION&#39;,&#39;AWARENESS&#39;,&#39;WEB_CONVERSION&#39;,&#39;VIDEO_COMPLETION&#39;]. | [optional] 
**campaign_ids** | **[str]** | List of campaign ids. &lt;br&gt;Only support campaign_ids field when level of the report is CAMPAIGN. | [optional] 
**ad_group_ids** | **[str]** | List of ad group ids. &lt;br&gt;Only support ad_group_ids field when level of the report is AD_GROUP. | [optional] 
**product_sku_ids** | **[str]** | List of SKU ids. &lt;br&gt;Only support product_sku_ids field when report breakdown type is PRODUCT_SKU_GROUP. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


