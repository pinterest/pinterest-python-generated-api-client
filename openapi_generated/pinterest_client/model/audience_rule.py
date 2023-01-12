"""
    Pinterest REST API

    Pinterest's REST API  # noqa: E501

    The version of the OpenAPI document: 5.7.0
    Contact: pinterest-api@pinterest.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_generated.pinterest_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from openapi_generated.pinterest_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_generated.pinterest_client.model.objective_type import ObjectiveType
    from openapi_generated.pinterest_client.model.pinterest_tag_event_data import PinterestTagEventData
    globals()['ObjectiveType'] = ObjectiveType
    globals()['PinterestTagEventData'] = PinterestTagEventData


class AudienceRule(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('customer_list_id',): {
            'regex': {
                'pattern': r'^\d+$',  # noqa: E501
            },
        },
        ('visitor_source_id',): {
            'regex': {
                'pattern': r'^\d+$',  # noqa: E501
            },
        },
        ('ad_account_id',): {
            'regex': {
                'pattern': r'^\d+$',  # noqa: E501
            },
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'country': (str,),  # noqa: E501
            'customer_list_id': (str,),  # noqa: E501
            'engagement_domain': ([str],),  # noqa: E501
            'engagement_type': (str,),  # noqa: E501
            'event': (str,),  # noqa: E501
            'event_data': (PinterestTagEventData,),  # noqa: E501
            'percentage': (int,),  # noqa: E501
            'pin_id': ([str],),  # noqa: E501
            'prefill': (bool,),  # noqa: E501
            'retention_days': (int,),  # noqa: E501
            'seed_id': ([str],),  # noqa: E501
            'url': ([str],),  # noqa: E501
            'visitor_source_id': (str,),  # noqa: E501
            'event_source': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'ingestion_source': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'engager_type': (int,),  # noqa: E501
            'campaign_id': ([str],),  # noqa: E501
            'ad_id': ([str],),  # noqa: E501
            'objective_type': ([ObjectiveType],),  # noqa: E501
            'ad_account_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'country': 'country',  # noqa: E501
        'customer_list_id': 'customer_list_id',  # noqa: E501
        'engagement_domain': 'engagement_domain',  # noqa: E501
        'engagement_type': 'engagement_type',  # noqa: E501
        'event': 'event',  # noqa: E501
        'event_data': 'event_data',  # noqa: E501
        'percentage': 'percentage',  # noqa: E501
        'pin_id': 'pin_id',  # noqa: E501
        'prefill': 'prefill',  # noqa: E501
        'retention_days': 'retention_days',  # noqa: E501
        'seed_id': 'seed_id',  # noqa: E501
        'url': 'url',  # noqa: E501
        'visitor_source_id': 'visitor_source_id',  # noqa: E501
        'event_source': 'event_source',  # noqa: E501
        'ingestion_source': 'ingestion_source',  # noqa: E501
        'engager_type': 'engager_type',  # noqa: E501
        'campaign_id': 'campaign_id',  # noqa: E501
        'ad_id': 'ad_id',  # noqa: E501
        'objective_type': 'objective_type',  # noqa: E501
        'ad_account_id': 'ad_account_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AudienceRule - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            country (str): Valid countries include: \"US\", \"CA\", and \"GB\".. [optional]  # noqa: E501
            customer_list_id (str): Customer list ID. For CUSTOMER_LIST `audience_type`.. [optional]  # noqa: E501
            engagement_domain ([str]): The audience account's verified domain. **Required** for ENGAGEMENT `audience_type`.. [optional]  # noqa: E501
            engagement_type (str): Engagement type enum. Optional for ENGAGEMENT `audience_type`. Supported values are `click`, `save`, `closeup`, `comment` and `like`. All engagements are included if this field is not set. . [optional]  # noqa: E501
            event (str): A Pinterest tag event. Optional for VISITOR `audience_type`. Possible values are `pagevisit`, `signup`, `checkout`, `viewcategory`, `search`, `addtocart`, `watchvideo`, `lead`, and `custom`. This field also accepts a partner-defined Pinterest tag event.. [optional]  # noqa: E501
            event_data (PinterestTagEventData): [optional]  # noqa: E501
            percentage (int): Percentage should be 1-10. The targeted audience should be this % size across Pinterest.. [optional]  # noqa: E501
            pin_id ([str]): IDs of engaged organic pins. Optional for ENGAGEMENT `audience_type`. For example, \"pin_id:\": [\"34567\"]. [optional]  # noqa: E501
            prefill (bool): Optional for VISITOR `audience_type`. If `true`, the specified rule on existing engagement data is applied to pre-populate the audience. If `false`, the audience is empty at creation time. The default is `true`.. [optional]  # noqa: E501
            retention_days (int): Number of days a Pinterest user remains in the audience. Optional for ENGAGEMENT and VISITOR `audience_type`. Accepted range is 1-540. Defaults to 180 if not specified.. [optional]  # noqa: E501
            seed_id ([str]): Audience ID(s). For ACTALIKE `audience_type`. . [optional]  # noqa: E501
            url ([str]): Optional for ENGAGEMENT or VISITOR `audience_type`. For ENGAGEMENT, it is the engaged pin's URL. For VISITOR, you can use it as a string or a {operator: value} object for filtering visitors based on conversion tag event URLs. Supported operators are [ =, !=, contains, not_contains].<br>Example 1:  \"url\": \"http://www.myonlinestore123.com/view_item/shoe\"<br>Example 2: \"url\": {\"contains\": \"/view_item/shoe\"}. [optional]  # noqa: E501
            visitor_source_id (str): The conversion tag ID, or the Pinterest tag ID, that you use on your website. For VISITOR `audience_type`.. [optional]  # noqa: E501
            event_source ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Optional for VISITOR. You can use it as a {'=': [value]}. Supported values are: web, mobile, offline. [optional]  # noqa: E501
            ingestion_source ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Optional for VISITOR. You can use it as a {'=': [value]}. Supported values are: tag, mmp, file_upload, conversions_api. [optional]  # noqa: E501
            engager_type (int): Optional for ENGAGEMENT. Engager type value should be 1-2.. [optional]  # noqa: E501
            campaign_id ([str]): Campaign ID for engagement audience filter.. [optional]  # noqa: E501
            ad_id ([str]): Ad ID for engagement audience filter.. [optional]  # noqa: E501
            objective_type ([ObjectiveType]): Objective for engagement audience filter.. [optional]  # noqa: E501
            ad_account_id (str): Ad account ID.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """AudienceRule - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            country (str): Valid countries include: \"US\", \"CA\", and \"GB\".. [optional]  # noqa: E501
            customer_list_id (str): Customer list ID. For CUSTOMER_LIST `audience_type`.. [optional]  # noqa: E501
            engagement_domain ([str]): The audience account's verified domain. **Required** for ENGAGEMENT `audience_type`.. [optional]  # noqa: E501
            engagement_type (str): Engagement type enum. Optional for ENGAGEMENT `audience_type`. Supported values are `click`, `save`, `closeup`, `comment` and `like`. All engagements are included if this field is not set. . [optional]  # noqa: E501
            event (str): A Pinterest tag event. Optional for VISITOR `audience_type`. Possible values are `pagevisit`, `signup`, `checkout`, `viewcategory`, `search`, `addtocart`, `watchvideo`, `lead`, and `custom`. This field also accepts a partner-defined Pinterest tag event.. [optional]  # noqa: E501
            event_data (PinterestTagEventData): [optional]  # noqa: E501
            percentage (int): Percentage should be 1-10. The targeted audience should be this % size across Pinterest.. [optional]  # noqa: E501
            pin_id ([str]): IDs of engaged organic pins. Optional for ENGAGEMENT `audience_type`. For example, \"pin_id:\": [\"34567\"]. [optional]  # noqa: E501
            prefill (bool): Optional for VISITOR `audience_type`. If `true`, the specified rule on existing engagement data is applied to pre-populate the audience. If `false`, the audience is empty at creation time. The default is `true`.. [optional]  # noqa: E501
            retention_days (int): Number of days a Pinterest user remains in the audience. Optional for ENGAGEMENT and VISITOR `audience_type`. Accepted range is 1-540. Defaults to 180 if not specified.. [optional]  # noqa: E501
            seed_id ([str]): Audience ID(s). For ACTALIKE `audience_type`. . [optional]  # noqa: E501
            url ([str]): Optional for ENGAGEMENT or VISITOR `audience_type`. For ENGAGEMENT, it is the engaged pin's URL. For VISITOR, you can use it as a string or a {operator: value} object for filtering visitors based on conversion tag event URLs. Supported operators are [ =, !=, contains, not_contains].<br>Example 1:  \"url\": \"http://www.myonlinestore123.com/view_item/shoe\"<br>Example 2: \"url\": {\"contains\": \"/view_item/shoe\"}. [optional]  # noqa: E501
            visitor_source_id (str): The conversion tag ID, or the Pinterest tag ID, that you use on your website. For VISITOR `audience_type`.. [optional]  # noqa: E501
            event_source ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Optional for VISITOR. You can use it as a {'=': [value]}. Supported values are: web, mobile, offline. [optional]  # noqa: E501
            ingestion_source ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Optional for VISITOR. You can use it as a {'=': [value]}. Supported values are: tag, mmp, file_upload, conversions_api. [optional]  # noqa: E501
            engager_type (int): Optional for ENGAGEMENT. Engager type value should be 1-2.. [optional]  # noqa: E501
            campaign_id ([str]): Campaign ID for engagement audience filter.. [optional]  # noqa: E501
            ad_id ([str]): Ad ID for engagement audience filter.. [optional]  # noqa: E501
            objective_type ([ObjectiveType]): Objective for engagement audience filter.. [optional]  # noqa: E501
            ad_account_id (str): Ad account ID.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")