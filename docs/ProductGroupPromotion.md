# ProductGroupPromotion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the product group promotion. | [optional] 
**ad_group_id** | **str** | ID of the ad group the product group belongs to. | [optional] 
**type** | **str, none_type** | Product group promotion | [optional] 
**bid_in_micro_currency** | **int** | The bid in micro currency. | [optional] 
**included** | **bool, none_type** | True if the group is BIDDABLE, false if it should be EXCLUDED from serving ads. | [optional] 
**definition** | **str, none_type** | The full product group definition path | [optional] 
**relative_definition** | **str, none_type** | The definition of the product group, relative to its parent - an attribute name/value pair | [optional] 
**parent_id** | **str, none_type** | The parent Product Group ID of this Product Group | [optional] 
**slideshow_collections_title** | **str, none_type** | Slideshow Collections Title | [optional] 
**slideshow_collections_description** | **str, none_type** | Slideshow Collections Description | [optional] 
**status** | [**EntityStatus**](EntityStatus.md) |  | [optional] 
**tracking_url** | **str, none_type** | Tracking template for proudct group promotions. 4000 limit | [optional] 
**catalogs_product_group_id** | **str** | ID of the catalogs product group that this product group promotion references | [optional] 
**catalogs_product_group_name** | **str** | Catalogs product group | [optional] 
**creative_type** | [**CreativeType**](CreativeType.md) |  | [optional] 
**collections_hero_pin_id** | **str, none_type** | Hero Pin ID if this PG is promoted as a Collection | [optional] 
**collections_hero_destination_url** | **str, none_type** | Collections Hero Destination Url | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


