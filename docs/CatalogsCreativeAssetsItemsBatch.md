# CatalogsCreativeAssetsItemsBatch

Object describing the catalogs creative assets items batch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_type** | [**CatalogsType**](CatalogsType.md) |  | 
**batch_id** | **str** | Id of the catalogs items batch | [optional] 
**created_time** | **datetime** | Date and time (UTC) of the batch creation: YYYY-MM-DD&#39;T&#39;hh:mm:ss | [optional] [readonly] 
**completed_time** | **datetime, none_type** | Date and time (UTC) of the batch completion: YYYY-MM-DD&#39;T&#39;hh:mm:ss | [optional] [readonly] 
**status** | [**BatchOperationStatus**](BatchOperationStatus.md) |  | [optional] 
**items** | [**[CreativeAssetsProcessingRecord]**](CreativeAssetsProcessingRecord.md) | Array with the catalogs items processing records part of the catalogs items batch | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


