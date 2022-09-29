# pinterest.generated.client.BoardsApi

All URIs are relative to *https://api.pinterest.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**board_sections_create**](BoardsApi.md#board_sections_create) | **POST** /boards/{board_id}/sections | Create board section
[**board_sections_delete**](BoardsApi.md#board_sections_delete) | **DELETE** /boards/{board_id}/sections/{section_id} | Delete board section
[**board_sections_list**](BoardsApi.md#board_sections_list) | **GET** /boards/{board_id}/sections | List board sections
[**board_sections_list_pins**](BoardsApi.md#board_sections_list_pins) | **GET** /boards/{board_id}/sections/{section_id}/pins | List Pins on board section
[**board_sections_update**](BoardsApi.md#board_sections_update) | **PATCH** /boards/{board_id}/sections/{section_id} | Update board section
[**boards_create**](BoardsApi.md#boards_create) | **POST** /boards | Create board
[**boards_delete**](BoardsApi.md#boards_delete) | **DELETE** /boards/{board_id} | Delete board
[**boards_get**](BoardsApi.md#boards_get) | **GET** /boards/{board_id} | Get board
[**boards_list**](BoardsApi.md#boards_list) | **GET** /boards | List boards
[**boards_list_pins**](BoardsApi.md#boards_list_pins) | **GET** /boards/{board_id}/pins | List Pins on board
[**boards_update**](BoardsApi.md#boards_update) | **PATCH** /boards/{board_id} | Update board


# **board_sections_create**
> BoardSection board_sections_create(board_id, board_section)

Create board section

Create a board section on a board owned by the \"operation user_account\" - or on a group board that has been shared with this account. - By default, the \"operation user_account\" is the token user_account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import boards_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.board_section import BoardSection
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boards_api.BoardsApi(api_client)
    board_id = "4" # str | Unique identifier of a board.
    board_section = BoardSection(
        name="Salads",
    ) # BoardSection | Create a board section.

    # example passing only required values which don't have defaults set
    try:
        # Create board section
        api_response = api_instance.board_sections_create(board_id, board_section)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->board_sections_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**| Unique identifier of a board. |
 **board_section** | [**BoardSection**](BoardSection.md)| Create a board section. |

### Return type

[**BoardSection**](BoardSection.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | response |  -  |
**400** | Invalid board section parameters. |  -  |
**403** | Not authorized to create board sections. |  -  |
**409** | Could not get exclusive access to the board to create a new section. |  -  |
**500** | Could not create a new board section. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **board_sections_delete**
> board_sections_delete(board_id, section_id)

Delete board section

Delete a board section on a board owned by the \"operation user_account\" - or on a group board that has been shared with this account. - By default, the \"operation user_account\" is the token user_account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import boards_api
from pinterest.generated.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boards_api.BoardsApi(api_client)
    board_id = "4" # str | Unique identifier of a board.
    section_id = "4" # str | Unique identifier of a board section.

    # example passing only required values which don't have defaults set
    try:
        # Delete board section
        api_instance.board_sections_delete(board_id, section_id)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->board_sections_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**| Unique identifier of a board. |
 **section_id** | **str**| Unique identifier of a board section. |

### Return type

void (empty response body)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Board section deleted successfully |  -  |
**403** | Not authorized to delete board section. |  -  |
**404** | Board section not found. |  -  |
**409** | Board section conflict. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **board_sections_list**
> bool, date, datetime, dict, float, int, list, str, none_type board_sections_list(board_id)

List board sections

Get a list of all board sections from a board owned by the \"operation user_account\" - or a group board that has been shared with this account. - By default, the \"operation user_account\" is the token user_account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import boards_api
from pinterest.generated.client.model.paginated import Paginated
from pinterest.generated.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boards_api.BoardsApi(api_client)
    board_id = "4" # str | Unique identifier of a board.
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/getting-started/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # List board sections
        api_response = api_instance.board_sections_list(board_id)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->board_sections_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List board sections
        api_response = api_instance.board_sections_list(board_id, bookmark=bookmark, page_size=page_size)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->board_sections_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**| Unique identifier of a board. |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/getting-started/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25

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
**200** | response |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **board_sections_list_pins**
> bool, date, datetime, dict, float, int, list, str, none_type board_sections_list_pins(board_id, section_id)

List Pins on board section

Get a list of the Pins on a board section of a board owned by the \"operation user_account\" - or on a group board that has been shared with this account. - By default, the \"operation user_account\" is the token user_account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import boards_api
from pinterest.generated.client.model.paginated import Paginated
from pinterest.generated.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boards_api.BoardsApi(api_client)
    board_id = "4" # str | Unique identifier of a board.
    section_id = "4" # str | Unique identifier of a board section.
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/getting-started/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # List Pins on board section
        api_response = api_instance.board_sections_list_pins(board_id, section_id)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->board_sections_list_pins: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Pins on board section
        api_response = api_instance.board_sections_list_pins(board_id, section_id, bookmark=bookmark, page_size=page_size)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->board_sections_list_pins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**| Unique identifier of a board. |
 **section_id** | **str**| Unique identifier of a board section. |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/getting-started/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25

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
**200** | response |  -  |
**403** | Not authorized to access Pins on board section. |  -  |
**404** | Board or section not found. |  -  |
**409** | Board section conflict. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **board_sections_update**
> BoardSection board_sections_update(board_id, section_id, board_section)

Update board section

Update a board section on a board owned by the \"operation user_account\" - or on a group board that has been shared with this account. - By default, the \"operation user_account\" is the token user_account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import boards_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.board_section import BoardSection
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boards_api.BoardsApi(api_client)
    board_id = "4" # str | Unique identifier of a board.
    section_id = "4" # str | Unique identifier of a board section.
    board_section = BoardSection(
        name="Salads",
    ) # BoardSection | Update a board section.

    # example passing only required values which don't have defaults set
    try:
        # Update board section
        api_response = api_instance.board_sections_update(board_id, section_id, board_section)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->board_sections_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**| Unique identifier of a board. |
 **section_id** | **str**| Unique identifier of a board section. |
 **board_section** | [**BoardSection**](BoardSection.md)| Update a board section. |

### Return type

[**BoardSection**](BoardSection.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |
**400** | Invalid board section parameters. |  -  |
**403** | Not authorized to update board section. |  -  |
**409** | Board section conflict. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_create**
> Board boards_create(board)

Create board

Create a board owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import boards_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.board import Board
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boards_api.BoardsApi(api_client)
    board = Board(
        name="Summer Recipes",
        description="My favorite summer recipes",
        privacy="PUBLIC",
    ) # Board | Create a board using a single board json object.

    # example passing only required values which don't have defaults set
    try:
        # Create board
        api_response = api_instance.boards_create(board)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->boards_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board** | [**Board**](Board.md)| Create a board using a single board json object. |

### Return type

[**Board**](Board.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | response |  -  |
**400** | The board name is invalid or duplicated. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_delete**
> boards_delete(board_id)

Delete board

Delete a board owned by the \"operation user_account\". - By default, the \"operation user_account\" is the token user_account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import boards_api
from pinterest.generated.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boards_api.BoardsApi(api_client)
    board_id = "4" # str | Unique identifier of a board.

    # example passing only required values which don't have defaults set
    try:
        # Delete board
        api_instance.boards_delete(board_id)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->boards_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**| Unique identifier of a board. |

### Return type

void (empty response body)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Board deleted successfully |  -  |
**403** | Not authorized to delete the board. |  -  |
**404** | Board not found. |  -  |
**409** | Could not get exclusive access to delete the board. |  -  |
**429** | This request exceeded a rate limit. This can happen if the client exceeds one of the published rate limits or if multiple write operations are applied to an object within a short time window. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_get**
> Board boards_get(board_id)

Get board

Get a board owned by the operation user_account - or a group board that has been shared with this account. - By default, the \"operation user_account\" is the token user_account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import boards_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.board import Board
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boards_api.BoardsApi(api_client)
    board_id = "4" # str | Unique identifier of a board.

    # example passing only required values which don't have defaults set
    try:
        # Get board
        api_response = api_instance.boards_get(board_id)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->boards_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**| Unique identifier of a board. |

### Return type

[**Board**](Board.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |
**404** | Board not found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_list**
> bool, date, datetime, dict, float, int, list, str, none_type boards_list()

List boards

Get a list of the boards owned by the \"operation user_account\" + group boards where this account is a collaborator  Optional: Specify a privacy type (public, protected, or secret) to indicate which boards to return. - If no privacy is specified, all boards that can be returned (based on the scopes of the token and ad_account role if applicable) will be returned.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import boards_api
from pinterest.generated.client.model.paginated import Paginated
from pinterest.generated.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boards_api.BoardsApi(api_client)
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/getting-started/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25
    privacy = "PUBLIC" # str | Privacy setting for a board. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List boards
        api_response = api_instance.boards_list(bookmark=bookmark, page_size=page_size, privacy=privacy)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->boards_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/getting-started/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25
 **privacy** | **str**| Privacy setting for a board. | [optional]

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
**200** | response |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_list_pins**
> bool, date, datetime, dict, float, int, list, str, none_type boards_list_pins(board_id)

List Pins on board

Get a list of the Pins on a board owned by the \"operation user_account\" - or on a group board that has been shared with this account. - By default, the \"operation user_account\" is the token user_account.

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import boards_api
from pinterest.generated.client.model.paginated import Paginated
from pinterest.generated.client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boards_api.BoardsApi(api_client)
    board_id = "4" # str | Unique identifier of a board.
    bookmark = "bookmark_example" # str | Cursor used to fetch the next page of items (optional)
    page_size = 25 # int | Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/getting-started/pagination/'>Pagination</a> for more information. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # List Pins on board
        api_response = api_instance.boards_list_pins(board_id)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->boards_list_pins: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Pins on board
        api_response = api_instance.boards_list_pins(board_id, bookmark=bookmark, page_size=page_size)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->boards_list_pins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**| Unique identifier of a board. |
 **bookmark** | **str**| Cursor used to fetch the next page of items | [optional]
 **page_size** | **int**| Maximum number of items to include in a single page of the response. See documentation on &lt;a href&#x3D;&#39;/docs/getting-started/pagination/&#39;&gt;Pagination&lt;/a&gt; for more information. | [optional] if omitted the server will use the default value of 25

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
**200** | response |  -  |
**404** | Board not found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_update**
> Board boards_update(board_id, board_update)

Update board

Update a board owned by the \"operating user_account\".

### Example

* OAuth Authentication (pinterest_oauth2):

```python
import time
import pinterest.generated.client
from pinterest.generated.client.api import boards_api
from pinterest.generated.client.model.error import Error
from pinterest.generated.client.model.board_update import BoardUpdate
from pinterest.generated.client.model.board import Board
from pprint import pprint
# Defining the host is optional and defaults to https://api.pinterest.com/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: pinterest_oauth2
configuration = pinterest.generated.client.Configuration(
    host = "https://api.pinterest.com/v5"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pinterest.generated.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = boards_api.BoardsApi(api_client)
    board_id = "4" # str | Unique identifier of a board.
    board_update = BoardUpdate(
        name="Summer Recipes",
        description="My favorite summer recipes",
        privacy="PUBLIC",
    ) # BoardUpdate | Update a board.

    # example passing only required values which don't have defaults set
    try:
        # Update board
        api_response = api_instance.boards_update(board_id, board_update)
        pprint(api_response)
    except pinterest.generated.client.ApiException as e:
        print("Exception when calling BoardsApi->boards_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**| Unique identifier of a board. |
 **board_update** | [**BoardUpdate**](BoardUpdate.md)| Update a board. |

### Return type

[**Board**](Board.md)

### Authorization

[pinterest_oauth2](../README.md#pinterest_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |
**400** | Invalid board parameters. |  -  |
**403** | Not authorized to update the board. |  -  |
**429** | This request exceeded a rate limit. This can happen if the client exceeds one of the published rate limits or if multiple write operations are applied to an object within a short time window. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

