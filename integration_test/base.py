import random

from openapi_generated.pinterest_client.api.ad_groups_api import AdGroupsApi
from openapi_generated.pinterest_client.api.boards_api import BoardsApi
from openapi_generated.pinterest_client.api.campaigns_api import CampaignsApi
from openapi_generated.pinterest_client.api.pins_api import PinsApi
from openapi_generated.pinterest_client.exceptions import NotFoundException, ApiException
from openapi_generated.pinterest_client.model.action_type import ActionType
from openapi_generated.pinterest_client.model.ad_group_create_request import AdGroupCreateRequest
from openapi_generated.pinterest_client.model.board import Board
from openapi_generated.pinterest_client.model.campaign_create_request import CampaignCreateRequest
from openapi_generated.pinterest_client.model.objective_type import ObjectiveType
from openapi_generated.pinterest_client.model.pin import Pin
from .config import DEFAULT_AD_ACCOUNT_ID
from .config import DEFAULT_AD_ACCOUNT_COUNTRY
from .config import DEFAULT_AD_ACCOUNT_NAME
from .config import DEFAULT_BOARD_ID
from .config import OWNER_USER_ID
import unittest

from integration_test.utils import get_default_client, parse_to_object, get_random_number


class BaseIntegrationTest(unittest.TestCase):
    _api_class = None
    _pin = None
    _board = None
    _campaign = None
    _ad_group = None

    def setUp(self):
        super(BaseIntegrationTest, self).setUp()
        self._ad_account_id = DEFAULT_AD_ACCOUNT_ID
        self._ad_account_name = DEFAULT_AD_ACCOUNT_NAME
        self._ad_account_country = DEFAULT_AD_ACCOUNT_COUNTRY
        self._board_id = DEFAULT_BOARD_ID
        self._owner_user_id = OWNER_USER_ID
        self._api_client = get_default_client()
        self._api = self._api_class(api_client=self._api_client)

    def tearDown(self) -> None:
        super(BaseIntegrationTest, self).tearDown()
        self._clean_organic()

    @property
    def pin(self):
        if self._pin is None:
            self._pin = PinsApi(self._api_client).pins_create(
                Pin(
                    title='Test PIN Generated Client Library {}'.format(get_random_number()),
                    link="https://www.pinterest.com/",
                    board_id=self.board.id,
                    media_source={
                        "source_type": "image_url",
                        "url": "https://fastly.picsum.photos/id/1043/200/300.jpg"
                               "?hmac=3l-zIM3sjEYfLwln1cOurui-983Bxq1zjEYt9HeScyQ",
                    }
                )
            )
        return self._pin

    @property
    def board(self):
        if self._board is None:
            try:
                self._board = BoardsApi(self._api_client).boards_get(self._board_id)
            except NotFoundException as _:
                for _ in range(0, 3):
                    try:
                        self._board = BoardsApi(self._api_client).boards_create(
                            Board(
                                name='Board Client Library {}'.format(get_random_number()),
                            )
                        )
                        break
                    except ApiException as _:
                        continue
        return self._board

    @property
    def campaign(self):
        if self._campaign is None:
            response = CampaignsApi(self._api_client).campaigns_create(
                ad_account_id=self._ad_account_id,
                campaign_create_request=[
                    CampaignCreateRequest(
                        ad_account_id=str(self._ad_account_id),
                        name=self._ad_account_name,
                        daily_spend_cap=1432744744,
                        order_line_id=None,
                        tracking_urls=None,
                        start_time=None,
                        end_time=None,
                        objective_type=ObjectiveType("AWARENESS"),
                        is_campaign_budget_optimization=False,
                        is_flexible_daily_budgets=False,
                        default_ad_group_budget_in_micro_currency=None,
                        is_automated_campaign=False,
                    )
                ],
            )
            self._campaign = parse_to_object(response)
        return self._campaign

    @property
    def ad_group(self):
        if self._ad_group is None:
            action_type = ActionType('IMPRESSION')
            response = AdGroupsApi(self._api_client).ad_groups_create(
                ad_account_id=self._ad_account_id,
                ad_group_create_request=[
                    AdGroupCreateRequest(
                        ad_account_id=self._ad_account_id,
                        name='CLIENT_LIBRARY_ADD_GROUP_INTEGRATION_TEST_{}'.format(get_random_number()),
                        campaign_id=self.campaign.id,
                        billable_event=action_type,
                        tracking_url=None,
                        bid_in_micro_currency=5000000,
                    )],
            )
            self._ad_group = parse_to_object(response)
        return self._ad_group

    def _clean_organic(self):
        if self._pin:
            PinsApi(self._api_client).pins_delete(self._pin.id)
        if self._board:
            BoardsApi(self._api_client).boards_delete(self._board.id)

