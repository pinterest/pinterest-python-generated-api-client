"""
    Pinterest REST API

    Pinterest's REST API  # noqa: E501

    The version of the OpenAPI document: 5.10.0
    Contact: pinterest-api@pinterest.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_generated.pinterest_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_generated.pinterest_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_generated.pinterest_client.model.audience import Audience
from openapi_generated.pinterest_client.model.audience_create_custom_request import AudienceCreateCustomRequest
from openapi_generated.pinterest_client.model.audience_create_request import AudienceCreateRequest
from openapi_generated.pinterest_client.model.audience_update_request import AudienceUpdateRequest
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.paginated import Paginated


class AudiencesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.audiences_create_endpoint = _Endpoint(
            settings={
                'response_type': (Audience,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/audiences',
                'operation_id': 'audiences_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'audience_create_request',
                ],
                'required': [
                    'ad_account_id',
                    'audience_create_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'ad_account_id',
                ]
            },
            root_map={
                'validations': {
                    ('ad_account_id',): {
                        'max_length': 18,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ad_account_id':
                        (str,),
                    'audience_create_request':
                        (AudienceCreateRequest,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'audience_create_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.audiences_create_custom_endpoint = _Endpoint(
            settings={
                'response_type': (Audience,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/audiences/custom',
                'operation_id': 'audiences_create_custom',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'audience_create_custom_request',
                ],
                'required': [
                    'ad_account_id',
                    'audience_create_custom_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'ad_account_id',
                ]
            },
            root_map={
                'validations': {
                    ('ad_account_id',): {
                        'max_length': 18,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ad_account_id':
                        (str,),
                    'audience_create_custom_request':
                        (AudienceCreateCustomRequest,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'audience_create_custom_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.audiences_get_endpoint = _Endpoint(
            settings={
                'response_type': (Audience,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/audiences/{audience_id}',
                'operation_id': 'audiences_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'audience_id',
                ],
                'required': [
                    'ad_account_id',
                    'audience_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'ad_account_id',
                    'audience_id',
                ]
            },
            root_map={
                'validations': {
                    ('ad_account_id',): {
                        'max_length': 18,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                    ('audience_id',): {
                        'max_length': 18,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ad_account_id':
                        (str,),
                    'audience_id':
                        (str,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                    'audience_id': 'audience_id',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'audience_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.audiences_list_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/audiences',
                'operation_id': 'audiences_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'bookmark',
                    'order',
                    'page_size',
                ],
                'required': [
                    'ad_account_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'order',
                ],
                'validation': [
                    'ad_account_id',
                    'page_size',
                ]
            },
            root_map={
                'validations': {
                    ('ad_account_id',): {
                        'max_length': 18,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                    ('page_size',): {

                        'inclusive_maximum': 250,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('order',): {

                        "ASCENDING": "ASCENDING",
                        "DESCENDING": "DESCENDING"
                    },
                },
                'openapi_types': {
                    'ad_account_id':
                        (str,),
                    'bookmark':
                        (str,),
                    'order':
                        (str,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                    'bookmark': 'bookmark',
                    'order': 'order',
                    'page_size': 'page_size',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'bookmark': 'query',
                    'order': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.audiences_update_endpoint = _Endpoint(
            settings={
                'response_type': (Audience,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/audiences/{audience_id}',
                'operation_id': 'audiences_update',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'audience_id',
                    'audience_update_request',
                ],
                'required': [
                    'ad_account_id',
                    'audience_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'ad_account_id',
                    'audience_id',
                ]
            },
            root_map={
                'validations': {
                    ('ad_account_id',): {
                        'max_length': 18,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                    ('audience_id',): {
                        'max_length': 18,
                        'regex': {
                            'pattern': r'^\d+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ad_account_id':
                        (str,),
                    'audience_id':
                        (str,),
                    'audience_update_request':
                        (AudienceUpdateRequest,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                    'audience_id': 'audience_id',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'audience_id': 'path',
                    'audience_update_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def audiences_create(
        self,
        ad_account_id,
        audience_create_request,
        **kwargs
    ):
        """Create audience  # noqa: E501

        Create an audience you can use in targeting for specific ad groups. Targeting combines customer information with the ways users interact with Pinterest to help you reach specific groups of users; you can include or exclude specific audience_ids when you create an ad group. <p/> For more, see <a class=\"reference external\" href=\"https://help.pinterest.com/en/business/article/audience-targeting\" target=\"_blank\">Audience targeting</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.audiences_create(ad_account_id, audience_create_request, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            audience_create_request (AudienceCreateRequest): List of ads to create, size limit [1, 30]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Audience
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ad_account_id'] = \
            ad_account_id
        kwargs['audience_create_request'] = \
            audience_create_request
        return self.audiences_create_endpoint.call_with_http_info(**kwargs)

    def audiences_create_custom(
        self,
        ad_account_id,
        audience_create_custom_request,
        **kwargs
    ):
        """Create custom audience  # noqa: E501

        Create a custom audience and find the audiences you want your ads to reach.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.audiences_create_custom(ad_account_id, audience_create_custom_request, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            audience_create_custom_request (AudienceCreateCustomRequest): Custom audience to create.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Audience
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ad_account_id'] = \
            ad_account_id
        kwargs['audience_create_custom_request'] = \
            audience_create_custom_request
        return self.audiences_create_custom_endpoint.call_with_http_info(**kwargs)

    def audiences_get(
        self,
        ad_account_id,
        audience_id,
        **kwargs
    ):
        """Get audience  # noqa: E501

        Get a specific audience given the audience ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.audiences_get(ad_account_id, audience_id, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            audience_id (str): Unique identifier of an audience

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Audience
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ad_account_id'] = \
            ad_account_id
        kwargs['audience_id'] = \
            audience_id
        return self.audiences_get_endpoint.call_with_http_info(**kwargs)

    def audiences_list(
        self,
        ad_account_id,
        **kwargs
    ):
        """List audiences  # noqa: E501

        Get list of audiences for the ad account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.audiences_list(ad_account_id, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.

        Keyword Args:
            bookmark (str): Cursor used to fetch the next page of items. [optional]
            order (str): The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items.. [optional]
            page_size (int): Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/getting-started/pagination/'>Pagination</a> for more information.. [optional] if omitted the server will use the default value of 25
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ad_account_id'] = \
            ad_account_id
        return self.audiences_list_endpoint.call_with_http_info(**kwargs)

    def audiences_update(
        self,
        ad_account_id,
        audience_id,
        **kwargs
    ):
        """Update audience  # noqa: E501

        Update (edit or remove) an existing targeting audience.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.audiences_update(ad_account_id, audience_id, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            audience_id (str): Unique identifier of an audience

        Keyword Args:
            audience_update_request (AudienceUpdateRequest): The audience to be updated.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Audience
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ad_account_id'] = \
            ad_account_id
        kwargs['audience_id'] = \
            audience_id
        return self.audiences_update_endpoint.call_with_http_info(**kwargs)

