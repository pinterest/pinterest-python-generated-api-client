# SSIOCreateInsertionOrderRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Starting date of time period. Format: YYYY-MM-DD | 
**po_number** | **str** | The po number | 
**billing_contact_firstname** | **str** | The billing contact first name | 
**billing_contact_lastname** | **str** | The billing contact last name | 
**billing_contact_email** | **str** | The billing contact email | 
**media_contact_firstname** | **str** | The media contact first name | 
**media_contact_lastname** | **str** | The media contact last name | 
**media_contact_email** | **str** | The media contact email | 
**pmp_id** | **str** | The pmp id | 
**order_name** | **str** | The order name | 
**order_line_type** | **str** | Type can be Budget or Perpetual | 
**accepted_terms_id** | **str** | The SFDC id for the terms | 
**billto_company_id** | **str** | The bill-to company id | 
**billto_business_address_id** | **str** | The bill-to business address id | 
**billto_billing_address_id** | **str** | The bill-to billing address id | 
**currency_info** | [**Currency**](Currency.md) |  | 
**end_date** | **str** | End date of time period. Format: YYYY-MM-DD | [optional] 
**budget_amount** | **float** | If Budget order line, the budget amount. | [optional] 
**agency_link** | **str** | URL link for agency | [optional] 
**user_email** | **str** | The email of user submitting the insertion order | [optional] 
**accepted_terms_time** | **int** | The UTC timestamp (to the nearest sec) of when terms were accepted | [optional] 
**estimated_monthly_spend** | **float** | If Ongoing (perpetual) order line, the estimated monthly spend | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


