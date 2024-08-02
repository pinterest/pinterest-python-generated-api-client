# openapi_generated.pinterest_client.BusinessAccessInviteApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_access_requests_create**](BusinessAccessInviteApi.md#asset_access_requests_create) | **POST** /businesses/{business_id}/requests/assets/access | Create a request to access an existing partner&#39;s assets.
[**cancel_invites_or_requests**](BusinessAccessInviteApi.md#cancel_invites_or_requests) | **DELETE** /businesses/{business_id}/invites | Cancel invites/requests
[**create_asset_invites**](BusinessAccessInviteApi.md#create_asset_invites) | **POST** /businesses/{business_id}/invites/assets/access | Update invite/request with an asset permission
[**create_membership_or_partnership_invites**](BusinessAccessInviteApi.md#create_membership_or_partnership_invites) | **POST** /businesses/{business_id}/invites | Create invites or requests
[**get_invites**](BusinessAccessInviteApi.md#get_invites) | **GET** /businesses/{business_id}/invites | Get invites/requests
[**respond_business_access_invites**](BusinessAccessInviteApi.md#respond_business_access_invites) | **PATCH** /businesses/invites | Accept or decline an invite/request


# **asset_access_requests_create**
> CreateAssetAccessRequestResponse asset_access_requests_create(business_id, create_asset_access_request_body)

Create a request to access an existing partner's assets.

Create a request to access an existing partner's assets with the specified permissions. The request will be sent to the partner for approval. The assets that can be requested are ad accounts and profiles.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_invite_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.create_asset_access_request_response import CreateAssetAccessRequestResponse
from openapi_generated.pinterest_client.model.create_asset_access_request_body import CreateAssetAccessRequestBody
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
    api_instance = business_access_invite_api.BusinessAccessInviteApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    create_asset_access_request_body = CreateAssetAccessRequestBody(
        asset_requests=[
            CreateAssetAccessRequestBodyAssetRequests(
                partner_id="809944451643622187",
                asset_id_to_permissions=AssetIdToPermissions(
                    key=[
                        Permissions("ADMIN"),
                    ],
                ),
            ),
        ],
    ) # CreateAssetAccessRequestBody | 

    # example passing only required values which don't have defaults set
    try:
        # Create a request to access an existing partner's assets.
        api_response = api_instance.asset_access_requests_create(business_id, create_asset_access_request_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessInviteApi->asset_access_requests_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **create_asset_access_request_body** | [**CreateAssetAccessRequestBody**](CreateAssetAccessRequestBody.md)|  |

### Return type

[**CreateAssetAccessRequestResponse**](CreateAssetAccessRequestResponse.md)

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

# **cancel_invites_or_requests**
> DeleteInvitesResultsResponseArray cancel_invites_or_requests(business_id, cancel_invites_body)

Cancel invites/requests

Cancel membership/partnership invites and/or requests.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_invite_api
from openapi_generated.pinterest_client.model.cancel_invites_body import CancelInvitesBody
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.delete_invites_results_response_array import DeleteInvitesResultsResponseArray
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
    api_instance = business_access_invite_api.BusinessAccessInviteApi(api_client)
    business_id = "729090764583391194" # str | Business id
    cancel_invites_body = CancelInvitesBody(
        invite_ids=["1234567890123456789","1122334455667788991"],
    ) # CancelInvitesBody | A list with invite ids

    # example passing only required values which don't have defaults set
    try:
        # Cancel invites/requests
        api_response = api_instance.cancel_invites_or_requests(business_id, cancel_invites_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessInviteApi->cancel_invites_or_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Business id |
 **cancel_invites_body** | [**CancelInvitesBody**](CancelInvitesBody.md)| A list with invite ids |

### Return type

[**DeleteInvitesResultsResponseArray**](DeleteInvitesResultsResponseArray.md)

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

# **create_asset_invites**
> UpdateInvitesResultsResponseArray create_asset_invites(business_id, create_asset_invites_request)

Update invite/request with an asset permission

Assign asset permissions information to an existing invite/request. Can be used to: - Request access to a partner's asset. Note: This is only for when no existing partnership exists. If an existing   partnership exists, use \"Create a request to access an existing partner's assets\" to request access to your   partner's assets.     - invite_type=\"PARTNER_REQUEST\" - Invite a partner to access your business assets. Note: This is only for when there is no existing partnership.   If there is an existing partnership, use \"Assign/Update partner asset permissions\" to assign a partner access to   new assets.     - invite_type=\"PARTNER_INVITE\" - Invite a member to access your business assets. Note: This is only for when there is no existing membership.   If there is an existing membership, use \"Assign/Update member asset permissions\" to assign a member access to new   assets.     - invite_type=\"MEMBER_INVITE\"  To learn more about permission levels, visit https://help.pinterest.com/en/business/article/business-manager-overview.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_invite_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.update_invites_results_response_array import UpdateInvitesResultsResponseArray
from openapi_generated.pinterest_client.model.create_asset_invites_request import CreateAssetInvitesRequest
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
    api_instance = business_access_invite_api.BusinessAccessInviteApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    create_asset_invites_request = CreateAssetInvitesRequest(
        invites=[
            CreateAssetInvitesRequestItem(
                invite_id="1234567890123",
                invite_type=InviteType("MEMBER_INVITE"),
                asset_id_to_permissions=AssetIdToPermissions(
                    key=[
                        Permissions("ADMIN"),
                    ],
                ),
            ),
        ],
    ) # CreateAssetInvitesRequest | A list of invites/requests together with the asset permissions to be assigned to the invite/request. 

    # example passing only required values which don't have defaults set
    try:
        # Update invite/request with an asset permission
        api_response = api_instance.create_asset_invites(business_id, create_asset_invites_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessInviteApi->create_asset_invites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **create_asset_invites_request** | [**CreateAssetInvitesRequest**](CreateAssetInvitesRequest.md)| A list of invites/requests together with the asset permissions to be assigned to the invite/request.  |

### Return type

[**UpdateInvitesResultsResponseArray**](UpdateInvitesResultsResponseArray.md)

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

# **create_membership_or_partnership_invites**
> CreateInvitesResultsResponseArray create_membership_or_partnership_invites(business_id, create_membership_or_partnership_invites_body)

Create invites or requests

Create batch invites or requests. Can create batch invites or requests as described below. - Invite members to join the business. This would required specifying the following:     - invite_type=\"MEMBER_INVITE\"     - business_role=\"EMPLOYEE\" OR business_role=\"BIZ_ADMIN\" (To learn more about business roles, visit     https://help.pinterest.com/en/business/article/profile-permissions-in-business-access.)     - members - Invite partners to access your business assets. This would require specifying the following:     - invite_type=\"PARTNER_INVITE\"     - business_role=\"PARTNER\"     - partners - Request to be a partner so you can access their assets. This would require specifying the following:     - invite_type=\"PARTNER_REQUEST\"     - business_role=\"PARTNER\"     - partners

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_invite_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.create_membership_or_partnership_invites_body import CreateMembershipOrPartnershipInvitesBody
from openapi_generated.pinterest_client.model.create_invites_results_response_array import CreateInvitesResultsResponseArray
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
    api_instance = business_access_invite_api.BusinessAccessInviteApi(api_client)
    business_id = "729090764583391194" # str | Business id
    create_membership_or_partnership_invites_body = CreateMembershipOrPartnershipInvitesBody(
        business_role="BIZ_ADMIN",
        invite_type=InviteType("MEMBER_INVITE"),
        members=["business0101","user@business.com"],
        partners=["809944451643622187","766456567741825556"],
    ) # CreateMembershipOrPartnershipInvitesBody | An object with the properties: invite_type, partners, members, business_role

    # example passing only required values which don't have defaults set
    try:
        # Create invites or requests
        api_response = api_instance.create_membership_or_partnership_invites(business_id, create_membership_or_partnership_invites_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessInviteApi->create_membership_or_partnership_invites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Business id |
 **create_membership_or_partnership_invites_body** | [**CreateMembershipOrPartnershipInvitesBody**](CreateMembershipOrPartnershipInvitesBody.md)| An object with the properties: invite_type, partners, members, business_role |

### Return type

[**CreateInvitesResultsResponseArray**](CreateInvitesResultsResponseArray.md)

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

# **get_invites**
> bool, date, datetime, dict, float, int, list, str, none_type get_invites(business_id)

Get invites/requests

Get the membership/partnership invites and/or requests for the authorized user.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_invite_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.invite_type import InviteType
from openapi_generated.pinterest_client.model.invite_response import InviteResponse
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
    api_instance = business_access_invite_api.BusinessAccessInviteApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    is_member = True # bool | A boolean field to indicate whether the invite is to create a partnership or a membership. (optional) if omitted the server will use the default value of True
    invite_status = [
        "PENDING",
    ] # [str] | A list of invite statuses to filter invites by. Only invites whose status is in the provided statuses will be returned. (optional)
    invite_type = InviteType("MEMBER_INVITE") # InviteType | Invite type to filter invites by. Only invites of the specified type will be returned. (optional)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get invites/requests
        api_response = api_instance.get_invites(business_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessInviteApi->get_invites: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get invites/requests
        api_response = api_instance.get_invites(business_id, is_member=is_member, invite_status=invite_status, invite_type=invite_type, bookmark=bookmark, page_size=page_size)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessInviteApi->get_invites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **is_member** | **bool**| A boolean field to indicate whether the invite is to create a partnership or a membership. | [optional] if omitted the server will use the default value of True
 **invite_status** | **[str]**| A list of invite statuses to filter invites by. Only invites whose status is in the provided statuses will be returned. | [optional]
 **invite_type** | **InviteType**| Invite type to filter invites by. Only invites of the specified type will be returned. | [optional]
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

# **respond_business_access_invites**
> RespondToInvitesResponseArray respond_business_access_invites(auth_respond_invites_body)

Accept or decline an invite/request

Accept or decline invites or requests.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_invite_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.auth_respond_invites_body import AuthRespondInvitesBody
from openapi_generated.pinterest_client.model.respond_to_invites_response_array import RespondToInvitesResponseArray
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
    api_instance = business_access_invite_api.BusinessAccessInviteApi(api_client)
    auth_respond_invites_body = AuthRespondInvitesBody(
        invites=[
            AuthRespondInvitesBodyInvites(
                action=AuthRespondInvitesBodyAction(
                    accept_invite=True,
                    asset_id_to_permissions=AssetIdToPermissions(
                        key=[
                            Permissions("ADMIN"),
                        ],
                    ),
                ),
                invite_id="4",
            ),
        ],
    ) # AuthRespondInvitesBody | 

    # example passing only required values which don't have defaults set
    try:
        # Accept or decline an invite/request
        api_response = api_instance.respond_business_access_invites(auth_respond_invites_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessInviteApi->respond_business_access_invites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_respond_invites_body** | [**AuthRespondInvitesBody**](AuthRespondInvitesBody.md)|  |

### Return type

[**RespondToInvitesResponseArray**](RespondToInvitesResponseArray.md)

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

