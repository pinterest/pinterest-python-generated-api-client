# CreateMMMReportRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_name** | **str** | Name of the Marketing Mix Modeling (MMM) report | 
**start_date** | **str** | Metric report start date (UTC). Format: YYYY-MM-DD | 
**end_date** | **str** | Metric report end date (UTC). Format: YYYY-MM-DD | 
**granularity** | **str** | DAY - metrics are broken down daily.&lt;br&gt; WEEK - metrics are broken down weekly. | 
**level** | **str** | Level of the report | 
**targeting_types** | **[str]** | List of targeting types | 
**columns** | **[str]** | Metric and entity columns | 
**custom_column_ids** | [**[Items]**](Items.md) | List of custom column ids | [optional] 
**countries** | **[str, none_type]** | A List of country for filtering | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


