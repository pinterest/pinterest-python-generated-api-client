# AdGroupResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Ad group ID. | [optional] 
**ad_account_id** | **str** | Advertiser ID. | [optional] 
**created_time** | **int** | Ad group creation time. Unix timestamp in seconds. | [optional] 
**updated_time** | **int** | Ad group last update time. Unix timestamp in seconds. | [optional] 
**type** | **str** | Always \&quot;adgroup\&quot;. | [optional]  if omitted the server will use the default value of "adgroup"
**conversion_learning_mode_type** | **str, none_type** | oCPM learn mode | [optional] 
**summary_status** | **str** | Ad group summary status. | [optional] 
**feed_profile_id** | **str** | Feed Profile ID associated to the adgroup. | [optional] 
**dca_assets** | **bool, date, datetime, dict, float, int, list, str, none_type** | [DCA] The Dynamic creative assets to use for DCA. Dynamic Creative Assembly (DCA) accepts basic creative assets of an ad (image, video, title, call to action, logo etc). Then it automatically generates optimized ad combinations based on these assets. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


