# openapi_generated.pinterest_client.BusinessAccessAssetsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_group_create**](BusinessAccessAssetsApi.md#asset_group_create) | **POST** /businesses/{business_id}/asset_groups | Create a new asset group.
[**asset_group_delete**](BusinessAccessAssetsApi.md#asset_group_delete) | **DELETE** /businesses/{business_id}/asset_groups | Delete asset groups.
[**asset_group_update**](BusinessAccessAssetsApi.md#asset_group_update) | **PATCH** /businesses/{business_id}/asset_groups | Update asset groups.
[**business_asset_members_get**](BusinessAccessAssetsApi.md#business_asset_members_get) | **GET** /businesses/{business_id}/assets/{asset_id}/members | Get members with access to asset
[**business_asset_partners_get**](BusinessAccessAssetsApi.md#business_asset_partners_get) | **GET** /businesses/{business_id}/assets/{asset_id}/partners | Get partners with access to asset
[**business_assets_get**](BusinessAccessAssetsApi.md#business_assets_get) | **GET** /businesses/{business_id}/assets | List business assets
[**business_member_assets_get**](BusinessAccessAssetsApi.md#business_member_assets_get) | **GET** /businesses/{business_id}/members/{member_id}/assets | Get assets assigned to a member
[**business_members_asset_access_delete**](BusinessAccessAssetsApi.md#business_members_asset_access_delete) | **DELETE** /businesses/{business_id}/members/assets/access | Delete member access to asset
[**business_members_asset_access_update**](BusinessAccessAssetsApi.md#business_members_asset_access_update) | **PATCH** /businesses/{business_id}/members/assets/access | Assign/Update member asset permissions
[**business_partner_asset_access_get**](BusinessAccessAssetsApi.md#business_partner_asset_access_get) | **GET** /businesses/{business_id}/partners/{partner_id}/assets | Get assets assigned to a partner or assets assigned by a partner
[**delete_partner_asset_access_handler_impl**](BusinessAccessAssetsApi.md#delete_partner_asset_access_handler_impl) | **DELETE** /businesses/{business_id}/partners/assets | Delete partner access to asset
[**update_partner_asset_access_handler_impl**](BusinessAccessAssetsApi.md#update_partner_asset_access_handler_impl) | **PATCH** /businesses/{business_id}/partners/assets | Assign/Update partner asset permissions


# **asset_group_create**
> CreateAssetGroupResponse asset_group_create(business_id, create_asset_group_body)

Create a new asset group.

Create a new asset group with the specified parameters. - An <a href=\"https://help.pinterest.com/en/business/article/asset-groups\">asset group</a> is a custom group of assets based on how you’d like to manage your accounts.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_assets_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.create_asset_group_response import CreateAssetGroupResponse
from openapi_generated.pinterest_client.model.create_asset_group_body import CreateAssetGroupBody
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_access_assets_api.BusinessAccessAssetsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    create_asset_group_body = CreateAssetGroupBody(
        asset_group_name="Canada Ad Accounts",
        asset_group_description="Asset groups that has ad accounts shared in Canada",
        asset_group_types=AssetGroupTypes([
            AssetGroupType("["BRAND","LOCATION_OR_LANGUAGE","PRODUCT_LINE","OTHER"]"),
        ]),
    ) # CreateAssetGroupBody | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new asset group.
        api_response = api_instance.asset_group_create(business_id, create_asset_group_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->asset_group_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **create_asset_group_body** | [**CreateAssetGroupBody**](CreateAssetGroupBody.md)|  |

### Return type

[**CreateAssetGroupResponse**](CreateAssetGroupResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid parameters. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_group_delete**
> DeleteAssetGroupResponse asset_group_delete(business_id, delete_asset_group_body)

Delete asset groups.

Delete a batch of asset groups.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_assets_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.delete_asset_group_body import DeleteAssetGroupBody
from openapi_generated.pinterest_client.model.delete_asset_group_response import DeleteAssetGroupResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_access_assets_api.BusinessAccessAssetsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    delete_asset_group_body = DeleteAssetGroupBody(
        asset_groups_to_delete=["666791336903426391","666791336903426392"],
    ) # DeleteAssetGroupBody | 

    # example passing only required values which don't have defaults set
    try:
        # Delete asset groups.
        api_response = api_instance.asset_group_delete(business_id, delete_asset_group_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->asset_group_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **delete_asset_group_body** | [**DeleteAssetGroupBody**](DeleteAssetGroupBody.md)|  |

### Return type

[**DeleteAssetGroupResponse**](DeleteAssetGroupResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid parameters. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_group_update**
> UpdateAssetGroupResponse asset_group_update(business_id, update_asset_group_body)

Update asset groups.

Update a batch of asset groups with the specified parameters.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_assets_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.update_asset_group_body import UpdateAssetGroupBody
from openapi_generated.pinterest_client.model.update_asset_group_response import UpdateAssetGroupResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_access_assets_api.BusinessAccessAssetsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    update_asset_group_body = UpdateAssetGroupBody(
        asset_groups_to_update=[
            UpdateAssetGroupBodyAssetGroupsToUpdate(
                asset_group_id="666791336903426391",
                name="Canada Ad Accounts",
                description="Asset groups that has ad accounts shared in Canada",
                asset_group_types=AssetGroupTypes([
                    AssetGroupType("["BRAND","LOCATION_OR_LANGUAGE","PRODUCT_LINE","OTHER"]"),
                ]),
                assets_to_add=[
                    "549755885175",
                ],
                assets_to_remove=[
                    "549755885175",
                ],
            ),
        ],
    ) # UpdateAssetGroupBody | 

    # example passing only required values which don't have defaults set
    try:
        # Update asset groups.
        api_response = api_instance.asset_group_update(business_id, update_asset_group_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->asset_group_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **update_asset_group_body** | [**UpdateAssetGroupBody**](UpdateAssetGroupBody.md)|  |

### Return type

[**UpdateAssetGroupResponse**](UpdateAssetGroupResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid parameters. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_asset_members_get**
> bool, date, datetime, dict, float, int, list, str, none_type business_asset_members_get(business_id, asset_id)

Get members with access to asset

Get all the members the requesting business has granted access to on the given asset.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_assets_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.user_single_asset_binding import UserSingleAssetBinding
from openapi_generated.pinterest_client.model.paginated import Paginated
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_access_assets_api.BusinessAccessAssetsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    asset_id = "729090764583391194" # str | Unique identifier of a business asset.
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    start_index = 0 # int | An index to start fetching the results from. Only the results starting from this index will be returned. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Get members with access to asset
        api_response = api_instance.business_asset_members_get(business_id, asset_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->business_asset_members_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get members with access to asset
        api_response = api_instance.business_asset_members_get(business_id, asset_id, bookmark=bookmark, page_size=page_size, start_index=start_index)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->business_asset_members_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **asset_id** | **str**| Unique identifier of a business asset. |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **start_index** | **int**| An index to start fetching the results from. Only the results starting from this index will be returned. | [optional] if omitted the server will use the default value of 0

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_asset_partners_get**
> bool, date, datetime, dict, float, int, list, str, none_type business_asset_partners_get(business_id, asset_id)

Get partners with access to asset

Get all the partners the requesting business has granted access to on the given asset. Note: If the asset has been shared with you, an empty array will be returned. This is because an asset shared with you cannot be shared with a different partner.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_assets_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.user_single_asset_binding import UserSingleAssetBinding
from openapi_generated.pinterest_client.model.paginated import Paginated
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_access_assets_api.BusinessAccessAssetsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    asset_id = "729090764583391194" # str | Unique identifier of a business asset.
    start_index = 0 # int | An index to start fetching the results from. Only the results starting from this index will be returned. (optional) if omitted the server will use the default value of 0
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get partners with access to asset
        api_response = api_instance.business_asset_partners_get(business_id, asset_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->business_asset_partners_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get partners with access to asset
        api_response = api_instance.business_asset_partners_get(business_id, asset_id, start_index=start_index, bookmark=bookmark, page_size=page_size)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->business_asset_partners_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **asset_id** | **str**| Unique identifier of a business asset. |
 **start_index** | **int**| An index to start fetching the results from. Only the results starting from this index will be returned. | [optional] if omitted the server will use the default value of 0
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_assets_get**
> bool, date, datetime, dict, float, int, list, str, none_type business_assets_get(business_id)

List business assets

Get all the assets the requesting business has access to. This includes assets the business owns and assets the business has access to through partnerships.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_assets_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.permissions_with_owner import PermissionsWithOwner
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.get_business_assets_response import GetBusinessAssetsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_access_assets_api.BusinessAccessAssetsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    permissions = [
        PermissionsWithOwner("ADMIN"),
    ] # [PermissionsWithOwner] | A list of asset permissions used to filter the assets. Only assets where the requesting business has at least one of the specified permissions will be returned. (optional)
    child_asset_id = "549764894835" # str | A child asset unique identifier. Used to fetch asset groups that contain the asset id as a child. (optional)
    asset_group_id = "7078106104032" # str | An asset group unique identifier. Used to fetch assets contained within the specified asset group. (optional)
    asset_type = "AD_ACCOUNT" # str | A resource type to filter the assets by. Only assets of the specified type will be returned. (optional) if omitted the server will use the default value of "AD_ACCOUNT"
    start_index = 0 # int | An index to start fetching the results from. Only the results starting from this index will be returned. (optional) if omitted the server will use the default value of 0
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # List business assets
        api_response = api_instance.business_assets_get(business_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->business_assets_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List business assets
        api_response = api_instance.business_assets_get(business_id, permissions=permissions, child_asset_id=child_asset_id, asset_group_id=asset_group_id, asset_type=asset_type, start_index=start_index, bookmark=bookmark, page_size=page_size)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->business_assets_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **permissions** | [**[PermissionsWithOwner]**](PermissionsWithOwner.md)| A list of asset permissions used to filter the assets. Only assets where the requesting business has at least one of the specified permissions will be returned. | [optional]
 **child_asset_id** | **str**| A child asset unique identifier. Used to fetch asset groups that contain the asset id as a child. | [optional]
 **asset_group_id** | **str**| An asset group unique identifier. Used to fetch assets contained within the specified asset group. | [optional]
 **asset_type** | **str**| A resource type to filter the assets by. Only assets of the specified type will be returned. | [optional] if omitted the server will use the default value of "AD_ACCOUNT"
 **start_index** | **int**| An index to start fetching the results from. Only the results starting from this index will be returned. | [optional] if omitted the server will use the default value of 0
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_member_assets_get**
> bool, date, datetime, dict, float, int, list, str, none_type business_member_assets_get(business_id, member_id)

Get assets assigned to a member

Get assets on which you assigned asset permissions to the given member. Can be used to: - get all assets, regardless of asset type or - get assets of one asset type by using the asset_type query. The return response will include the permissions the member has to that asset and the asset type.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_assets_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.asset_id_permissions import AssetIdPermissions
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_access_assets_api.BusinessAccessAssetsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    member_id = "729090764583391194" # str | The member id to fetch assets for.
    asset_type = "AD_ACCOUNT" # str | A resource type to filter the assets by. Only assets of the specified type will be returned. (optional) if omitted the server will use the default value of "AD_ACCOUNT"
    start_index = 0 # int | An index to start fetching the results from. Only the results starting from this index will be returned. (optional) if omitted the server will use the default value of 0
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get assets assigned to a member
        api_response = api_instance.business_member_assets_get(business_id, member_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->business_member_assets_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get assets assigned to a member
        api_response = api_instance.business_member_assets_get(business_id, member_id, asset_type=asset_type, start_index=start_index, bookmark=bookmark, page_size=page_size)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->business_member_assets_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **member_id** | **str**| The member id to fetch assets for. |
 **asset_type** | **str**| A resource type to filter the assets by. Only assets of the specified type will be returned. | [optional] if omitted the server will use the default value of "AD_ACCOUNT"
 **start_index** | **int**| An index to start fetching the results from. Only the results starting from this index will be returned. | [optional] if omitted the server will use the default value of 0
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_members_asset_access_delete**
> DeleteMemberAccessResultsResponseArray business_members_asset_access_delete(business_id, inline_object)

Delete member access to asset

Terminate multiple members' access to an asset.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_assets_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.delete_member_access_results_response_array import DeleteMemberAccessResultsResponseArray
from openapi_generated.pinterest_client.model.inline_object import InlineObject
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_access_assets_api.BusinessAccessAssetsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    inline_object = InlineObject(
        accesses=[
            BusinessesBusinessIdMembersAssetsAccessAccesses(
                asset_id="549755885175",
                member_id="140943737684417",
            ),
        ],
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Delete member access to asset
        api_response = api_instance.business_members_asset_access_delete(business_id, inline_object)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->business_members_asset_access_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

[**DeleteMemberAccessResultsResponseArray**](DeleteMemberAccessResultsResponseArray.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_members_asset_access_update**
> UpdateMemberAssetsResultsResponseArray business_members_asset_access_update(business_id, update_member_asset_access_body)

Assign/Update member asset permissions

Grant multiple members access to assets and/or update multiple member's exisiting permissions to an asset. Note: Not all listed permissions are applicable to each asset type. For example, PROFILE_PUBLISHER would not be applicable to an asset of type AD_ACCOUNT. The permission level PROFILE_PUBLISHER is only available to an asset of the type PROFILE. 

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_assets_api
from openapi_generated.pinterest_client.model.update_member_asset_access_body import UpdateMemberAssetAccessBody
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.update_member_assets_results_response_array import UpdateMemberAssetsResultsResponseArray
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_access_assets_api.BusinessAccessAssetsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    update_member_asset_access_body = UpdateMemberAssetAccessBody(
        accesses=[
            UpdateMemberAssetAccessBodyAccesses(
                asset_id="549755885175",
                member_id="140943737684417",
                permissions=[
                    Permissions("["ANALYST","ADMIN"]"),
                ],
            ),
        ],
    ) # UpdateMemberAssetAccessBody | List of member asset permissions to create or update.

    # example passing only required values which don't have defaults set
    try:
        # Assign/Update member asset permissions
        api_response = api_instance.business_members_asset_access_update(business_id, update_member_asset_access_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->business_members_asset_access_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **update_member_asset_access_body** | [**UpdateMemberAssetAccessBody**](UpdateMemberAssetAccessBody.md)| List of member asset permissions to create or update. |

### Return type

[**UpdateMemberAssetsResultsResponseArray**](UpdateMemberAssetsResultsResponseArray.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_partner_asset_access_get**
> bool, date, datetime, dict, float, int, list, str, none_type business_partner_asset_access_get(business_id, partner_id)

Get assets assigned to a partner or assets assigned by a partner

Can be used to get the business assets your partner has granted you access to or the business assets you have granted your partner access to. If you specify: - partner_type=INTERNAL, you will retrieve your business assets that the partner has access to. - partner_type=EXTERNAL, you will retrieve the partner's business assets that the partner has granted you access to.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_assets_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.get_partner_assets_response import GetPartnerAssetsResponse
from openapi_generated.pinterest_client.model.paginated import Paginated
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_access_assets_api.BusinessAccessAssetsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    partner_id = "729090764583391194" # str | The partner id to be bound to the Business
    partner_type = None # bool, date, datetime, dict, float, int, list, str, none_type | Specifies whether to fetch internal or external (shared) partners. If partner_type=INTERNAL, the asset being queried is for accesses the partner has to your business assets.<br> If partner_type=EXTERNAL, the asset being queried is for the accesses you have to the partner's business asset. (optional)
    asset_type = "AD_ACCOUNT" # str | A resource type to filter the assets by. Only assets of the specified type will be returned. (optional) if omitted the server will use the default value of "AD_ACCOUNT"
    start_index = 0 # int | An index to start fetching the results from. Only the results starting from this index will be returned. (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get assets assigned to a partner or assets assigned by a partner
        api_response = api_instance.business_partner_asset_access_get(business_id, partner_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->business_partner_asset_access_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get assets assigned to a partner or assets assigned by a partner
        api_response = api_instance.business_partner_asset_access_get(business_id, partner_id, partner_type=partner_type, asset_type=asset_type, start_index=start_index, page_size=page_size, bookmark=bookmark)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->business_partner_asset_access_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **partner_id** | **str**| The partner id to be bound to the Business |
 **partner_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| Specifies whether to fetch internal or external (shared) partners. If partner_type&#x3D;INTERNAL, the asset being queried is for accesses the partner has to your business assets.&lt;br&gt; If partner_type&#x3D;EXTERNAL, the asset being queried is for the accesses you have to the partner&#39;s business asset. | [optional]
 **asset_type** | **str**| A resource type to filter the assets by. Only assets of the specified type will be returned. | [optional] if omitted the server will use the default value of "AD_ACCOUNT"
 **start_index** | **int**| An index to start fetching the results from. Only the results starting from this index will be returned. | [optional] if omitted the server will use the default value of 0
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/reference/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_partner_asset_access_handler_impl**
> DeletePartnerAssetsResultsResponseArray delete_partner_asset_access_handler_impl(business_id, delete_partner_asset_access_body)

Delete partner access to asset

Terminate multiple partners' access to an asset. If - partner_type=INTERNAL: You will terminate a partner's asset access to your business assets. - partner_type=EXTERNAL: You will terminate your own access to your partner's business assets.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_assets_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.delete_partner_assets_results_response_array import DeletePartnerAssetsResultsResponseArray
from openapi_generated.pinterest_client.model.delete_partner_asset_access_body import DeletePartnerAssetAccessBody
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_access_assets_api.BusinessAccessAssetsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    delete_partner_asset_access_body = DeletePartnerAssetAccessBody(
        accesses=[
            DeletePartnerAssetAccessBodyAccesses(
                partner_id="1234567890123",
                asset_id="549755885175",
                partner_type="INTERNAL",
            ),
        ],
    ) # DeletePartnerAssetAccessBody | 

    # example passing only required values which don't have defaults set
    try:
        # Delete partner access to asset
        api_response = api_instance.delete_partner_asset_access_handler_impl(business_id, delete_partner_asset_access_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->delete_partner_asset_access_handler_impl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **delete_partner_asset_access_body** | [**DeletePartnerAssetAccessBody**](DeletePartnerAssetAccessBody.md)|  |

### Return type

[**DeletePartnerAssetsResultsResponseArray**](DeletePartnerAssetsResultsResponseArray.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_partner_asset_access_handler_impl**
> UpdatePartnerAssetsResultsResponseArray update_partner_asset_access_handler_impl(business_id, update_partner_asset_access_body)

Assign/Update partner asset permissions

Grant multiple partners access to assets and/or update multiple partner's exisiting permissions to an asset. If your partner already had permissions on the asset, they will be overriden with the new permissions you assign to them. To learn more about permission levels, visit https://help.pinterest.com/en/business/article/business-manager-overview  Note: Not all listed permissions are applicable to each asset type. For example, PROFILE_PUBLISHER would not be applicable to an asset of type AD_ACCOUNT. The permission level PROFILE_PUBLISHER is only available to an asset of the type PROFILE.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_assets_api
from openapi_generated.pinterest_client.model.update_partner_asset_access_body import UpdatePartnerAssetAccessBody
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.update_partner_assets_results_response_array import UpdatePartnerAssetsResultsResponseArray
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = openapi_generated.pinterest_client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_generated.pinterest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_access_assets_api.BusinessAccessAssetsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    update_partner_asset_access_body = UpdatePartnerAssetAccessBody(
        accesses=[
            UpdatePartnerAssetAccessBodyAccesses(
                partner_id="1234567890123",
                asset_id="549755885175",
                permissions=[
                    Permissions("["ANALYST","ADMIN"]"),
                ],
            ),
        ],
    ) # UpdatePartnerAssetAccessBody | A list of assets and permissions to assign to your partners.

    # example passing only required values which don't have defaults set
    try:
        # Assign/Update partner asset permissions
        api_response = api_instance.update_partner_asset_access_handler_impl(business_id, update_partner_asset_access_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessAssetsApi->update_partner_asset_access_handler_impl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **update_partner_asset_access_body** | [**UpdatePartnerAssetAccessBody**](UpdatePartnerAssetAccessBody.md)| A list of assets and permissions to assign to your partners. |

### Return type

[**UpdatePartnerAssetsResultsResponseArray**](UpdatePartnerAssetsResultsResponseArray.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

