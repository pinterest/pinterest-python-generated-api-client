# BulkDownloadRequest

Ad entities to get in bulk request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_types** | **[str]** | All entity types specified will be downloaded. Fewer types result in faster downloads. | [optional] 
**entity_ids** | **[str]** | All entities specified by these IDs as well as their children and grandchildren will be downloaded if the entity type is one of the types requested to be downloaded. | [optional] 
**updated_since** | **str** | Unix UTC timestamp to retrieve all entities that have changed since this time. | [optional] 
**campaign_filter** | [**BulkDownloadRequestCampaignFilter**](BulkDownloadRequestCampaignFilter.md) |  | [optional] 
**output_format** | **str** |  | [optional]  if omitted the server will use the default value of "JSON"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


