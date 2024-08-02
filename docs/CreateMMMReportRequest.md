# CreateMMMReportRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_name** | **str** | Name of the Marketing Mix Modeling (MMM) report | 
**start_date** | **str** | Metric report start date (UTC). Format: YYYY-MM-DD | 
**end_date** | **str** | Metric report end date (UTC). Format: YYYY-MM-DD | 
**granularity** | **str** | DAY - metrics are broken down daily.&lt;br&gt; WEEK - metrics are broken down weekly. | 
**level** | **str** | Level of the report | 
**targeting_types** | [**[MMMReportingTargetingType]**](MMMReportingTargetingType.md) | List of targeting types | 
**columns** | [**[MMMReportingColumn]**](MMMReportingColumn.md) | Metric and entity columns | 
**countries** | [**[TargetingAdvertiserCountry]**](TargetingAdvertiserCountry.md) | A List of countries for filtering | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


