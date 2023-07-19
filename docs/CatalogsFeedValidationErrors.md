# CatalogsFeedValidationErrors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fetch_error** | **int** | Pinterest couldn&#39;t download your feed. | [optional] 
**fetch_inactive_feed_error** | **int** | Your feed wasn&#39;t ingested because it hasn’t changed in the previous 90 days. | [optional] 
**encoding_error** | **int** | Your feed includes data with an unsupported encoding format. | [optional] 
**delimiter_error** | **int** | Your feed includes data with formatting errors. | [optional] 
**required_columns_missing** | **int** | Your feed is missing some required column headers. | [optional] 
**duplicate_products** | **int** | Some products are duplicated. | [optional] 
**image_link_invalid** | **int** | Some image links are formatted incorrectly. | [optional] 
**itemid_missing** | **int** | Some items are missing an item id in their product metadata, those items will not be published. | [optional] 
**title_missing** | **int** | Some items are missing a title in their product metadata, those items will not be published. | [optional] 
**description_missing** | **int** | Some items are missing a description in their product metadata, those items will not be published. | [optional] 
**product_link_missing** | **int** | Some items are missing a link URL in their product metadata, those items will not be published. | [optional] 
**image_link_missing** | **int** | Some items are missing an image link URL in their product metadata, those items will not be published. | [optional] 
**availability_invalid** | **int** | Some items are missing an availability value in their product metadata, those items will not be published. | [optional] 
**product_price_invalid** | **int** | Some items have price formatting errors in their product metadata, those items will not be published. | [optional] 
**link_format_invalid** | **int** | Some link values are formatted incorrectly. | [optional] 
**parse_line_error** | **int** | Your feed contains formatting errors for some items. | [optional] 
**adwords_format_invalid** | **int** | Some adwords links contain too many characters. | [optional] 
**internal_service_error** | **int** | We experienced a technical difficulty and were unable to ingest your feed. The next ingestion will happen in 24 hours. | [optional] 
**no_verified_domain** | **int** | Your merchant domain needs to be claimed. | [optional] 
**adult_invalid** | **int** | Some items have invalid adult values. | [optional] 
**image_link_length_too_long** | **int** | Some items have image_link URLs that contain too many characters, so those items will not be published. | [optional] 
**invalid_domain** | **int** | Some of your product link values don&#39;t match the verified domain associated with this account. | [optional] 
**feed_length_too_long** | **int** | Your feed contains too many items, some items will not be published. | [optional] 
**link_length_too_long** | **int** | Some product links contain too many characters, those items will not be published. | [optional] 
**malformed_xml** | **int** | Your feed couldn&#39;t be validated because the xml file is formatted incorrectly. | [optional] 
**price_missing** | **int** | Some products are missing a price, those items will not be published. | [optional] 
**feed_too_small** | **int** | Your feed couldn&#39;t be validated because the file doesn&#39;t contain the minimum number of lines required. | [optional] 
**max_items_per_item_group_exceeded** | **int** | Some items exceed the maximum number of items per item group, those items will not be published. | [optional] 
**item_main_image_download_failure** | **int** | Some items&#39; main images can&#39;t be found. | [optional] 
**pinjoin_content_unsafe** | **int** | Some items were not published because they don&#39;t meet Pinterest&#39;s Merchant Guidelines. | [optional] 
**blocklisted_image_signature** | **int** | Some items were not published because they don&#39;t meet Pinterest&#39;s Merchant Guidelines. | [optional] 
**list_price_invalid** | **int** | Some items have list price formatting errors in their product metadata, those items will not be published. | [optional] 
**price_cannot_be_determined** | **int** | Some items were not published because price cannot be determined. The price, list price, and sale price are all different, so those items will not be published. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


