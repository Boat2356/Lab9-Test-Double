# Lab9 - Test double
# Integration testing using Mock - Crate Mock object to mimic the behavior of external service
# นายชลพัฒน์ ปิ่นมุนี รหัส 653380126-0 sec1

from unittest.mock import patch
import sys
sys.path.append('source')
import currency_exchanger
from utils import get_mock_currency_api_response
import unittest

class TestCurrencyExchanger(unittest.TestCase):
    def setUp(self):
        self.currency_exchanger = currency_exchanger.CurrencyExchanger()
        self.mock_api_response = get_mock_currency_api_response()

    @patch('currency_exchanger.requests')
    def test_get_currency_rate(self, mock_requests):
        # Assign mock's return value
        mock_requests.get.return_value = self.mock_api_response
        
        # Act - execute class under test
        self.currency_exchanger.get_currency_rate()
        
        # Check whether the mocked method is called
        mock_requests.get.assert_called_once()
        
        # Check whether the mocked method is called with the right parameter
        mock_requests.get.assert_called_with(self.currency_exchanger.currency_api, params={'from': self.currency_exchanger.base_currency, 'to': self.currency_exchanger.target_currency})

        # Assert the returned responses
        self.assertIsNotNone(self.currency_exchanger.api_response)
        self.assertEqual(self.currency_exchanger.api_response, self.mock_api_response.json())
        

    @patch('currency_exchanger.requests')
    def test_currency_exchange(self, mock_requests):
        # Assign mock's return value
        mock_requests.get.return_value = self.mock_api_response
        
        # Act - execute class under test
        amount = 100
        result = self.currency_exchanger.currency_exchange(amount)
        
        # Check whether the mocked method is called
        mock_requests.get.assert_called_once()
        
        # Check whether the mocked method is called with the right parameter
        mock_requests.get.assert_called_with(self.currency_exchanger.currency_api, params={'from': self.currency_exchanger.base_currency, 'to': self.currency_exchanger.target_currency})
        
        # Expected result
        expected_result = amount * self.mock_api_response.json()['result'][self.currency_exchanger.target_currency]
        
        self.assertEqual(result, expected_result)          
                
if __name__ == '__main__':
    unittest.main()