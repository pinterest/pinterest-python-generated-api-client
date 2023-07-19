# Pin

Pin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**link** | **str, none_type** |  | [optional] 
**title** | **str, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**dominant_color** | **str, none_type** | Dominant pin color. Hex number, e.g. \\\&quot;#6E7874\\\&quot;. | [optional] 
**alt_text** | **str, none_type** |  | [optional] 
**creative_type** | **str, none_type** |  | [optional] [readonly] 
**board_id** | **str** | The board to which this Pin belongs. | [optional] 
**board_section_id** | **str, none_type** | The board section to which this Pin belongs. | [optional] 
**board_owner** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] [readonly] 
**is_owner** | **bool** | Whether the \&quot;operation user_account\&quot; is the Pin owner. | [optional] [readonly] 
**media** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] [readonly] 
**media_source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**parent_pin_id** | **str, none_type** | The source pin id if this pin was saved from another pin. &lt;a href&#x3D;\&quot;https://help.pinterest.com/article/save-pins-on-pinterest\&quot;&gt;Learn more&lt;/a&gt;. | [optional] 
**is_standard** | **bool** | Whether the Pin is standard or not. See documentation on &lt;a href&#x3D;\&quot;https://developers.pinterest.com/docs/content/update/\&quot;&gt;Changes to Pin creation&lt;/a&gt; for more information. | [optional] 
**has_been_promoted** | **bool** | Whether the Pin has been promoted or not. | [optional] [readonly] 
**note** | **str, none_type** | Private note for this Pin. &lt;a href&#x3D;\&quot;https://help.pinterest.com/en/article/add-notes-to-your-pins\&quot;&gt;Learn more&lt;/a&gt;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


