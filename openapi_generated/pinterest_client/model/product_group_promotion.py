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
    from openapi_generated.pinterest_client.model.creative_type import CreativeType
    from openapi_generated.pinterest_client.model.entity_status import EntityStatus
    from openapi_generated.pinterest_client.model.product_group_promotion_common import ProductGroupPromotionCommon
    globals()['CreativeType'] = CreativeType
    globals()['EntityStatus'] = EntityStatus
    globals()['ProductGroupPromotionCommon'] = ProductGroupPromotionCommon


class ProductGroupPromotion(ModelComposed):
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
        ('id',): {
            'regex': {
                'pattern': r'^\d+$',  # noqa: E501
            },
        },
        ('ad_group_id',): {
            'regex': {
                'pattern': r'^(AG)?\d+$',  # noqa: E501
            },
        },
        ('parent_id',): {
            'regex': {
                'pattern': r'^\d+$',  # noqa: E501
            },
        },
        ('catalogs_product_group_id',): {
            'regex': {
                'pattern': r'^\d+$',  # noqa: E501
            },
        },
        ('collections_hero_pin_id',): {
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
            'id': (str,),  # noqa: E501
            'ad_group_id': (str,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
            'bid_in_micro_currency': (int,),  # noqa: E501
            'included': (bool, none_type,),  # noqa: E501
            'definition': (str, none_type,),  # noqa: E501
            'relative_definition': (str, none_type,),  # noqa: E501
            'parent_id': (str, none_type,),  # noqa: E501
            'slideshow_collections_title': (str, none_type,),  # noqa: E501
            'slideshow_collections_description': (str, none_type,),  # noqa: E501
            'status': (EntityStatus,),  # noqa: E501
            'tracking_url': (str, none_type,),  # noqa: E501
            'catalogs_product_group_id': (str, none_type,),  # noqa: E501
            'catalogs_product_group_name': (str, none_type,),  # noqa: E501
            'creative_type': (CreativeType,),  # noqa: E501
            'collections_hero_pin_id': (str, none_type,),  # noqa: E501
            'collections_hero_destination_url': (str, none_type,),  # noqa: E501
            'is_mdl': (bool, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'ad_group_id': 'ad_group_id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'bid_in_micro_currency': 'bid_in_micro_currency',  # noqa: E501
        'included': 'included',  # noqa: E501
        'definition': 'definition',  # noqa: E501
        'relative_definition': 'relative_definition',  # noqa: E501
        'parent_id': 'parent_id',  # noqa: E501
        'slideshow_collections_title': 'slideshow_collections_title',  # noqa: E501
        'slideshow_collections_description': 'slideshow_collections_description',  # noqa: E501
        'status': 'status',  # noqa: E501
        'tracking_url': 'tracking_url',  # noqa: E501
        'catalogs_product_group_id': 'catalogs_product_group_id',  # noqa: E501
        'catalogs_product_group_name': 'catalogs_product_group_name',  # noqa: E501
        'creative_type': 'creative_type',  # noqa: E501
        'collections_hero_pin_id': 'collections_hero_pin_id',  # noqa: E501
        'collections_hero_destination_url': 'collections_hero_destination_url',  # noqa: E501
        'is_mdl': 'is_mdl',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ProductGroupPromotion - a model defined in OpenAPI

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
            id (str): ID of the product group promotion.. [optional]  # noqa: E501
            ad_group_id (str): ID of the ad group the product group belongs to.. [optional]  # noqa: E501
            type (str, none_type): Product group promotion. [optional]  # noqa: E501
            bid_in_micro_currency (int): The bid in micro currency.. [optional]  # noqa: E501
            included (bool, none_type): True if the group is BIDDABLE, false if it should be EXCLUDED from serving ads.. [optional]  # noqa: E501
            definition (str, none_type): The full product group definition path. [optional]  # noqa: E501
            relative_definition (str, none_type): The definition of the product group, relative to its parent - an attribute name/value pair. [optional]  # noqa: E501
            parent_id (str, none_type): The parent Product Group ID of this Product Group. [optional]  # noqa: E501
            slideshow_collections_title (str, none_type): Slideshow Collections Title. [optional]  # noqa: E501
            slideshow_collections_description (str, none_type): Slideshow Collections Description. [optional]  # noqa: E501
            status (EntityStatus): [optional]  # noqa: E501
            tracking_url (str, none_type): Tracking template for proudct group promotions. 4000 limit. [optional]  # noqa: E501
            catalogs_product_group_id (str, none_type): ID of the catalogs product group that this product group promotion references. [optional]  # noqa: E501
            catalogs_product_group_name (str, none_type): Catalogs product group name. [optional]  # noqa: E501
            creative_type (CreativeType): [optional]  # noqa: E501
            collections_hero_pin_id (str, none_type): Hero Pin ID if this PG is promoted as a Collection. [optional]  # noqa: E501
            collections_hero_destination_url (str, none_type): Collections Hero Destination Url. [optional]  # noqa: E501
            is_mdl (bool, none_type): If set to true products promoted in this product group will use the Mobile Deep Link specified in your catalog. [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ProductGroupPromotion - a model defined in OpenAPI

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
            id (str): ID of the product group promotion.. [optional]  # noqa: E501
            ad_group_id (str): ID of the ad group the product group belongs to.. [optional]  # noqa: E501
            type (str, none_type): Product group promotion. [optional]  # noqa: E501
            bid_in_micro_currency (int): The bid in micro currency.. [optional]  # noqa: E501
            included (bool, none_type): True if the group is BIDDABLE, false if it should be EXCLUDED from serving ads.. [optional]  # noqa: E501
            definition (str, none_type): The full product group definition path. [optional]  # noqa: E501
            relative_definition (str, none_type): The definition of the product group, relative to its parent - an attribute name/value pair. [optional]  # noqa: E501
            parent_id (str, none_type): The parent Product Group ID of this Product Group. [optional]  # noqa: E501
            slideshow_collections_title (str, none_type): Slideshow Collections Title. [optional]  # noqa: E501
            slideshow_collections_description (str, none_type): Slideshow Collections Description. [optional]  # noqa: E501
            status (EntityStatus): [optional]  # noqa: E501
            tracking_url (str, none_type): Tracking template for proudct group promotions. 4000 limit. [optional]  # noqa: E501
            catalogs_product_group_id (str, none_type): ID of the catalogs product group that this product group promotion references. [optional]  # noqa: E501
            catalogs_product_group_name (str, none_type): Catalogs product group name. [optional]  # noqa: E501
            creative_type (CreativeType): [optional]  # noqa: E501
            collections_hero_pin_id (str, none_type): Hero Pin ID if this PG is promoted as a Collection. [optional]  # noqa: E501
            collections_hero_destination_url (str, none_type): Collections Hero Destination Url. [optional]  # noqa: E501
            is_mdl (bool, none_type): If set to true products promoted in this product group will use the Mobile Deep Link specified in your catalog. [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [

          ],
          'oneOf': [
          ],
        }
