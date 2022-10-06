# ConversionEventsUserData

Object containing customer information data. Note, It is required at least one of 1) em, 2) hashed_maids or 3) pair client_ip_address + client_user_agent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**em** | **[str]** | Sha256 hashes of lowercase version of user&#39;s email addresses. Used for matching. | 
**hashed_maids** | **[str]** | Sha256 hashes of user&#39;s \&quot;Google Advertising IDs\&quot; (GAIDs) or \&quot;Apple&#39;s Identifier for Advertisers\&quot; (IDFAs). Used for matching. | 
**client_ip_address** | **str** | The user&#39;s IP address, which can be either in IPv4 or IPv6 format. Used for matching. | 
**client_user_agent** | **str** | The user agent string of the user&#39;s web browser. | 
**ph** | **[str]** | Sha256 hashes of user&#39;s phone numbers, only digits with country code, area code, and number. Remove any symbols, letters, spaces and leading zeros. | [optional] 
**ge** | **[str]** | Sha256 hashes of user&#39;s gender, in lowercase. Either \&quot;f\&quot; or \&quot;m\&quot; or \&quot;n\&quot; for non-binary gender. | [optional] 
**db** | **[str]** | Sha256 hashes of user&#39;s date of birthday, given as year, month, and day. | [optional] 
**ln** | **[str]** | Sha256 hashes of user&#39;s last name, in lowercase. | [optional] 
**fn** | **[str]** | Sha256 hashes of user&#39;s first name, in lowercase. | [optional] 
**ct** | **[str]** | Sha256 hashes of user&#39;s city, in lowercase, and without spaces or punctuation. | [optional] 
**st** | **[str]** | Sha256 hashes of user&#39;s state, given as a two-letter code in lowercase. | [optional] 
**zp** | **[str]** | Sha256 hashes of user&#39;s zipcode, only digits. | [optional] 
**country** | **[str]** | Sha256 hashes of two-character ISO-3166 country code indicating the user&#39;s country, in lowercase. | [optional] 
**external_id** | **[str]** | Sha256 hashes of the unique id from the advertiser that identifies a user in their space, e.g. user id, loyalty id, etc. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


