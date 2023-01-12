# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_generated.pinterest_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_generated.pinterest_client.model.account import Account
from openapi_generated.pinterest_client.model.action_type import ActionType
from openapi_generated.pinterest_client.model.ad_account import AdAccount
from openapi_generated.pinterest_client.model.ad_account_analytics_response import AdAccountAnalyticsResponse
from openapi_generated.pinterest_client.model.ad_account_create_request import AdAccountCreateRequest
from openapi_generated.pinterest_client.model.ad_account_owner import AdAccountOwner
from openapi_generated.pinterest_client.model.ad_accounts_country_response import AdAccountsCountryResponse
from openapi_generated.pinterest_client.model.ad_accounts_country_response_data import AdAccountsCountryResponseData
from openapi_generated.pinterest_client.model.ad_array_response import AdArrayResponse
from openapi_generated.pinterest_client.model.ad_array_response_element import AdArrayResponseElement
from openapi_generated.pinterest_client.model.ad_common import AdCommon
from openapi_generated.pinterest_client.model.ad_create_request import AdCreateRequest
from openapi_generated.pinterest_client.model.ad_group_array_response import AdGroupArrayResponse
from openapi_generated.pinterest_client.model.ad_group_array_response_element import AdGroupArrayResponseElement
from openapi_generated.pinterest_client.model.ad_group_common import AdGroupCommon
from openapi_generated.pinterest_client.model.ad_group_create_request import AdGroupCreateRequest
from openapi_generated.pinterest_client.model.ad_group_create_request_all_of import AdGroupCreateRequestAllOf
from openapi_generated.pinterest_client.model.ad_group_response import AdGroupResponse
from openapi_generated.pinterest_client.model.ad_group_response_all_of import AdGroupResponseAllOf
from openapi_generated.pinterest_client.model.ad_group_summary_status import AdGroupSummaryStatus
from openapi_generated.pinterest_client.model.ad_group_update_request import AdGroupUpdateRequest
from openapi_generated.pinterest_client.model.ad_group_update_request_all_of import AdGroupUpdateRequestAllOf
from openapi_generated.pinterest_client.model.ad_groups_analytics_response import AdGroupsAnalyticsResponse
from openapi_generated.pinterest_client.model.ad_pin_id import AdPinId
from openapi_generated.pinterest_client.model.ad_preview_create_from_image import AdPreviewCreateFromImage
from openapi_generated.pinterest_client.model.ad_preview_create_from_pin import AdPreviewCreateFromPin
from openapi_generated.pinterest_client.model.ad_preview_request import AdPreviewRequest
from openapi_generated.pinterest_client.model.ad_preview_url_response import AdPreviewURLResponse
from openapi_generated.pinterest_client.model.ad_response import AdResponse
from openapi_generated.pinterest_client.model.ad_response_all_of import AdResponseAllOf
from openapi_generated.pinterest_client.model.ad_update_request import AdUpdateRequest
from openapi_generated.pinterest_client.model.ad_update_request1 import AdUpdateRequest1
from openapi_generated.pinterest_client.model.ads_analytics_create_async_request import AdsAnalyticsCreateAsyncRequest
from openapi_generated.pinterest_client.model.ads_analytics_create_async_request_all_of import AdsAnalyticsCreateAsyncRequestAllOf
from openapi_generated.pinterest_client.model.ads_analytics_create_async_request_all_of1 import AdsAnalyticsCreateAsyncRequestAllOf1
from openapi_generated.pinterest_client.model.ads_analytics_create_async_response import AdsAnalyticsCreateAsyncResponse
from openapi_generated.pinterest_client.model.ads_analytics_filter_column import AdsAnalyticsFilterColumn
from openapi_generated.pinterest_client.model.ads_analytics_filter_operator import AdsAnalyticsFilterOperator
from openapi_generated.pinterest_client.model.ads_analytics_get_async_response import AdsAnalyticsGetAsyncResponse
from openapi_generated.pinterest_client.model.ads_analytics_metrics_filter import AdsAnalyticsMetricsFilter
from openapi_generated.pinterest_client.model.ads_analytics_response import AdsAnalyticsResponse
from openapi_generated.pinterest_client.model.ads_analytics_targeting_type import AdsAnalyticsTargetingType
from openapi_generated.pinterest_client.model.analytics_metrics_response import AnalyticsMetricsResponse
from openapi_generated.pinterest_client.model.analytics_metrics_response_daily_metrics import AnalyticsMetricsResponseDailyMetrics
from openapi_generated.pinterest_client.model.analytics_response import AnalyticsResponse
from openapi_generated.pinterest_client.model.audience import Audience
from openapi_generated.pinterest_client.model.audience_category import AudienceCategory
from openapi_generated.pinterest_client.model.audience_common import AudienceCommon
from openapi_generated.pinterest_client.model.audience_create_request import AudienceCreateRequest
from openapi_generated.pinterest_client.model.audience_create_request1 import AudienceCreateRequest1
from openapi_generated.pinterest_client.model.audience_demographic_value import AudienceDemographicValue
from openapi_generated.pinterest_client.model.audience_demographics import AudienceDemographics
from openapi_generated.pinterest_client.model.audience_insight_category_common import AudienceInsightCategoryCommon
from openapi_generated.pinterest_client.model.audience_insight_type import AudienceInsightType
from openapi_generated.pinterest_client.model.audience_insights_response import AudienceInsightsResponse
from openapi_generated.pinterest_client.model.audience_rule import AudienceRule
from openapi_generated.pinterest_client.model.audience_type import AudienceType
from openapi_generated.pinterest_client.model.audience_update_operation_type import AudienceUpdateOperationType
from openapi_generated.pinterest_client.model.audience_update_request import AudienceUpdateRequest
from openapi_generated.pinterest_client.model.audience_update_request1 import AudienceUpdateRequest1
from openapi_generated.pinterest_client.model.availability_filter import AvailabilityFilter
from openapi_generated.pinterest_client.model.batch_operation import BatchOperation
from openapi_generated.pinterest_client.model.batch_operation_status import BatchOperationStatus
from openapi_generated.pinterest_client.model.bid_floor import BidFloor
from openapi_generated.pinterest_client.model.bid_floor_request import BidFloorRequest
from openapi_generated.pinterest_client.model.bid_floor_spec import BidFloorSpec
from openapi_generated.pinterest_client.model.board import Board
from openapi_generated.pinterest_client.model.board_owner import BoardOwner
from openapi_generated.pinterest_client.model.board_section import BoardSection
from openapi_generated.pinterest_client.model.board_update import BoardUpdate
from openapi_generated.pinterest_client.model.book_closed_response import BookClosedResponse
from openapi_generated.pinterest_client.model.brand_filter import BrandFilter
from openapi_generated.pinterest_client.model.budget_type import BudgetType
from openapi_generated.pinterest_client.model.bulk_download_request import BulkDownloadRequest
from openapi_generated.pinterest_client.model.bulk_download_request_campaign_filter import BulkDownloadRequestCampaignFilter
from openapi_generated.pinterest_client.model.bulk_download_response import BulkDownloadResponse
from openapi_generated.pinterest_client.model.bulk_entity_type import BulkEntityType
from openapi_generated.pinterest_client.model.bulk_output_format import BulkOutputFormat
from openapi_generated.pinterest_client.model.bulk_upsert_request import BulkUpsertRequest
from openapi_generated.pinterest_client.model.bulk_upsert_request_create import BulkUpsertRequestCreate
from openapi_generated.pinterest_client.model.bulk_upsert_request_update import BulkUpsertRequestUpdate
from openapi_generated.pinterest_client.model.bulk_upsert_response import BulkUpsertResponse
from openapi_generated.pinterest_client.model.bulk_upsert_status import BulkUpsertStatus
from openapi_generated.pinterest_client.model.bulk_upsert_status_response import BulkUpsertStatusResponse
from openapi_generated.pinterest_client.model.campaign_common import CampaignCommon
from openapi_generated.pinterest_client.model.campaign_create_common import CampaignCreateCommon
from openapi_generated.pinterest_client.model.campaign_create_common_all_of import CampaignCreateCommonAllOf
from openapi_generated.pinterest_client.model.campaign_create_request import CampaignCreateRequest
from openapi_generated.pinterest_client.model.campaign_create_request_all_of import CampaignCreateRequestAllOf
from openapi_generated.pinterest_client.model.campaign_create_response import CampaignCreateResponse
from openapi_generated.pinterest_client.model.campaign_create_response_data import CampaignCreateResponseData
from openapi_generated.pinterest_client.model.campaign_create_response_data_all_of import CampaignCreateResponseDataAllOf
from openapi_generated.pinterest_client.model.campaign_create_response_item import CampaignCreateResponseItem
from openapi_generated.pinterest_client.model.campaign_id import CampaignId
from openapi_generated.pinterest_client.model.campaign_response import CampaignResponse
from openapi_generated.pinterest_client.model.campaign_response_all_of import CampaignResponseAllOf
from openapi_generated.pinterest_client.model.campaign_summary_status import CampaignSummaryStatus
from openapi_generated.pinterest_client.model.campaign_update_request import CampaignUpdateRequest
from openapi_generated.pinterest_client.model.campaign_update_request_all_of import CampaignUpdateRequestAllOf
from openapi_generated.pinterest_client.model.campaign_update_response import CampaignUpdateResponse
from openapi_generated.pinterest_client.model.campaigns_analytics_response import CampaignsAnalyticsResponse
from openapi_generated.pinterest_client.model.catalogs_db_item import CatalogsDbItem
from openapi_generated.pinterest_client.model.catalogs_feed import CatalogsFeed
from openapi_generated.pinterest_client.model.catalogs_feed_credentials import CatalogsFeedCredentials
from openapi_generated.pinterest_client.model.catalogs_feed_ingestion_details import CatalogsFeedIngestionDetails
from openapi_generated.pinterest_client.model.catalogs_feed_ingestion_errors import CatalogsFeedIngestionErrors
from openapi_generated.pinterest_client.model.catalogs_feed_ingestion_info import CatalogsFeedIngestionInfo
from openapi_generated.pinterest_client.model.catalogs_feed_processing_result import CatalogsFeedProcessingResult
from openapi_generated.pinterest_client.model.catalogs_feed_processing_result_fields import CatalogsFeedProcessingResultFields
from openapi_generated.pinterest_client.model.catalogs_feed_processing_schedule import CatalogsFeedProcessingSchedule
from openapi_generated.pinterest_client.model.catalogs_feed_processing_status import CatalogsFeedProcessingStatus
from openapi_generated.pinterest_client.model.catalogs_feed_product_counts import CatalogsFeedProductCounts
from openapi_generated.pinterest_client.model.catalogs_feed_validation_details import CatalogsFeedValidationDetails
from openapi_generated.pinterest_client.model.catalogs_feed_validation_errors import CatalogsFeedValidationErrors
from openapi_generated.pinterest_client.model.catalogs_feed_validation_warnings import CatalogsFeedValidationWarnings
from openapi_generated.pinterest_client.model.catalogs_feeds_create_request import CatalogsFeedsCreateRequest
from openapi_generated.pinterest_client.model.catalogs_feeds_update_request import CatalogsFeedsUpdateRequest
from openapi_generated.pinterest_client.model.catalogs_format import CatalogsFormat
from openapi_generated.pinterest_client.model.catalogs_item_validation_details import CatalogsItemValidationDetails
from openapi_generated.pinterest_client.model.catalogs_item_validation_errors import CatalogsItemValidationErrors
from openapi_generated.pinterest_client.model.catalogs_item_validation_issue import CatalogsItemValidationIssue
from openapi_generated.pinterest_client.model.catalogs_item_validation_issues import CatalogsItemValidationIssues
from openapi_generated.pinterest_client.model.catalogs_item_validation_warnings import CatalogsItemValidationWarnings
from openapi_generated.pinterest_client.model.catalogs_items import CatalogsItems
from openapi_generated.pinterest_client.model.catalogs_items_batch import CatalogsItemsBatch
from openapi_generated.pinterest_client.model.catalogs_items_batch_request import CatalogsItemsBatchRequest
from openapi_generated.pinterest_client.model.catalogs_items_create_batch_request import CatalogsItemsCreateBatchRequest
from openapi_generated.pinterest_client.model.catalogs_items_delete_discontinued_batch_request import CatalogsItemsDeleteDiscontinuedBatchRequest
from openapi_generated.pinterest_client.model.catalogs_items_update_batch_request import CatalogsItemsUpdateBatchRequest
from openapi_generated.pinterest_client.model.catalogs_list_products_by_filter_request import CatalogsListProductsByFilterRequest
from openapi_generated.pinterest_client.model.catalogs_list_products_by_filter_request_one_of import CatalogsListProductsByFilterRequestOneOf
from openapi_generated.pinterest_client.model.catalogs_product import CatalogsProduct
from openapi_generated.pinterest_client.model.catalogs_product_group import CatalogsProductGroup
from openapi_generated.pinterest_client.model.catalogs_product_group_create_request import CatalogsProductGroupCreateRequest
from openapi_generated.pinterest_client.model.catalogs_product_group_currency_criteria import CatalogsProductGroupCurrencyCriteria
from openapi_generated.pinterest_client.model.catalogs_product_group_feed_based_case import CatalogsProductGroupFeedBasedCase
from openapi_generated.pinterest_client.model.catalogs_product_group_filter_keys import CatalogsProductGroupFilterKeys
from openapi_generated.pinterest_client.model.catalogs_product_group_filters import CatalogsProductGroupFilters
from openapi_generated.pinterest_client.model.catalogs_product_group_filters_all_of import CatalogsProductGroupFiltersAllOf
from openapi_generated.pinterest_client.model.catalogs_product_group_filters_all_of_request import CatalogsProductGroupFiltersAllOfRequest
from openapi_generated.pinterest_client.model.catalogs_product_group_filters_all_of_request_any_of import CatalogsProductGroupFiltersAllOfRequestAnyOf
from openapi_generated.pinterest_client.model.catalogs_product_group_filters_all_of_request_any_of1 import CatalogsProductGroupFiltersAllOfRequestAnyOf1
from openapi_generated.pinterest_client.model.catalogs_product_group_filters_any_of import CatalogsProductGroupFiltersAnyOf
from openapi_generated.pinterest_client.model.catalogs_product_group_merchant_based_case import CatalogsProductGroupMerchantBasedCase
from openapi_generated.pinterest_client.model.catalogs_product_group_multiple_string_criteria import CatalogsProductGroupMultipleStringCriteria
from openapi_generated.pinterest_client.model.catalogs_product_group_multiple_string_list_criteria import CatalogsProductGroupMultipleStringListCriteria
from openapi_generated.pinterest_client.model.catalogs_product_group_pricing_criteria import CatalogsProductGroupPricingCriteria
from openapi_generated.pinterest_client.model.catalogs_product_group_product_counts import CatalogsProductGroupProductCounts
from openapi_generated.pinterest_client.model.catalogs_product_group_status import CatalogsProductGroupStatus
from openapi_generated.pinterest_client.model.catalogs_product_group_type import CatalogsProductGroupType
from openapi_generated.pinterest_client.model.catalogs_product_group_update_request import CatalogsProductGroupUpdateRequest
from openapi_generated.pinterest_client.model.catalogs_product_metadata import CatalogsProductMetadata
from openapi_generated.pinterest_client.model.catalogs_status import CatalogsStatus
from openapi_generated.pinterest_client.model.condition_filter import ConditionFilter
from openapi_generated.pinterest_client.model.conversion_api_response import ConversionApiResponse
from openapi_generated.pinterest_client.model.conversion_api_response_events import ConversionApiResponseEvents
from openapi_generated.pinterest_client.model.conversion_attribution_window_days import ConversionAttributionWindowDays
from openapi_generated.pinterest_client.model.conversion_event_response import ConversionEventResponse
from openapi_generated.pinterest_client.model.conversion_events import ConversionEvents
from openapi_generated.pinterest_client.model.conversion_events_custom_data import ConversionEventsCustomData
from openapi_generated.pinterest_client.model.conversion_events_custom_data_contents import ConversionEventsCustomDataContents
from openapi_generated.pinterest_client.model.conversion_events_data import ConversionEventsData
from openapi_generated.pinterest_client.model.conversion_events_user_data import ConversionEventsUserData
from openapi_generated.pinterest_client.model.conversion_events_user_data_any_of import ConversionEventsUserDataAnyOf
from openapi_generated.pinterest_client.model.conversion_events_user_data_any_of1 import ConversionEventsUserDataAnyOf1
from openapi_generated.pinterest_client.model.conversion_events_user_data_any_of2 import ConversionEventsUserDataAnyOf2
from openapi_generated.pinterest_client.model.conversion_report_attribution_type import ConversionReportAttributionType
from openapi_generated.pinterest_client.model.conversion_report_time_type import ConversionReportTimeType
from openapi_generated.pinterest_client.model.conversion_tag_common import ConversionTagCommon
from openapi_generated.pinterest_client.model.conversion_tag_configs import ConversionTagConfigs
from openapi_generated.pinterest_client.model.conversion_tag_create import ConversionTagCreate
from openapi_generated.pinterest_client.model.conversion_tag_list_response import ConversionTagListResponse
from openapi_generated.pinterest_client.model.conversion_tag_response import ConversionTagResponse
from openapi_generated.pinterest_client.model.conversion_tag_type import ConversionTagType
from openapi_generated.pinterest_client.model.conversion_tags_ocpm_eligible_response import ConversionTagsOcpmEligibleResponse
from openapi_generated.pinterest_client.model.country import Country
from openapi_generated.pinterest_client.model.creative_type import CreativeType
from openapi_generated.pinterest_client.model.currency import Currency
from openapi_generated.pinterest_client.model.currency_filter import CurrencyFilter
from openapi_generated.pinterest_client.model.custom_label0_filter import CustomLabel0Filter
from openapi_generated.pinterest_client.model.custom_label1_filter import CustomLabel1Filter
from openapi_generated.pinterest_client.model.custom_label2_filter import CustomLabel2Filter
from openapi_generated.pinterest_client.model.custom_label3_filter import CustomLabel3Filter
from openapi_generated.pinterest_client.model.custom_label4_filter import CustomLabel4Filter
from openapi_generated.pinterest_client.model.customer_list import CustomerList
from openapi_generated.pinterest_client.model.customer_list_request import CustomerListRequest
from openapi_generated.pinterest_client.model.customer_list_update_request import CustomerListUpdateRequest
from openapi_generated.pinterest_client.model.data_output_format import DataOutputFormat
from openapi_generated.pinterest_client.model.data_status import DataStatus
from openapi_generated.pinterest_client.model.delivery_metrics_response import DeliveryMetricsResponse
from openapi_generated.pinterest_client.model.delivery_metrics_response_items import DeliveryMetricsResponseItems
from openapi_generated.pinterest_client.model.enhanced_match_status_type import EnhancedMatchStatusType
from openapi_generated.pinterest_client.model.entity_status import EntityStatus
from openapi_generated.pinterest_client.model.error import Error
from openapi_generated.pinterest_client.model.exception import Exception
from openapi_generated.pinterest_client.model.feed_fields import FeedFields
from openapi_generated.pinterest_client.model.gender_filter import GenderFilter
from openapi_generated.pinterest_client.model.get_audiences_order_by import GetAudiencesOrderBy
from openapi_generated.pinterest_client.model.google_product_category0_filter import GoogleProductCategory0Filter
from openapi_generated.pinterest_client.model.google_product_category1_filter import GoogleProductCategory1Filter
from openapi_generated.pinterest_client.model.google_product_category2_filter import GoogleProductCategory2Filter
from openapi_generated.pinterest_client.model.google_product_category3_filter import GoogleProductCategory3Filter
from openapi_generated.pinterest_client.model.google_product_category4_filter import GoogleProductCategory4Filter
from openapi_generated.pinterest_client.model.google_product_category5_filter import GoogleProductCategory5Filter
from openapi_generated.pinterest_client.model.google_product_category6_filter import GoogleProductCategory6Filter
from openapi_generated.pinterest_client.model.granularity import Granularity
from openapi_generated.pinterest_client.model.image_details import ImageDetails
from openapi_generated.pinterest_client.model.image_metadata import ImageMetadata
from openapi_generated.pinterest_client.model.inline_object import InlineObject
from openapi_generated.pinterest_client.model.item_attributes import ItemAttributes
from openapi_generated.pinterest_client.model.item_attributes_all_of import ItemAttributesAllOf
from openapi_generated.pinterest_client.model.item_batch_record import ItemBatchRecord
from openapi_generated.pinterest_client.model.item_create_batch_record import ItemCreateBatchRecord
from openapi_generated.pinterest_client.model.item_delete_discontinued_batch_record import ItemDeleteDiscontinuedBatchRecord
from openapi_generated.pinterest_client.model.item_group_id_filter import ItemGroupIdFilter
from openapi_generated.pinterest_client.model.item_id_filter import ItemIdFilter
from openapi_generated.pinterest_client.model.item_processing_record import ItemProcessingRecord
from openapi_generated.pinterest_client.model.item_processing_status import ItemProcessingStatus
from openapi_generated.pinterest_client.model.item_response import ItemResponse
from openapi_generated.pinterest_client.model.item_response_any_of import ItemResponseAnyOf
from openapi_generated.pinterest_client.model.item_response_any_of1 import ItemResponseAnyOf1
from openapi_generated.pinterest_client.model.item_update_batch_record import ItemUpdateBatchRecord
from openapi_generated.pinterest_client.model.item_validation_event import ItemValidationEvent
from openapi_generated.pinterest_client.model.keyword import Keyword
from openapi_generated.pinterest_client.model.keyword_error import KeywordError
from openapi_generated.pinterest_client.model.keyword_metrics import KeywordMetrics
from openapi_generated.pinterest_client.model.keyword_metrics_response import KeywordMetricsResponse
from openapi_generated.pinterest_client.model.keyword_update import KeywordUpdate
from openapi_generated.pinterest_client.model.keyword_update_body import KeywordUpdateBody
from openapi_generated.pinterest_client.model.keywords_common import KeywordsCommon
from openapi_generated.pinterest_client.model.keywords_metrics_array_response import KeywordsMetricsArrayResponse
from openapi_generated.pinterest_client.model.keywords_request import KeywordsRequest
from openapi_generated.pinterest_client.model.keywords_response import KeywordsResponse
from openapi_generated.pinterest_client.model.language import Language
from openapi_generated.pinterest_client.model.line_item import LineItem
from openapi_generated.pinterest_client.model.match_type import MatchType
from openapi_generated.pinterest_client.model.match_type_response import MatchTypeResponse
from openapi_generated.pinterest_client.model.max_price_filter import MaxPriceFilter
from openapi_generated.pinterest_client.model.media_upload import MediaUpload
from openapi_generated.pinterest_client.model.media_upload_all_of import MediaUploadAllOf
from openapi_generated.pinterest_client.model.media_upload_all_of_upload_parameters import MediaUploadAllOfUploadParameters
from openapi_generated.pinterest_client.model.media_upload_details import MediaUploadDetails
from openapi_generated.pinterest_client.model.media_upload_request import MediaUploadRequest
from openapi_generated.pinterest_client.model.media_upload_status import MediaUploadStatus
from openapi_generated.pinterest_client.model.media_upload_type import MediaUploadType
from openapi_generated.pinterest_client.model.metrics import Metrics
from openapi_generated.pinterest_client.model.metrics_reporting_level import MetricsReportingLevel
from openapi_generated.pinterest_client.model.metrics_response import MetricsResponse
from openapi_generated.pinterest_client.model.min_price_filter import MinPriceFilter
from openapi_generated.pinterest_client.model.non_nullable_catalogs_currency import NonNullableCatalogsCurrency
from openapi_generated.pinterest_client.model.non_nullable_product_availability_type import NonNullableProductAvailabilityType
from openapi_generated.pinterest_client.model.nullable_catalogs_item_field_type import NullableCatalogsItemFieldType
from openapi_generated.pinterest_client.model.nullable_currency import NullableCurrency
from openapi_generated.pinterest_client.model.oauth_access_token_request_code import OauthAccessTokenRequestCode
from openapi_generated.pinterest_client.model.oauth_access_token_request_code_all_of import OauthAccessTokenRequestCodeAllOf
from openapi_generated.pinterest_client.model.oauth_access_token_request_refresh import OauthAccessTokenRequestRefresh
from openapi_generated.pinterest_client.model.oauth_access_token_request_refresh_all_of import OauthAccessTokenRequestRefreshAllOf
from openapi_generated.pinterest_client.model.oauth_access_token_response import OauthAccessTokenResponse
from openapi_generated.pinterest_client.model.oauth_access_token_response_code import OauthAccessTokenResponseCode
from openapi_generated.pinterest_client.model.oauth_access_token_response_code_all_of import OauthAccessTokenResponseCodeAllOf
from openapi_generated.pinterest_client.model.oauth_access_token_response_refresh import OauthAccessTokenResponseRefresh
from openapi_generated.pinterest_client.model.objective_type import ObjectiveType
from openapi_generated.pinterest_client.model.optimization_goal_metadata import OptimizationGoalMetadata
from openapi_generated.pinterest_client.model.optimization_goal_metadata_conversion_tag_v3_goal_metadata import OptimizationGoalMetadataConversionTagV3GoalMetadata
from openapi_generated.pinterest_client.model.optimization_goal_metadata_conversion_tag_v3_goal_metadata_attribution_windows import OptimizationGoalMetadataConversionTagV3GoalMetadataAttributionWindows
from openapi_generated.pinterest_client.model.optimization_goal_metadata_frequency_goal_metadata import OptimizationGoalMetadataFrequencyGoalMetadata
from openapi_generated.pinterest_client.model.optimization_goal_metadata_scrollup_goal_metadata import OptimizationGoalMetadataScrollupGoalMetadata
from openapi_generated.pinterest_client.model.order_line import OrderLine
from openapi_generated.pinterest_client.model.order_line_all_of import OrderLineAllOf
from openapi_generated.pinterest_client.model.order_line_error import OrderLineError
from openapi_generated.pinterest_client.model.order_line_paid_type import OrderLinePaidType
from openapi_generated.pinterest_client.model.order_line_response import OrderLineResponse
from openapi_generated.pinterest_client.model.order_line_single_response import OrderLineSingleResponse
from openapi_generated.pinterest_client.model.order_line_status import OrderLineStatus
from openapi_generated.pinterest_client.model.order_lines import OrderLines
from openapi_generated.pinterest_client.model.order_lines_array_response import OrderLinesArrayResponse
from openapi_generated.pinterest_client.model.pacing_delivery_type import PacingDeliveryType
from openapi_generated.pinterest_client.model.paginated import Paginated
from openapi_generated.pinterest_client.model.pin import Pin
from openapi_generated.pinterest_client.model.pin_media import PinMedia
from openapi_generated.pinterest_client.model.pin_media_metadata import PinMediaMetadata
from openapi_generated.pinterest_client.model.pin_media_source import PinMediaSource
from openapi_generated.pinterest_client.model.pin_media_source_image_base64 import PinMediaSourceImageBase64
from openapi_generated.pinterest_client.model.pin_media_source_image_url import PinMediaSourceImageURL
from openapi_generated.pinterest_client.model.pin_media_source_images_base64 import PinMediaSourceImagesBase64
from openapi_generated.pinterest_client.model.pin_media_source_images_base64_items import PinMediaSourceImagesBase64Items
from openapi_generated.pinterest_client.model.pin_media_source_images_url import PinMediaSourceImagesURL
from openapi_generated.pinterest_client.model.pin_media_source_images_url_items import PinMediaSourceImagesURLItems
from openapi_generated.pinterest_client.model.pin_media_source_video_id import PinMediaSourceVideoID
from openapi_generated.pinterest_client.model.pin_media_with_image import PinMediaWithImage
from openapi_generated.pinterest_client.model.pin_media_with_image_all_of import PinMediaWithImageAllOf
from openapi_generated.pinterest_client.model.pin_media_with_image_and_video import PinMediaWithImageAndVideo
from openapi_generated.pinterest_client.model.pin_media_with_image_and_video_all_of import PinMediaWithImageAndVideoAllOf
from openapi_generated.pinterest_client.model.pin_media_with_images import PinMediaWithImages
from openapi_generated.pinterest_client.model.pin_media_with_images_all_of import PinMediaWithImagesAllOf
from openapi_generated.pinterest_client.model.pin_media_with_video import PinMediaWithVideo
from openapi_generated.pinterest_client.model.pin_media_with_video_all_of import PinMediaWithVideoAllOf
from openapi_generated.pinterest_client.model.pin_media_with_videos import PinMediaWithVideos
from openapi_generated.pinterest_client.model.pin_media_with_videos_all_of import PinMediaWithVideosAllOf
from openapi_generated.pinterest_client.model.pin_promotion_summary_status import PinPromotionSummaryStatus
from openapi_generated.pinterest_client.model.pinterest_tag_event_data import PinterestTagEventData
from openapi_generated.pinterest_client.model.placement_group_type import PlacementGroupType
from openapi_generated.pinterest_client.model.product_availability_type import ProductAvailabilityType
from openapi_generated.pinterest_client.model.product_group_analytics_response import ProductGroupAnalyticsResponse
from openapi_generated.pinterest_client.model.product_group_promotion import ProductGroupPromotion
from openapi_generated.pinterest_client.model.product_group_promotion_array_element import ProductGroupPromotionArrayElement
from openapi_generated.pinterest_client.model.product_group_promotion_array_response import ProductGroupPromotionArrayResponse
from openapi_generated.pinterest_client.model.product_group_promotion_common import ProductGroupPromotionCommon
from openapi_generated.pinterest_client.model.product_group_promotion_create_request import ProductGroupPromotionCreateRequest
from openapi_generated.pinterest_client.model.product_group_promotion_update_request import ProductGroupPromotionUpdateRequest
from openapi_generated.pinterest_client.model.product_group_promotion_update_response_item import ProductGroupPromotionUpdateResponseItem
from openapi_generated.pinterest_client.model.product_group_summary_status import ProductGroupSummaryStatus
from openapi_generated.pinterest_client.model.product_groups_create_request_feed_base_case import ProductGroupsCreateRequestFeedBaseCase
from openapi_generated.pinterest_client.model.product_type0_filter import ProductType0Filter
from openapi_generated.pinterest_client.model.product_type1_filter import ProductType1Filter
from openapi_generated.pinterest_client.model.product_type2_filter import ProductType2Filter
from openapi_generated.pinterest_client.model.product_type3_filter import ProductType3Filter
from openapi_generated.pinterest_client.model.product_type4_filter import ProductType4Filter
from openapi_generated.pinterest_client.model.related_terms import RelatedTerms
from openapi_generated.pinterest_client.model.related_terms_related_terms_list import RelatedTermsRelatedTermsList
from openapi_generated.pinterest_client.model.reporting_column_async import ReportingColumnAsync
from openapi_generated.pinterest_client.model.single_interest_targeting_option_response import SingleInterestTargetingOptionResponse
from openapi_generated.pinterest_client.model.targeting_option_response import TargetingOptionResponse
from openapi_generated.pinterest_client.model.targeting_spec import TargetingSpec
from openapi_generated.pinterest_client.model.targeting_spec1 import TargetingSpec1
from openapi_generated.pinterest_client.model.targeting_spec_shoppingretargeting import TargetingSpecSHOPPINGRETARGETING
from openapi_generated.pinterest_client.model.targeting_spec_shoppingretargeting1 import TargetingSpecSHOPPINGRETARGETING1
from openapi_generated.pinterest_client.model.targeting_type_filter import TargetingTypeFilter
from openapi_generated.pinterest_client.model.terms_of_service import TermsOfService
from openapi_generated.pinterest_client.model.terms_suggested_response import TermsSuggestedResponse
from openapi_generated.pinterest_client.model.top_pins_analytics_response import TopPinsAnalyticsResponse
from openapi_generated.pinterest_client.model.top_pins_analytics_response_date_availability import TopPinsAnalyticsResponseDateAvailability
from openapi_generated.pinterest_client.model.top_pins_analytics_response_pins import TopPinsAnalyticsResponsePins
from openapi_generated.pinterest_client.model.top_video_pins_analytics_response import TopVideoPinsAnalyticsResponse
from openapi_generated.pinterest_client.model.top_video_pins_analytics_response_pins import TopVideoPinsAnalyticsResponsePins
from openapi_generated.pinterest_client.model.tracking_urls import TrackingUrls
from openapi_generated.pinterest_client.model.updatable_item_attributes import UpdatableItemAttributes
from openapi_generated.pinterest_client.model.user_list_operation_type import UserListOperationType
from openapi_generated.pinterest_client.model.user_list_type import UserListType
from openapi_generated.pinterest_client.model.user_website_summary import UserWebsiteSummary
from openapi_generated.pinterest_client.model.video_metadata import VideoMetadata