# AdsAnalyticsCreateAsyncRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Metric report start date (UTC). Format: YYYY-MM-DD | 
**end_date** | **str** | Metric report end date (UTC). Format: YYYY-MM-DD | 
**granularity** | **str** | TOTAL - metrics are aggregated over the specified date range.&lt;br&gt; DAY - metrics are broken down daily.&lt;br&gt; HOUR - metrics are broken down hourly.&lt;br&gt;WEEKLY - metrics are broken down weekly.&lt;br&gt;MONTHLY - metrics are broken down monthly | 
**columns** | [**[ReportingColumnAsync]**](ReportingColumnAsync.md) | Metric and entity columns. Pin promotion and ad related columns are not supported for the Product Item level reports. | 
**level** | **str** | Level of the report | 
**click_window_days** | **int** | Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;30&#x60; days. | [optional]  if omitted the server will use the default value of 30
**engagement_window_days** | **int** | Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;30&#x60; days. | [optional]  if omitted the server will use the default value of 30
**view_window_days** | **int** | Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to &#x60;1&#x60; day. | [optional]  if omitted the server will use the default value of 1
**conversion_report_time** | **str** | The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. | [optional]  if omitted the server will use the default value of "TIME_OF_AD_ACTION"
**attribution_types** | [**[ConversionReportAttributionType]**](ConversionReportAttributionType.md) | List of types of attribution for the conversion report | [optional] 
**report_format** | **str** | Specification for formatting the report data. Reports in JSON will not zero-fill metrics, whereas reports in CSV will. Both report formats will omit rows where all the columns are equal to 0. | [optional]  if omitted the server will use the default value of "JSON"
**primary_sort** | **str** |  | [optional]  if omitted the server will use the default value of "BY_ID"
**start_hour** | **int** | Which hour of the start date to begin the report. The entire day will be included if no start hour is provided. Only allowed for hourly reports. | [optional] 
**end_hour** | **int** | Which hour of the end date to stop the report (inclusive). For example, with an end_date of &#39;2020-01-01&#39; and end_hour of &#39;15&#39;, the report will contain metrics up to &#39;2020-01-01 14:59:59&#39;. The entire day will be included if no end hour is provided. Only allowed for hourly reports. | [optional] 
**campaign_ids** | **[str]** | List of campaign ids | [optional] 
**campaign_statuses** | [**[CampaignSummaryStatus]**](CampaignSummaryStatus.md) | List of status values for filtering | [optional] 
**campaign_objective_types** | [**[ObjectiveType]**](ObjectiveType.md) | List of values for filtering. [\&quot;WEB_SESSIONS\&quot;] in BETA. | [optional] 
**ad_group_ids** | **[str]** | List of ad group ids | [optional] 
**ad_group_statuses** | [**[AdGroupSummaryStatus]**](AdGroupSummaryStatus.md) | List of values for filtering | [optional] 
**ad_ids** | **[str]** | List of ad ids [This parameter is no supported for Product Item Level Reports] | [optional] 
**ad_statuses** | [**[PinPromotionSummaryStatus]**](PinPromotionSummaryStatus.md) | List of values for filtering [This parameter is not supported for Product Item Level Reports] | [optional] 
**product_group_ids** | **[str]** | List of product group ids | [optional] 
**product_group_statuses** | [**[ProductGroupSummaryStatus]**](ProductGroupSummaryStatus.md) | List of values for filtering | [optional] 
**product_item_ids** | **[str]** | List of product item ids | [optional] 
**targeting_types** | [**[AdsAnalyticsTargetingType]**](AdsAnalyticsTargetingType.md) | List of targeting types. Requires &#x60;level&#x60; to be a value ending in &#x60;_TARGETING&#x60;. [\&quot;AGE_BUCKET_AND_GENDER\&quot;] is in BETA and not yet available to all users. | [optional] 
**metrics_filters** | [**[AdsAnalyticsMetricsFilter]**](AdsAnalyticsMetricsFilter.md) | List of metrics filters | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


