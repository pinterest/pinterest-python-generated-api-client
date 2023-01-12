# AdResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**pin_id** | **str** | Pin ID. | [optional] 
**ad_account_id** | **str** | The ID of the advertiser that this ad belongs to. | [optional] 
**campaign_id** | **str** | ID of the ad campaign that contains this ad. | [optional] 
**collection_items_destination_url_template** | **str, none_type** | Destination URL template for all items within a collections drawer. | [optional] 
**created_time** | **int** | Pin creation time. Unix timestamp in seconds. | [optional] 
**id** | **str** | The ID of this ad. | [optional] 
**rejected_reasons** | **[str]** | Enum reason why the pin was rejected. Returned if &lt;code&gt;review_status&lt;/code&gt; is \&quot;REJECTED\&quot;. | [optional] 
**rejection_labels** | **[str]** | Text reason why the pin was rejected. Returned if &lt;code&gt;review_status&lt;/code&gt; is \&quot;REJECTED\&quot;. | [optional] 
**review_status** | **str** | Ad review status | [optional] 
**type** | **str** | Always \&quot;ad\&quot;. | [optional] 
**updated_time** | **int** | Last update time. Unix timestamp in seconds. | [optional] 
**summary_status** | **str** | Ad summary status | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


