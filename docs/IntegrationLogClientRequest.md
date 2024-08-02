# IntegrationLogClientRequest

HTTP request details included in the log sent by the client.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**host** | **str** | HTTP request host from host header. | 
**path** | **str** | HTTP request path. | 
**request_headers** | **{str: (str,)}** | HTTP request headers as key-value pairs. | [optional] 
**response_headers** | **{str: (str,)}** | HTTP response headers as key-value pairs. | [optional] 
**response_status_code** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


