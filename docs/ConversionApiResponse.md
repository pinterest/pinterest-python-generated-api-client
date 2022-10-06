# ConversionApiResponse

Schema describing the object in the response, which contains information about the events that were received and processed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_events_received** | **int** | Total number of events received in the request. | 
**num_events_processed** | **int** | Number of events that were successfully processed from the events. | 
**events** | [**[ConversionApiResponseEvents]**](ConversionApiResponseEvents.md) | Specific messages for each event received. The order will match the order in which the events were received in the request. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


