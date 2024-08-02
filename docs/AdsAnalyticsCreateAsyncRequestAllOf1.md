# AdsAnalyticsCreateAsyncRequestAllOf1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**[ReportingColumnAsync]**](ReportingColumnAsync.md) | Metric and entity columns. Pin promotion and ad related columns are not supported for the Product Item level reports. | 
**level** | **str** | Level of the report | 
**report_format** | **str** | Specification for formatting the report data. Reports in JSON will not zero-fill metrics, whereas reports in CSV will. Both report formats will omit rows where all the columns are equal to 0. | [optional]  if omitted the server will use the default value of "JSON"
**primary_sort** | **str** |  | [optional]  if omitted the server will use the default value of "BY_ID"
**start_hour** | **int** | Which hour of the start date to begin the report. The entire day will be included if no start hour is provided. Only allowed for hourly reports. | [optional] 
**end_hour** | **int** | Which hour of the end date to stop the report (inclusive). For example, with an end_date of &#39;2020-01-01&#39; and end_hour of &#39;15&#39;, the report will contain metrics up to &#39;2020-01-01 14:59:59&#39;. The entire day will be included if no end hour is provided. Only allowed for hourly reports. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


