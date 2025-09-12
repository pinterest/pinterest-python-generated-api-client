# ConversionEventAppInfo

Object containing information about the application where event occurred.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** | Name of the app. Primarily used for Mobile Apps. | [optional] 
**app_package_name** | **str** | App package name | [optional] 
**app_id** | **str** | App ID in Google Play Store, AppStore or other stores. | [optional] 
**app_version** | **str** | App version. Primarily used for mobile apps | [optional] 
**app_store** | **str** | The name of the app distributor or store from which the app was installed. Some options: Samsung Galaxy Store, Google Play Store, Amazon Store, Apple App Store, F-Droid, Aptoide, Obtanium, Huawei AppGallery, Xiaomi Mi GetApps | [optional] 
**window_width** | **int** | Inner width of the window or viewport. | [optional] 
**window_height** | **int** | Inner height of the window or viewport. | [optional] 
**install_time** | **int** | App install time. Unix timestamp in seconds | [optional] 
**user_agent** | **str** | User Agent request header. Primarily used for Web events | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


