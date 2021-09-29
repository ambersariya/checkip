from unittest import TestCase

import requests
import requests_mock
from requests_mock.mocker import Mocker
from src.check_ip import CheckIp


class TestCheckIp(TestCase):
    def test_check_ip_returns_string(self):
        checkip = CheckIp()
        actual = checkip.check()
        assert type(actual) == str

    @requests_mock.Mocker()
    def test_check_ip_returns_valid_ip_address(self, requests_mock: Mocker):
        checkip = CheckIp()
        requests_mock.get(checkip.URL, text="127.0.0.1")
        actual = checkip.check()
        assert actual in "127.0.0.1"

    @requests_mock.Mocker()
    def test_check_ip_raises_exception_when_there_is_no_connectivity(
        self, requests_mock: Mocker
    ):
        checkip = CheckIp()
        requests_mock.get(checkip.URL, exc=requests.exceptions.ConnectTimeout)
        with self.assertRaises(CheckIp.NoConnectivity):
            checkip.check()
