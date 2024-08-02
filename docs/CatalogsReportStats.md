# CatalogsReportStats

Diagnostics aggregated numbers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type** | **str** |  | 
**catalog_id** | **str** | ID of the catalog entity. | [optional] 
**code** | **int** | The event code that a diagnostics aggregated number references | [optional] 
**code_label** | **str** | A human-friendly label for the event code (e.g, &#39;SPAM&#39;) | [optional] 
**message** | **str** | Title message describing the diagnostic issue | [optional] 
**occurrences** | **int** | Number of occurrences of the issue | [optional] 
**severity** | **str** | An ERROR means that items have been dropped, while a WARN denotes that items have been ingested despite an issue | [optional] 
**ineligible_for_ads** | **bool** | Indicates if issue makes items ineligible for ads distribution | [optional] 
**ineligible_for_organic** | **bool** | Indicates if issue makes items ineligible for organic distribution | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


