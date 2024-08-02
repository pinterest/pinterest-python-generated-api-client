# CatalogsReportFeedIngestionFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed_id** | **str** | ID of the feed entity. | 
**report_type** | **str** |  | defaults to "FEED_INGESTION_ISSUES"
**processing_result_id** | **str** | Unique identifier of a feed processing result. It can be acquired from the \&quot;id\&quot; field of the \&quot;items\&quot; array within the response of the [List processing results for a given feed](/docs/api/v5/#operation/feed_processing_results/list). If not provided, default to most recent completed processing result. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


