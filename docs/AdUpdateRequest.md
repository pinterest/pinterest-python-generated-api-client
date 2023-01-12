# AdUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this ad. | 
**ad_group_id** | **str** | ID of the ad group that contains the ad. | [optional] 
**android_deep_link** | **str, none_type** | Deep link URL for Android devices. Not currently available. Using this field will generate an error. | [optional] 
**carousel_android_deep_links** | **[str], none_type** | Comma-separated deep links for the carousel pin on Android. | [optional] 
**carousel_destination_urls** | **[str], none_type** | Comma-separated destination URLs for the carousel pin to promote. | [optional] 
**carousel_ios_deep_links** | **[str], none_type** | Comma-separated deep links for the carousel pin on iOS. | [optional] 
**click_tracking_url** | **str, none_type** | Tracking url for the ad clicks. | [optional] 
**creative_type** | [**CreativeType**](CreativeType.md) |  | [optional] 
**destination_url** | **str, none_type** | Destination URL. | [optional] 
**ios_deep_link** | **str, none_type** | Deep link URL for iOS devices. Not currently available. Using this field will generate an error. | [optional] 
**is_pin_deleted** | **bool** | Is original pin deleted? | [optional] 
**is_removable** | **bool** | Is pin repinnable? | [optional] 
**name** | **str, none_type** | Name of the ad - 255 chars max. | [optional] 
**status** | [**EntityStatus**](EntityStatus.md) |  | [optional] 
**tracking_urls** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**view_tracking_url** | **str, none_type** | Tracking URL for ad impressions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


