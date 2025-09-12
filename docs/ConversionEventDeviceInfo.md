# ConversionEventDeviceInfo

Object containing information about the device where event occurred.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **str** | Device brand | [optional] 
**type** | **str** | Device type | [optional] 
**model** | **str** | Device model name | [optional] 
**form_factor** | **str** | Device form factor | [optional] 
**os_family** | **str** | OS Family | [optional] 
**os_name** | **str** | Short name of the OS. This value if specific to os family. Examples: Windows: 10, 11; Android: 16; iOS: 18; MacOS: 15; Linux: Debian, Ubuntu, Arch | [optional] 
**os_version** | **str** | Full name of the version. Examples: iOS: 18.3 Android: 16.1 MacOS: 15.5 Windows: 24H2 Ubuntu Linux: 25.04 | [optional] 
**os_release_name** | **str** | Marketing name for the release version iOS: Dawn Android: Baklava MacOS: Sequoia Ubuntu Linux: Plucky Puffin | [optional] 
**kernel_version** | **str** | Kernel version. Examples: Linux: 6.15. Obtain by running: uname -r MacOS: 24.3.0. Obtain by running: sysctl kern.version Android: 6.6. Obtain from OS.uname().release | [optional] 
**carrier** | **str** | User device&#39;s mobile carrier. | [optional] 
**screen_width** | **int** | Screen width in pixels | [optional] 
**screen_height** | **int** | Screen height in pixels | [optional] 
**screen_density** | **int** | Screen density, PPI | [optional] 
**cpu_cores** | **int** | Number of CPU cores | [optional] 
**storage_size** | **int** | Internal storage size in GB | [optional] 
**storage_free_space** | **int** | Internal storage size in GB | [optional] 
**external_storage_size** | **int** | External storage size in GB | [optional] 
**external_storage_free_space** | **int** | External storage size in GB | [optional] 
**locale** | **str** | Device locale BCP-47 format | [optional] 
**languages** | **[str]** | List of user installed languages. ISO 639-1 format | [optional] 
**timezone** | **str** | Device timezone | [optional] 
**timezone_abbr** | **str** | Timezone abbreviation | [optional] 
**network_type** | **str** | Network type: 4G, 5G, ethernet, wifi In Android: NetworkCapabilities.getNetworkCapabilities() | [optional] 
**battery_level** | **int** | Battery charge level percentage | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


