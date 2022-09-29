# TargetingSpec1

Ad group targeting specification defining the ad group target audience. For example, '{\"APPTYPE\":[\"iphone\"], \"GENDER\":[\"male\"], \"LOCALE\":[\"en-US\"], \"LOCATION\":[\"501\"], \"AGE_BUCKET\":[\"25-34\"]}'

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_bucket** | **[str]** | Values: [\&quot;18-24\&quot;,\&quot;21+\&quot;,\&quot;25-34\&quot;,\&quot;35-44\&quot;, \&quot;45-49\&quot;,\&quot;50-54\&quot;,\&quot;55-64\&quot;,\&quot;65+\&quot;] | [optional] 
**apptype** | **[str]** | Values: [\&quot;android_mobile\&quot;, \&quot;android_tablet\&quot;, \&quot;ipad\&quot;, \&quot;iphone\&quot;, \&quot;web\&quot;, \&quot;web_mobile\&quot;] | [optional] 
**audience_exclude** | **[str]** | Excluded customer list IDs. Used to drive new customer acquisition goals. For example: [\&quot;2542620905475\&quot;]. Audience lists need to have at least 100 people with Pinterest accounts in them. | [optional] 
**audience_include** | **[str]** | Targeted customer list IDs. For example: [\&quot;2542620905473\&quot;]. Audience lists need to have at least 100 people with Pinterest accounts in them | [optional] 
**gender** | **[str]** | Targeted genders. Values: [\&quot;unknown\&quot;,\&quot;male\&quot;,\&quot;female\&quot;] | [optional] 
**geo** | **[str]** | Location region codes, e.g., \&quot;BE-VOV\&quot; (East Flanders, Belgium) For complete list, &lt;a href&#x3D;\&quot;https://help.pinterest.com/sub/helpcenter/partner/pinterest_location_targeting_codes.xlsx\&quot; target&#x3D;\&quot;_blank\&quot;&gt;click here&lt;/a&gt; or postal codes, e.g., \&quot;US-94107\&quot;. Use either region codes or postal codes but not both. | [optional] 
**interest** | **[str]** | &lt;a href&#x3D;\&quot;https://docs.google.com/spreadsheets/d/1HxL-0Z3p2fgxis9YBP2HWC3tvPrs1hAuHDRtH-NJTIM/edit#gid&#x3D;118370875\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interest object IDs&lt;/a&gt;. | [optional] 
**locale** | **[str]** | 24 &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 639-1 two letter language codes&lt;/a&gt;. Values: [\&quot;cs\&quot;,\&quot;da\&quot;,\&quot;de\&quot;,\&quot;el\&quot;,\&quot;en\&quot;,\&quot;es\&quot;,\&quot;fi\&quot;,\&quot;fr\&quot;,\&quot;hu\&quot;, \&quot;id\&quot;,\&quot;in\&quot;,\&quot;it\&quot;,\&quot;ja\&quot;,\&quot;ko\&quot;,\&quot;no\&quot;,\&quot;pl\&quot;,\&quot;pt\&quot;,\&quot;ro\&quot;,\&quot;ru\&quot;,\&quot;sk\&quot;,\&quot;sv\&quot;,\&quot;tr\&quot;,\&quot;uk\&quot;,\&quot;zh\&quot;] | [optional] 
**location** | **[str]** | 22 &lt;a href&#x3D;\&quot;https://www.nationsonline.org/oneworld/country_code_list.htm\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO Alpha 2&lt;/a&gt; two letter country codes or &lt;a href&#x3D;\&quot;https://help.pinterest.com/sub/helpcenter/partner/pinterest_location_targeting_codes.xlsx\&quot; target&#x3D;\&quot;_blank\&quot;&gt;US Nielsen DMA (Designated Market Area) codes&lt;/a&gt; (location region codes) (e.g., [\&quot;US\&quot;, \&quot;807\&quot;]). For complete list, &lt;a href&#x3D;\&quot;https://help.pinterest.com/sub/helpcenter/partner/pinterest_location_targeting_codes.xlsx\&quot;&gt;click here&lt;/a&gt;. Location-Country and Location-Metro codes apply. | [optional] 
**shopping_retargeting** | [**[TargetingSpecSHOPPINGRETARGETING]**](TargetingSpecSHOPPINGRETARGETING.md) |  | [optional] 
**targeting_strategy** | **[str]** | Values: [\&quot;CHOOSE_YOUR_OWN\&quot;, \&quot;FIND_NEW_CUSTOMERS\&quot;, \&quot;RECONNECT_WITH_USERS\&quot;] | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


