# AdPreviewShopping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_product_group_id** | **str** | Catalog Product Group Id. | 
**creative_type** | **str** | Ad format of the shopping ad preview. | 
**customizable_cta_type** | [**CustomizableCtaType**](CustomizableCtaType.md) |  | [optional] 
**image_tag** | **str** | Multi image template tag. | [optional] 
**video_tag** | **str** | Multi video template tag, image_tag and video_tag are mutual exclusive. | [optional] 
**preferred_media_type** | **str** | Preferred media type. | [optional] 
**hero_pin_id** | **str** | Pin id for the hero image. When creative type is COLLECTION, either hero_pin_id or (hero_image_url, hero_image_title) is required. | [optional] 
**hero_image_url** | **str** | Hero image URL. | [optional] 
**hero_image_title** | **str** | Title displayed below ad. | [optional] 
**item_id** | **str** | Item id for product to preview standard shopping ads, optional and only applicable when creative type is SHOPPING. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


