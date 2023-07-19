# Board

Board

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** | Date and time of board creation. | [optional] [readonly] 
**board_pins_modified_at** | **datetime** | Date and time of last board pins modified. | [optional] [readonly] 
**description** | **str, none_type** |  | [optional] 
**collaborator_count** | **int** | Count of collaborators on the board. | [optional] [readonly] 
**pin_count** | **int** | Count of pins on the board. | [optional] [readonly] 
**follower_count** | **int** | Board follower count. | [optional] [readonly] 
**media** | [**BoardMedia**](BoardMedia.md) |  | [optional] 
**owner** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] [readonly] 
**privacy** | **str** | Privacy setting for a board. Learn more about &lt;a href&#x3D;\&quot;https://help.pinterest.com/en/article/secret-boards\&quot;&gt;secret boards&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://help.pinterest.com/en/business/article/protected-boards\&quot;&gt;protected boards&lt;/a&gt; | [optional]  if omitted the server will use the default value of "PUBLIC"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


