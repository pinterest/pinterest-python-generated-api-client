# openapi_generated.pinterest_client.BusinessAccessRelationshipsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_business_membership**](BusinessAccessRelationshipsApi.md#delete_business_membership) | **DELETE** /businesses/{business_id}/members | Terminate business memberships
[**delete_business_partners**](BusinessAccessRelationshipsApi.md#delete_business_partners) | **DELETE** /businesses/{business_id}/partners | Terminate business partnerships
[**get_business_employers**](BusinessAccessRelationshipsApi.md#get_business_employers) | **GET** /businesses/employers | List business employers for user
[**get_business_members**](BusinessAccessRelationshipsApi.md#get_business_members) | **GET** /businesses/{business_id}/members | Get business members
[**get_business_partners**](BusinessAccessRelationshipsApi.md#get_business_partners) | **GET** /businesses/{business_id}/partners | Get business partners
[**update_business_memberships**](BusinessAccessRelationshipsApi.md#update_business_memberships) | **PATCH** /businesses/{business_id}/members | Update member&#39;s business role


# **delete_business_membership**
> DeletedMembersResponse delete_business_membership(business_id, members_to_delete_body)

Terminate business memberships

Terminate memberships between the specified members and your business.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_relationships_api
from openapi_generated.pinterest_client.model.members_to_delete_body import MembersToDeleteBody
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.deleted_members_response import DeletedMembersResponse
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
    api_instance = business_access_relationships_api.BusinessAccessRelationshipsApi(api_client)
    business_id = "729090764583391194" # str | Business id
    members_to_delete_body = MembersToDeleteBody(
        members=[
            MembersToDeleteBodyMembers(
                member_id="140943737684417",
                business_role=BusinessRoleForMembers("BIZ_ADMIN"),
            ),
        ],
    ) # MembersToDeleteBody | List of members with role to delete.

    # example passing only required values which don't have defaults set
    try:
        # Terminate business memberships
        api_response = api_instance.delete_business_membership(business_id, members_to_delete_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessRelationshipsApi->delete_business_membership: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Business id |
 **members_to_delete_body** | [**MembersToDeleteBody**](MembersToDeleteBody.md)| List of members with role to delete. |

### Return type

[**DeletedMembersResponse**](DeletedMembersResponse.md)

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

# **delete_business_partners**
> DeletePartnersResponse delete_business_partners(business_id, delete_partners_request)

Terminate business partnerships

Terminate partnerships between the specified partners and your business. Note: You may only batch terminate partners of the same partner type.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_relationships_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.delete_partners_request import DeletePartnersRequest
from openapi_generated.pinterest_client.model.delete_partners_response import DeletePartnersResponse
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
    api_instance = business_access_relationships_api.BusinessAccessRelationshipsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    delete_partners_request = DeletePartnersRequest(
        partner_ids=[
            "1234567890123",
        ],
        partner_type="partner_type_example",
    ) # DeletePartnersRequest | An object containing a \"partner_ids\" property composed of a list of partner IDs and a \"partners_type\" property specifying the type of partners to delete. 

    # example passing only required values which don't have defaults set
    try:
        # Terminate business partnerships
        api_response = api_instance.delete_business_partners(business_id, delete_partners_request)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessRelationshipsApi->delete_business_partners: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **delete_partners_request** | [**DeletePartnersRequest**](DeletePartnersRequest.md)| An object containing a \&quot;partner_ids\&quot; property composed of a list of partner IDs and a \&quot;partners_type\&quot; property specifying the type of partners to delete.  |

### Return type

[**DeletePartnersResponse**](DeletePartnersResponse.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | A supplied partner id doesn&#39;t exist |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_employers**
> bool, date, datetime, dict, float, int, list, str, none_type get_business_employers()

List business employers for user

Get all of the viewing user's business employers.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_relationships_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.user_business_role_binding import UserBusinessRoleBinding
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
    api_instance = business_access_relationships_api.BusinessAccessRelationshipsApi(api_client)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List business employers for user
        api_response = api_instance.get_business_employers(page_size=page_size, bookmark=bookmark)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessRelationshipsApi->get_business_employers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_business_members**
> bool, date, datetime, dict, float, int, list, str, none_type get_business_members(business_id)

Get business members

Get all members of the specified business. The return response will include the member's business_role and assets they have access to if assets_summary=TRUE

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_relationships_api
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.member_business_role import MemberBusinessRole
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.user_business_role_binding import UserBusinessRoleBinding
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
    api_instance = business_access_relationships_api.BusinessAccessRelationshipsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    assets_summary = False # bool | Include assets summary in the response if this is true.  The assets summary returns a dictionary representing a summary of the assets for the business user ID, with information like the ad accounts and profiles the user has permissions for and what those permissions are (optional) if omitted the server will use the default value of False
    business_roles = [
        MemberBusinessRole("BIZ_ADMIN"),
    ] # [MemberBusinessRole] | A list of business roles to filter the members by. Only members whose roles are in the specified roles will be returned. (optional)
    member_ids = "00101010101,2222220101" # str | A list of business members ids separated by comma. (optional)
    start_index = 0 # int | An index to start fetching the results from. Only the results starting from this index will be returned. (optional) if omitted the server will use the default value of 0
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get business members
        api_response = api_instance.get_business_members(business_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessRelationshipsApi->get_business_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get business members
        api_response = api_instance.get_business_members(business_id, assets_summary=assets_summary, business_roles=business_roles, member_ids=member_ids, start_index=start_index, bookmark=bookmark, page_size=page_size)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessRelationshipsApi->get_business_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **assets_summary** | **bool**| Include assets summary in the response if this is true.  The assets summary returns a dictionary representing a summary of the assets for the business user ID, with information like the ad accounts and profiles the user has permissions for and what those permissions are | [optional] if omitted the server will use the default value of False
 **business_roles** | [**[MemberBusinessRole]**](MemberBusinessRole.md)| A list of business roles to filter the members by. Only members whose roles are in the specified roles will be returned. | [optional]
 **member_ids** | **str**| A list of business members ids separated by comma. | [optional]
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

# **get_business_partners**
> bool, date, datetime, dict, float, int, list, str, none_type get_business_partners(business_id)

Get business partners

Get all partners of the specified business.  If the assets_summary=TRUE and: - partner_type=INTERNAL, the business assets returned are your business assets the partner has access to. - partner_type=EXTERNAL, the business assets returned are your partner's business assets the partner has granted you   access to.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_relationships_api
from openapi_generated.pinterest_client.model.partner_type import PartnerType
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.user_business_role_binding import UserBusinessRoleBinding
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
    api_instance = business_access_relationships_api.BusinessAccessRelationshipsApi(api_client)
    business_id = "729090764583391194" # str | Unique identifier of the requesting business.
    assets_summary = False # bool | Include assets summary in the response if this is true.  The assets summary returns a dictionary representing a summary of the assets for the business user ID, with information like the ad accounts and profiles the user has permissions for and what those permissions are (optional) if omitted the server will use the default value of False
    partner_type = PartnerType("INTERNAL") # PartnerType | Specifies whether to fetch internal or external (shared) partners. If partner_type=INTERNAL, the asset being queried is for accesses the partner has to your business assets.<br> If partner_type=EXTERNAL, the asset being queried is for the accesses you have to the partner's business asset. (optional)
    partner_ids = "00101010101,2222220101" # str | A list of business partner ids separated by commas used to filter the results. Only partners with the specified ids will be returned. (optional)
    start_index = 0 # int | An index to start fetching the results from. Only the results starting from this index will be returned. (optional) if omitted the server will use the default value of 0
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/reference/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get business partners
        api_response = api_instance.get_business_partners(business_id)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessRelationshipsApi->get_business_partners: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get business partners
        api_response = api_instance.get_business_partners(business_id, assets_summary=assets_summary, partner_type=partner_type, partner_ids=partner_ids, start_index=start_index, page_size=page_size, bookmark=bookmark)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessRelationshipsApi->get_business_partners: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Unique identifier of the requesting business. |
 **assets_summary** | **bool**| Include assets summary in the response if this is true.  The assets summary returns a dictionary representing a summary of the assets for the business user ID, with information like the ad accounts and profiles the user has permissions for and what those permissions are | [optional] if omitted the server will use the default value of False
 **partner_type** | **PartnerType**| Specifies whether to fetch internal or external (shared) partners. If partner_type&#x3D;INTERNAL, the asset being queried is for accesses the partner has to your business assets.&lt;br&gt; If partner_type&#x3D;EXTERNAL, the asset being queried is for the accesses you have to the partner&#39;s business asset. | [optional]
 **partner_ids** | **str**| A list of business partner ids separated by commas used to filter the results. Only partners with the specified ids will be returned. | [optional]
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

# **update_business_memberships**
> UpdateMemberResultsResponseArray update_business_memberships(business_id, update_member_business_role_body)

Update member's business role

Update a member's business role within the business.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import openapi_generated.pinterest_client
from openapi_generated.pinterest_client.api import business_access_relationships_api
from openapi_generated.pinterest_client.model.update_member_results_response_array import UpdateMemberResultsResponseArray
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.update_member_business_role_body import UpdateMemberBusinessRoleBody
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
    api_instance = business_access_relationships_api.BusinessAccessRelationshipsApi(api_client)
    business_id = "729090764583391194" # str | Business id
    update_member_business_role_body = [
        UpdateMemberBusinessRoleBody(
            business_role=BusinessRoleForMembers("BIZ_ADMIN"),
            member_id="140943737684417",
        ),
    ] # [UpdateMemberBusinessRoleBody] | List of objects with the member id and the business_role.

    # example passing only required values which don't have defaults set
    try:
        # Update member's business role
        api_response = api_instance.update_business_memberships(business_id, update_member_business_role_body)
        pprint(api_response)
    except openapi_generated.pinterest_client.ApiException as e:
        print("Exception when calling BusinessAccessRelationshipsApi->update_business_memberships: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**| Business id |
 **update_member_business_role_body** | [**[UpdateMemberBusinessRoleBody]**](UpdateMemberBusinessRoleBody.md)| List of objects with the member id and the business_role. |

### Return type

[**UpdateMemberResultsResponseArray**](UpdateMemberResultsResponseArray.md)

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

