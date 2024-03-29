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
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.lead_form_response import LeadFormResponse
from openapi_generated.pinterest_client.model.paginated import Paginated


class LeadFormsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.lead_form_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadFormResponse,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/lead_forms/{lead_form_id}',
                'operation_id': 'lead_form_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'lead_form_id',
                ],
                'required': [
                    'ad_account_id',
                    'lead_form_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'ad_account_id',
                    'lead_form_id',
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
                    ('lead_form_id',): {

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
                    'lead_form_id':
                        (str,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                    'lead_form_id': 'lead_form_id',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'lead_form_id': 'path',
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
        self.lead_forms_list_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'pinterest_oauth2'
                ],
                'endpoint_path': '/ad_accounts/{ad_account_id}/lead_forms',
                'operation_id': 'lead_forms_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ad_account_id',
                    'page_size',
                    'order',
                    'bookmark',
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
                    'page_size':
                        (int,),
                    'order':
                        (str,),
                    'bookmark':
                        (str,),
                },
                'attribute_map': {
                    'ad_account_id': 'ad_account_id',
                    'page_size': 'page_size',
                    'order': 'order',
                    'bookmark': 'bookmark',
                },
                'location_map': {
                    'ad_account_id': 'path',
                    'page_size': 'query',
                    'order': 'query',
                    'bookmark': 'query',
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

    def lead_form_get(
        self,
        ad_account_id,
        lead_form_id,
        **kwargs
    ):
        """Get lead form by id  # noqa: E501

        Gets a lead form given it's ID. It must also be associated with the provided ad account ID. Retrieving an advertiser's lead form will only contain results if you're a part of the Lead ads beta. If you're interested in joining the beta, please reach out to your Pinterest account manager.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lead_form_get(ad_account_id, lead_form_id, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            lead_form_id (str): Unique identifier of a lead form.

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
            LeadFormResponse
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
        kwargs['lead_form_id'] = \
            lead_form_id
        return self.lead_form_get_endpoint.call_with_http_info(**kwargs)

    def lead_forms_list(
        self,
        ad_account_id,
        **kwargs
    ):
        """Get lead forms  # noqa: E501

        Gets all Lead Forms associated with an ad account ID. Retrieving an advertiser's list of lead forms will only contain results if you're a part of the Lead ads beta.  If you're interested in joining the beta, please reach out to your Pinterest account manager.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lead_forms_list(ad_account_id, async_req=True)
        >>> result = thread.get()

        Args:
            ad_account_id (str): Unique identifier of an ad account.

        Keyword Args:
            page_size (int): Maximum number of items to include in a single page of the response. See documentation on <a href='/docs/getting-started/pagination/'>Pagination</a> for more information.. [optional] if omitted the server will use the default value of 25
            order (str): The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items.. [optional]
            bookmark (str): Cursor used to fetch the next page of items. [optional]
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
        return self.lead_forms_list_endpoint.call_with_http_info(**kwargs)

