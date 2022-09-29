# CatalogsFeedValidationWarnings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title_length_too_long** | **int** | The title for some items were truncated because they contain too many characters. | [optional] 
**description_length_too_long** | **int** | The description for some items were truncated because they contain too many characters. | [optional] 
**gender_invalid** | **int** | Some items have gender values that are formatted incorrectly, which may limit visibility in recommendations, search results and shopping experiences. | [optional] 
**age_group_invalid** | **int** | Some items have age group values that are formatted incorrectly, which may limit visibility in recommendations, search results and shopping experiences. | [optional] 
**size_type_invalid** | **int** | Some items have size type values that are formatted incorrectly, which may limit visibility in recommendations, search results and shopping experiences. | [optional] 
**link_format_warning** | **int** | Some items have an invalid product link which contains invalid UTM tracking paramaters. | [optional] 
**duplicate_products** | **int** | Some products are duplicated. | [optional] 
**sales_price_invalid** | **int** | Some items have sale price values that are higher than the original price of the item. | [optional] 
**product_category_depth_warning** | **int** | Some items only have 1 or 2 levels of google_product_category values, which may limit visibility in recommendations, search results and shopping experiences. | [optional] 
**adwords_same_as_link** | **int** | Some items have adwords_redirect URLs that are duplicates of the link URLs for those items. | [optional] 
**duplicate_headers** | **int** | Your feed contains duplicate headers. | [optional] 
**fetch_same_signature** | **int** | Ingestion completed early because there are no changes to your feed since the last successful update. | [optional]  if omitted the server will use the default value of 1
**adwords_format_warning** | **int** | Some items have adwords_redirect links that are formatted incorrectly. | [optional] 
**additional_image_link_length_too_long** | **int** | Some items have additional_image_link URLs that contain too many characters, so those items will not be published. | [optional] 
**additional_image_link_warning** | **int** | Some items have additional_image_link URLs that are formatted incorrectly and will not be published with your items. | [optional] 
**image_link_warning** | **int** | Some items have image_link URLs that are formatted incorrectly and will not be published with those items. | [optional] 
**shipping_invalid** | **int** | Some items have shipping values that are formatted incorrectly. | [optional] 
**tax_invalid** | **int** | Some items have tax values that are formatted incorrectly. | [optional] 
**shipping_weight_invalid** | **int** | Some items have invalid shipping_weight values. | [optional] 
**expiration_date_invalid** | **int** | Some items have expiration_date values that are formatted incorrectly, those items will be published without an expiration date. | [optional] 
**availability_date_invalid** | **int** | Some items have availability_date values that are formatted incorrectly, those items will be published without an availability date. | [optional] 
**sale_date_invalid** | **int** | Some items have sale_price_effective_date values that are formatted incorrectly, those items will be published without a sale date. | [optional] 
**weight_unit_invalid** | **int** | Some items have weight_unit values that are formatted incorrectly, those items will be published without a weight unit. | [optional] 
**is_bundle_invalid** | **int** | Some items have is_bundle values that are formatted incorrectly, those items will be published without being bundled with other products. | [optional] 
**updated_time_invalid** | **int** | Some items have updated_time values thate are formatted incorrectly, those items will be published without an updated time. | [optional] 
**custom_label_length_too_long** | **int** | Some items have custom_label values that are too long, those items will be published without that custom label. | [optional] 
**product_type_length_too_long** | **int** | Some items have product_type values that are too long, those items will be published without that product type. | [optional] 
**too_many_additional_image_links** | **int** | Some items have additional_image_link values that exceed the limit for additional images, those items will be published without some of your images. | [optional] 
**multipack_invalid** | **int** | Some items have invalid multipack values. | [optional] 
**indexed_product_count_large_delta** | **int** | The product count has increased or decreased significantly compared to the last successful ingestion. | [optional] 
**item_additional_image_download_failure** | **int** | Some items include additional_image_links that can&#39;t be found. | [optional] 
**optional_product_category_missing** | **int** | Some items are missing a google_product_category. | [optional] 
**optional_product_category_invalid** | **int** | Some items include google_product_category values that are not formatted correctly according to the GPC taxonomy. | [optional] 
**optional_condition_missing** | **int** | Some items are missing a condition value, which may limit visibility in recommendations, search results and shopping experiences. | [optional] 
**optional_condition_invalid** | **int** | Some items include condition values that are formatted incorrectly, which may limit visibility in recommendations, search results and shopping experiences. | [optional] 
**ios_deep_link_invalid** | **int** | Some items include invalid ios_deep_link values. | [optional] 
**android_deep_link_invalid** | **int** | Some items include invalid android_deep_link. | [optional] 
**availability_normalized** | **int** | Some items include availability values that are formatted incorrectly and have been automatically corrected. | [optional] 
**condition_normalized** | **int** | Some items include condition values that are formatted incorrectly and have been automatically corrected. | [optional] 
**gender_normalized** | **int** | Some items include gender values that are formatted incorrectly and have been automatically corrected. | [optional] 
**size_type_normalized** | **int** | Some items include size_type values that are formatted incorrectly and have been automatically corrected. | [optional] 
**age_group_normalized** | **int** | Some items include age_group values that are formatted incorrectly and have been automatically corrected. | [optional] 
**utm_source_auto_corrected** | **int** | Some items include utm_source values that are formatted incorrectly and have been automatically corrected. | [optional] 
**country_does_not_map_to_currency** | **int** | Some items include a currency that doesn&#39;t match the usual currency for the location where that product is sold or shipped. | [optional] 
**min_ad_price_invalid** | **int** | Some items include min_ad_price values that are formatted incorrectly. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


