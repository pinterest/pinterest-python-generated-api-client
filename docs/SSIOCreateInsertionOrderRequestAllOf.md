# SSIOCreateInsertionOrderRequestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmp_id** | **str** | The pmp id | 
**order_name** | **str** | The order name | 
**order_line_type** | **str** | Type can be Budget or Perpetual | 
**accepted_terms_id** | **str** | The SFDC id for the terms | 
**billto_company_id** | **str** | The bill-to company id | 
**billto_business_address_id** | **str** | The bill-to business address id | 
**billto_billing_address_id** | **str** | The bill-to billing address id | 
**currency_info** | [**Currency**](Currency.md) |  | 
**accepted_terms_time** | **int** | The UTC timestamp (to the nearest sec) of when terms were accepted | [optional] 
**estimated_monthly_spend** | **float** | If Ongoing (perpetual) order line, the estimated monthly spend | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


