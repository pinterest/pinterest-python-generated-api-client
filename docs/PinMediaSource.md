# PinMediaSource

Pin media source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | **str** |  | defaults to "pin_url"
**is_standard** | **bool** | Set the parameter to false to create the new simplified Pin instead of the standard pin. Currently the field is only available to a list of beta users. | [optional]  if omitted the server will use the default value of True
**cover_image_url** | **str** | Cover image url. | [optional] 
**cover_image_content_type** | **str** | Content type for cover image Base64. | [optional] 
**cover_image_data** | **str** | Cover image Base64. | [optional] 
**index** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**media_id** | **str** |  | [optional] 
**items** | [**[PinMediaSourceImagesURLItems]**](PinMediaSourceImagesURLItems.md) | Array with image objects. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


