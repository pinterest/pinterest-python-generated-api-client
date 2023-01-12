
import unittest

from integration_test import base
from openapi_generated.pinterest_client.api.ad_accounts_api import AdAccountsApi  # noqa: E501
from openapi_generated.pinterest_client.model.ad_account import AdAccount
from openapi_generated.pinterest_client.model.ad_account_create_request import AdAccountCreateRequest
from openapi_generated.pinterest_client.model.country import Country


class TestAdAccountsApi(base.BaseIntegrationTest):
    """AdAccountsApi integration test stubs"""

    _api_class: AdAccountsApi = AdAccountsApi

    def setUp(self):
        super(TestAdAccountsApi, self).setUp()

    def test_ad_accounts_get(self):
        _api: AdAccountsApi = self._api
        account: AdAccount = _api.ad_accounts_get(self._ad_account_id)
        self.assertEqual(account.id, self._ad_account_id)

    def test_create_ad_account(self):
        _api: AdAccountsApi = self._api
        country = Country(self._ad_account_country)
        ad_account_create_request = AdAccountCreateRequest(
            country=country,
            name=self._ad_account_name,
            owner_user_id=self._owner_user_id,
        )

        ad_account = _api.ad_accounts_create(ad_account_create_request=ad_account_create_request)

        self.assertIsNotNone(ad_account)
        self.assertEqual(self._ad_account_name, ad_account.name)
        self.assertEqual(country, ad_account.country)


if __name__ == '__main__':
    unittest.main()
