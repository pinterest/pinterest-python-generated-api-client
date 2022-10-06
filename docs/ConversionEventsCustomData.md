# ConversionEventsCustomData

Object containing other custom data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str, none_type** | The ISO-4217 currency code. If not provided, we will default to the advertiser&#39;s currency set during account creation. | [optional] 
**value** | **str, none_type** | Total value of the event. Accepted as a string in the request; it will be parsed into a double. For example, if there are two items in a checkout event, the value should be the total price | [optional] 
**content_ids** | **[str]** | List of products IDs | [optional] 
**contents** | [**[ConversionEventsCustomDataContents]**](ConversionEventsCustomDataContents.md) | A list of objects containing information about products, such as price and quantity. | [optional] 
**num_items** | **int** | Total number of products of the event. For example, the total number of items purchased in a checkout event. | [optional] 
**order_id** | **str, none_type** | The order ID | [optional] 
**search_string** | **str, none_type** | The search string related to the user conversion event. | [optional] 
**np** | **str, none_type** | Named partner. Not required, this is for Pinterest internal use only. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


