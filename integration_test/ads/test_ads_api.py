
import unittest

from integration_test import base
from integration_test.utils import parse_to_object
from openapi_generated.pinterest_client.api.ads_api import AdsApi
from openapi_generated.pinterest_client.model.ad_create_request import AdCreateRequest
from openapi_generated.pinterest_client.model.ad_update_request import AdUpdateRequest
from openapi_generated.pinterest_client.model.creative_type import CreativeType
from openapi_generated.pinterest_client.model.entity_status import EntityStatus


class TestAdsApiApi(base.BaseIntegrationTest):
    """AdAccountsApi integration test stubs"""

    _api_class: AdsApi = AdsApi

    def setUp(self):
        super(TestAdsApiApi, self).setUp()

    def test_create_ad(self):
        _api: AdsApi = self._api

        ad_create_request: AdCreateRequest = AdCreateRequest(
            ad_account_id=self._ad_account_id,
            ad_group_id=self.ad_group.id,
            creative_type=CreativeType('REGULAR'),
            pin_id=self.pin.id,
            name='Test_create_ad',
            status=EntityStatus('ACTIVE'),
        )

        request = _api.ads_create(
            ad_account_id=self._ad_account_id,
            ad_create_request=[ad_create_request]
        )
        ads = parse_to_object(request)

        self.assertIsNotNone(ads)
        self.assertEqual(ads.ad_account_id, self._ad_account_id)
        self.assertEqual(ads.ad_group_id, self.ad_group.id)
        self.assertEqual(ads.pin_id, self.pin.id)

    def test_update_ad(self):
        _api: AdsApi = self._api

        name = 'Test_create_ad'
        ad_create_request: AdCreateRequest = AdCreateRequest(
            ad_account_id=self._ad_account_id,
            ad_group_id=self.ad_group.id,
            creative_type=CreativeType('REGULAR'),
            pin_id=self.pin.id,
            name=name,
            status=EntityStatus('ACTIVE'),
        )

        created_request = _api.ads_create(
            ad_account_id=self._ad_account_id,
            ad_create_request=[ad_create_request]
        )
        created_ad = parse_to_object(created_request)

        self.assertIsNotNone(created_ad)
        self.assertEqual(created_ad.name, name)
        self.assertEqual(created_ad.ad_account_id, self._ad_account_id)
        self.assertEqual(created_ad.ad_group_id, self.ad_group.id)
        self.assertEqual(created_ad.pin_id, self.pin.id)

        update_name = '{}-{}'.format(name, 'update')
        ad_update_request: AdUpdateRequest = AdUpdateRequest(
            id=created_ad.id,
            name=update_name
        )

        updated_request = _api.ads_update(
            ad_account_id=self._ad_account_id,
            ad_update_request=[ad_update_request]
        )
        updated_ad = parse_to_object(updated_request)

        self.assertIsNotNone(updated_ad)
        self.assertEqual(updated_ad.name, update_name)
        self.assertEqual(updated_ad.ad_account_id, self._ad_account_id)
        self.assertEqual(updated_ad.ad_group_id, self.ad_group.id)
        self.assertEqual(updated_ad.pin_id, self.pin.id)

    def test_get_ad(self):
        _api: AdsApi = self._api

        ad_create_request: AdCreateRequest = AdCreateRequest(
            ad_account_id=self._ad_account_id,
            ad_group_id=self.ad_group.id,
            creative_type=CreativeType('REGULAR'),
            pin_id=self.pin.id,
            name='Test_create_ad',
            status=EntityStatus('ACTIVE'),
        )

        created_request = _api.ads_create(
            ad_account_id=self._ad_account_id,
            ad_create_request=[ad_create_request]
        )
        created_ad = parse_to_object(created_request)

        returned_ad = _api.ads_get(
            ad_account_id=self._ad_account_id,
            ad_id=created_ad.id,
        )

        self.assertIsNotNone(returned_ad)
        self.assertEqual(returned_ad.name, created_ad.name)
        self.assertEqual(returned_ad.ad_account_id, created_ad.ad_account_id)
        self.assertEqual(returned_ad.ad_group_id, created_ad.ad_group_id)
        self.assertEqual(returned_ad.pin_id, created_ad.pin_id)


if __name__ == '__main__':
    unittest.main()
