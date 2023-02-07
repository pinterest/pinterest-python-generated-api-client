# CatalogProductGroup

non-promoted catalog product group entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the catalog product group. | [optional] 
**merchant_id** | **str** | Merchant ID pertaining to the owner of the catalog product group. | [optional] 
**name** | **str** | Name of catalog product group | [optional] 
**filters** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Object holding a list of filters | [optional] 
**filter_v2** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Object holding a list of filters | [optional] 
**type** | [**Board**](Board.md) |  | [optional] 
**status** | [**EntityStatus**](EntityStatus.md) |  | [optional] 
**feed_profile_id** | **str** | id of the feed profile belonging to this catalog product group | [optional] 
**created_at** | **int** | Unix timestamp in seconds of when catalog product group was created. | [optional] 
**last_update** | **int** | Unix timestamp in seconds of last time catalog product group was updated. | [optional] 
**product_count** | **int** | Amount of products in the catalog product group | [optional] 
**featured_position** | **int** | index of the featured position of the catalog product group | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


