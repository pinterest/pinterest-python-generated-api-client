"""
    Pinterest REST API

    Pinterest's REST API  # noqa: E501

    The version of the OpenAPI document: 5.8.0
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



class BoardCategoriesEnum(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'ANIMALS': "animals",
            'APPAREL': "apparel",
            'ARCHITECTURE': "architecture",
            'ART': "art",
            'ART_ARCH': "art_arch",
            'CARS_MOTORCYCLES': "cars_motorcycles",
            'CELEBRITIES': "celebrities",
            'CELEBRITIES_PUBLI': "celebrities_publi",
            'COMMERCE': "commerce",
            'CORGIS': "corgis",
            'CULTURE': "culture",
            'DESIGN': "design",
            'DIY_CRAFTS': "diy_crafts",
            'EDUCATION': "education",
            'EVERYTHING': "everything",
            'FASHION': "fashion",
            'FEATURED': "featured",
            'FILM_MUSIC_BOOKS': "film_music_books",
            'FITNESS': "fitness",
            'FOOD_DRINK': "food_drink",
            'FOR_DAD': "for_dad",
            'FRESH': "fresh",
            'GARDENING': "gardening",
            'GEEK': "geek",
            'GIFT_GUIDES': "gift_guides",
            'GIFTS': "gifts",
            'HAIR_BEAUTY': "hair_beauty",
            'HEALTH_FITNESS': "health_fitness",
            'HISTORY': "history",
            'HOLIDAYS': "holidays",
            'HOLIDAYS_EVENTS': "holidays_events",
            'HOME': "home",
            'HOME_DECOR': "home_decor",
            'HOME_IMPROVEMENT': "home_improvement",
            'HUMOR': "humor",
            'ILLUSTRATIONS_POS': "illustrations_pos",
            'KIDS': "kids",
            'MEN_APPAREL': "men_apparel",
            'MENS_FASHION': "mens_fashion",
            'MYLIFE': "mylife",
            'OTHER': "other",
            'OUTDOORS': "outdoors",
            'PEOPLE': "people",
            'PETS': "pets",
            'PHOTOGRAPHY': "photography",
            'POPULAR': "popular",
            'PRINTS_POSTERS': "prints_posters",
            'PRODUCTS': "products",
            'QUOTES': "quotes",
            'SCIENCE': "science",
            'SCIENCE_NATURE': "science_nature",
            'SHOP': "shop",
            'SHOP_SPACE': "shop_space",
            'SPORTS': "sports",
            'TATTOOS': "tattoos",
            'TECHNOLOGY': "technology",
            'TRAVEL': "travel",
            'TRAVEL_PLACES': "travel_places",
            'VIDEOS': "videos",
            'WEDDING_EVENTS': "wedding_events",
            'WEDDINGS': "weddings",
            'WOMEN_APPAREL': "women_apparel",
            'WOMENS_FASHION': "womens_fashion",
        },
    }

    validations = {
    }

    additional_properties_type = None

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
        return {
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """BoardCategoriesEnum - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): Board category.., must be one of ["animals", "apparel", "architecture", "art", "art_arch", "cars_motorcycles", "celebrities", "celebrities_publi", "commerce", "corgis", "culture", "design", "diy_crafts", "education", "everything", "fashion", "featured", "film_music_books", "fitness", "food_drink", "for_dad", "fresh", "gardening", "geek", "gift_guides", "gifts", "hair_beauty", "health_fitness", "history", "holidays", "holidays_events", "home", "home_decor", "home_improvement", "humor", "illustrations_pos", "kids", "men_apparel", "mens_fashion", "mylife", "other", "outdoors", "people", "pets", "photography", "popular", "prints_posters", "products", "quotes", "science", "science_nature", "shop", "shop_space", "sports", "tattoos", "technology", "travel", "travel_places", "videos", "wedding_events", "weddings", "women_apparel", "womens_fashion", ]  # noqa: E501

        Keyword Args:
            value (str): Board category.., must be one of ["animals", "apparel", "architecture", "art", "art_arch", "cars_motorcycles", "celebrities", "celebrities_publi", "commerce", "corgis", "culture", "design", "diy_crafts", "education", "everything", "fashion", "featured", "film_music_books", "fitness", "food_drink", "for_dad", "fresh", "gardening", "geek", "gift_guides", "gifts", "hair_beauty", "health_fitness", "history", "holidays", "holidays_events", "home", "home_decor", "home_improvement", "humor", "illustrations_pos", "kids", "men_apparel", "mens_fashion", "mylife", "other", "outdoors", "people", "pets", "photography", "popular", "prints_posters", "products", "quotes", "science", "science_nature", "shop", "shop_space", "sports", "tattoos", "technology", "travel", "travel_places", "videos", "wedding_events", "weddings", "women_apparel", "womens_fashion", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """BoardCategoriesEnum - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): Board category.., must be one of ["animals", "apparel", "architecture", "art", "art_arch", "cars_motorcycles", "celebrities", "celebrities_publi", "commerce", "corgis", "culture", "design", "diy_crafts", "education", "everything", "fashion", "featured", "film_music_books", "fitness", "food_drink", "for_dad", "fresh", "gardening", "geek", "gift_guides", "gifts", "hair_beauty", "health_fitness", "history", "holidays", "holidays_events", "home", "home_decor", "home_improvement", "humor", "illustrations_pos", "kids", "men_apparel", "mens_fashion", "mylife", "other", "outdoors", "people", "pets", "photography", "popular", "prints_posters", "products", "quotes", "science", "science_nature", "shop", "shop_space", "sports", "tattoos", "technology", "travel", "travel_places", "videos", "wedding_events", "weddings", "women_apparel", "womens_fashion", ]  # noqa: E501

        Keyword Args:
            value (str): Board category.., must be one of ["animals", "apparel", "architecture", "art", "art_arch", "cars_motorcycles", "celebrities", "celebrities_publi", "commerce", "corgis", "culture", "design", "diy_crafts", "education", "everything", "fashion", "featured", "film_music_books", "fitness", "food_drink", "for_dad", "fresh", "gardening", "geek", "gift_guides", "gifts", "hair_beauty", "health_fitness", "history", "holidays", "holidays_events", "home", "home_decor", "home_improvement", "humor", "illustrations_pos", "kids", "men_apparel", "mens_fashion", "mylife", "other", "outdoors", "people", "pets", "photography", "popular", "prints_posters", "products", "quotes", "science", "science_nature", "shop", "shop_space", "sports", "tattoos", "technology", "travel", "travel_places", "videos", "wedding_events", "weddings", "women_apparel", "womens_fashion", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self