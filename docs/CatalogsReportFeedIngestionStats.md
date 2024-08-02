# CatalogsReportFeedIngestionStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type** | **str** |  | [optional]  if omitted the server will use the default value of "FEED_INGESTION_ISSUES"
**catalog_id** | **str** | ID of the catalog entity. | [optional] 
**code** | **int** | The event code that a diagnostics aggregated number references | [optional] 
**code_label** | **str** | A human-friendly label for the event code (e.g, &#39;AVAILABILITY_INVALID&#39;) | [optional] 
**message** | **str** | Title message describing the diagnostic issue | [optional] 
**occurrences** | **int** | Number of occurrences of the issue | [optional] 
**severity** | **str** | An ERROR means that items have been dropped, while a WARN denotes that items have been ingested despite an issue | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


