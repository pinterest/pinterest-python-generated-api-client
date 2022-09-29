# TargetingSpec

Ad group targeting specification defining the ad group target audience. For example, {\"APPTYPE\":[\"iphone\"], \"GENDER\":[\"male\"], \"LOCALE\":[\"en-US\"], \"LOCATION\":[\"501\"], \"AGE_BUCKET\":[\"25-34\"]}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_bucket** | **[str], none_type** | Age ranges | [optional] 
**apptype** | **[str], none_type** | Allowed devices | [optional] 
**audience_exclude** | **[str], none_type** | Excluded customer list IDs. Used to drive new customer acquisition goals. For example: [\&quot;2542620905475\&quot;]. Audience lists need to have at least 100 people with Pinterest accounts in them. | [optional] 
**audience_include** | **[str], none_type** | Targeted customer list IDs. For example: [\&quot;2542620905473\&quot;]. Audience lists need to have at least 100 people with Pinterest accounts in them | [optional] 
**gender** | **[str], none_type** | Targeted genders. Values: [\&quot;unknown\&quot;,\&quot;male\&quot;,\&quot;female\&quot;] | [optional] 
**geo** | **[str], none_type** | Location region codes, e.g., \&quot;BE-VOV\&quot; (East Flanders, Belgium) For complete list, &lt;a href&#x3D;\&quot;https://help.pinterest.com/sub/helpcenter/partner/pinterest_location_targeting_codes.xlsx\&quot; target&#x3D;\&quot;_blank\&quot;&gt;click here&lt;/a&gt; or postal codes, e.g., \&quot;US-94107\&quot;. Use either region codes or postal codes but not both. | [optional] 
**interest** | **[str]** | Array of interest object IDs. | [optional] 
**locale** | **[str], none_type** | 24 ISO 639-1 two letter language codes. | [optional] 
**location** | **[str], none_type** | 22 ISO Alpha 2 two letter country codes or US Nielsen DMA (Designated Market Area) codes (location region codes) (e.g., [\&quot;US\&quot;, \&quot;807\&quot;]). For complete list, click here. Location-Country and Location-Metro codes apply. | [optional] 
**shopping_retargeting** | [**[TargetingSpecSHOPPINGRETARGETING1], none_type**](TargetingSpecSHOPPINGRETARGETING1.md) | Array of object: lookback_window [Integer]: Number of days ago to start lookback timeframe for dynamic retargeting tag_types [Array of integer]: Event types to target for dynamic retargeting exclusion_window [Integer]: Number of days ago to stop lookback timeframe for dynamic retargeting | [optional] 
**targeting_strategy** | **[str], none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


