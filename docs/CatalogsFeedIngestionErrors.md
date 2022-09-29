# CatalogsFeedIngestionErrors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_download_error** | **int** | Some items include images that can&#39;t be found. | [optional] 
**line_level_internal_error** | **int** | We experienced a technical difficulty and were unable to ingest this some items. The next ingestion will happen in 24 hours. | [optional] 
**large_product_count_decrease** | **int** | The product count has decreased by more than 99% compared to the last successful ingestion. | [optional]  if omitted the server will use the default value of 1
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


