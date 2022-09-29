# CustomerList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_account_id** | **str** | Associated ad account ID. | [optional] 
**created_time** | **float** | Creation time. Unix timestamp in seconds. | [optional] 
**id** | **str** | Customer list ID. | [optional] 
**name** | **str** | Customer list name. | [optional] 
**num_batches** | **float** | Total number of list updates.  List creation counts as one batch. Each &lt;a href&#x3D;\&quot;/docs/redoc/#operation/ads_v3_customer_list_add_handler_PUT\&quot;&gt;Append&lt;/a&gt; or &lt;a href&#x3D;\&quot;/docs/redoc/#operation/ads_v3_customer_list_remove_handler_PUT\&quot;&gt;Remove API&lt;/a&gt; call counts as another. List creation via the Ads Manager UI could result in more than one batch since the UI breaks up large lists. | [optional] 
**num_removed_user_records** | **float** | Number of removed user records. In a &lt;a href&#x3D;\&quot;/docs/redoc/#operation/ads_v3_customer_list_remove_handler_PUT\&quot;&gt;Remove API&lt;/a&gt; call, this counter increases even if the user is not found in the list. | [optional] 
**num_uploaded_user_records** | **float** | Number of uploaded user records. In an &lt;a href&#x3D;\&quot;/docs/redoc/#operation/ads_v3_customer_list_add_handler_PUT\&quot;&gt;Append API&lt;/a&gt; call, this counter increases even if the uploaded user is already in the list. | [optional] 
**status** | **str** | Customer list status. TOO_SMALL - the list has less than 100 Pinterest users. | [optional] 
**type** | **str** | Always \&quot;customerlist\&quot;. | [optional] 
**updated_time** | **float** | Last update time. Unix timestamp in seconds. | [optional] 
**exceptions** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Customer list errors | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


