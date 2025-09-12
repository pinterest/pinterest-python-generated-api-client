# BillingInvoiceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the billing invoice | [optional] 
**ad_account_id** | **str** | The ID of the ad account this invoice belongs to | [optional] 
**ad_account_name** | **str** | The name of the ad account this invoice belongs to | [optional] 
**document_type** | **str** | The type of the document | [optional] 
**amount_billed_micro_currency** | **int** | The amount billed in this invoice. Denoted in micro currency | [optional] 
**amount_tax_micro_currency** | **int, none_type** | The tax in this invoice. Denoted in micro currency | [optional] 
**amount_net_micro_currency** | **int, none_type** | The net amount in this invoice. Denoted in micro currency | [optional] 
**amount_discount_micro_currency** | **int, none_type** | The discount in this invoice. Denoted in micro currency | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**billing_period_start_date** | **date** | The start date of the billing period. Format: YYYY-MM-DD | [optional] 
**billing_period_end_date** | **date** | The end date of the billing period. Format: YYYY-MM-DD | [optional] 
**invoice_due_date** | **date** | The date the invoice is due. Format: YYYY-MM-DD | [optional] 
**status** | **str** | The status of the invoice | [optional] 
**payment_terms** | **str** | The payment terms of the invoice | [optional] 
**bill_to_country** | **str** | The country of the bill to address | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


