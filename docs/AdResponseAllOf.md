# AdResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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


